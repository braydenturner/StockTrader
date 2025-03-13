# Use a Miniconda base image (you can also use continuumio/anaconda3 if you prefer)
FROM continuumio/miniconda3:latest

# Create a working directory in the container
WORKDIR /app

# Copy your exported environment.yml into the container
COPY shared_libs/ /app/shared_libs
COPY analytics_service/ /app

# Create the Conda environment from environment.yml
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "analytics_service_env", "/bin/bash", "-c"]

EXPOSE 15672


# Finally, run your script using the conda environment
CMD ["conda", "run", "--no-capture-output", "-n", "analytics_service_env", "python", "worker.py"]