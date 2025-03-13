import uvicorn
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from shared_libs.tasks.data import fetch_daily_data


app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/data")
def get_data():
    print("/api/data")
    result = fetch_daily_data.delay()
    
    return {"data": result.get()}


if __name__ == "__main__":
    print("Running app")
    
    port = int(os.environ.get("PORT", 8000))  # default to 8000 if not set
    uvicorn.run(app, host="0.0.0.0", port=port)