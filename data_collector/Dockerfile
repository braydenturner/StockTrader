# Use a Miniconda base image (you can also use continuumio/anaconda3 if you prefer)
FROM continuumio/miniconda3:latest

# Create a working directory in the container
WORKDIR /app

# Copy your exported environment.yml into the container
COPY shared_libs/ /app/shared_libs
COPY data_collector/ /app/data_collector
COPY .env/ /app
COPY environment.yml /app

# Create the Conda environment from environment.yml
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "trading_bot_env", "/bin/bash", "-c"]

# Optional: set PYTHONPATH so Python sees /app
ENV PYTHONPATH=/app

# Finally, run Celery worker referencing the shared_libs Celery app
CMD ["conda", "run", "--no-capture-output", "-n", "trading_bot_env", \
     "celery", "-A", "data_collector.tasks", "worker", "--beat", "--loglevel=INFO", "--queues=data_queue"]

# Need to moe the beat to seperate process at some point. Can possible resue this container with new socker entry?
