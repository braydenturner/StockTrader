# Use a Miniconda base image (you can also use continuumio/anaconda3 if you prefer)
FROM continuumio/miniconda3:latest

# Create a working directory in the container
WORKDIR /app

# Copy your exported environment.yml into the container
COPY shared_libs/ /app/shared_libs
COPY celery_worker/ /app

# Create the Conda environment from environment.yml
RUN conda env create -f environment.yml

ENV PYTHONPATH=/app

SHELL ["conda", "run", "-n", "celery_worker_env", "/bin/bash", "-c"]

# Finally, run your script using the conda environment
CMD ["conda", "run", "--no-capture-output", "-n", "celery_worker_env", \
     "celery", "-A", "shared_libs.tasks.celery_app", "worker", "--loglevel=INFO"]