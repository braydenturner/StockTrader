import psycopg2

from psycopg2.extras import execute_batch
from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional, Type
from pydantic import BaseModel
from datetime import date
from pandas import DataFrame


class Data(SQLModel, table=True):
    pass

class StockTickerData(Data, table=True):
    ticker: str = Field(primary_key=True)
    date_: date = Field(primary_key=True)
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    adj_close: Optional[float]
    volume: Optional[int]
    
    @classmethod
    def convert_df_to_stock_data(cls, ticker: str, ticker_data: DataFrame) -> list:
        records = []
        # Convert DataFrame rows to StockData instances.
        for _, row in ticker_data.iterrows():
            row_dict = row.to_dict()
            # Ensure that the 'date' field is a date object.
            if hasattr(row_dict.get("date"), "date"):
                row_dict["date"] = row_dict["date"].date()
            # Add the ticker symbol to the record.
            row_dict["ticker"] = ticker
            try:
                stock_record = StockTickerData(**row_dict)
                records.append(stock_record)
            except Exception as e:
                print(f"Error parsing row for {ticker}: {e}")
                
        return records



class Database:
    
    
    def __init__(self, user: str, password: str, host: str, database: str):
        self.conn  = psycopg2.connect(
           host=host,
           database=database,
           user=user,
           password=password
        )
        
    def __del__(self):
        self.conn.commit()
        self.conn.close()
    
    
    def create_table(self, table_name: str, model: Type[BaseModel]):
        
        type_mapping = {
            str: "VARCHAR",
            int: "INTEGER",
            float: "FLOAT",
            date: "DATE"
        }
        
        columns = []
        for field_name, field in model.model_fields.items():
            # Get the field type. For Optional fields, field.type_ returns the inner type.
            field_type = field.type_
            pg_type = type_mapping.get(field_type, "VARCHAR")
            columns.append(f"{field_name} {pg_type}")
        
        # Define a composite primary key using ticker and date.
        primary_key = "PRIMARY KEY (ticker, date)"
        create_stmt = f"CREATE TABLE IF NOT EXISTS {table_name} (" + ", ".join(columns + [primary_key]) + ");"
        
        cursor = self.conn.cursor()
        cursor.execute(create_stmt)
        self.conn.commit()
        cursor.close()
        print(f"Table '{table_name}' is ready.")
        
    def store(self, table_name: str, data: list[Data]):
        columns = list(Data.__fields__.keys())
        placeholders = ", ".join(["%s"] * len(columns))
        columns_sql = ", ".join(columns)
        insert_stmt = (
            f"INSERT INTO {table_name} ({columns_sql}) "
            f"VALUES ({placeholders}) "
            f"ON CONFLICT (ticker, date) DO NOTHING;"
        )
        
        # Prepare the data as a list of tuples.
        data_tuples = [tuple(record.model_dump().get(col) for col in columns) for record in data]
        
        cursor =self.conn.cursor()
        try:
            execute_batch(cursor, insert_stmt, data_tuples)
            self.conn.commit()
            print(f"Data for stored successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error inserting data: {e}")
        finally:
            cursor.close()