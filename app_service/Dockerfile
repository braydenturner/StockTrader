# Use a Miniconda base image (you can also use continuumio/anaconda3 if you prefer)
FROM continuumio/miniconda3:latest

# Create a working directory in the container
WORKDIR /app

# Copy your exported environment.yml into the container
COPY shared_libs/ /app/shared_libs
COPY app_service/ /app
COPY .env/ /app
COPY environment.yml /app

# Create the Conda environment from environment.yml
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "trading_bot_env", "/bin/bash", "-c"]

# Expose a port if needed (e.g., for an API service)
EXPOSE 8000

ENV PYTHONPATH=/app

# Finally, run your script using the conda environment
CMD ["conda", "run", "--no-capture-output", "-n", "trading_bot_env", "python", "app/app.py"]