# Use a Miniconda base image (you can also use continuumio/anaconda3 if you prefer)
FROM continuumio/miniconda3:latest

# Create a working directory in the container
WORKDIR /app

# Copy your exported environment.yml into the container
COPY shared_libs/ /app/shared_libs
COPY analytics_service/ /app/analytics_service
COPY .env/ /app
COPY environment.yml /app

# Create the Conda environment from environment.yml
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "trading_bot_env", "/bin/bash", "-c"]

EXPOSE 15672

# Optional: set PYTHONPATH so Python sees /app
ENV PYTHONPATH=/app

# Finally, run Celery worker referencing the shared_libs Celery app
CMD ["conda", "run", "--no-capture-output", "-n", "trading_bot_env", \
     "celery", "-A", "analytics_service.tasks", "worker", "--loglevel=INFO", "--queues=analytics_queue"]