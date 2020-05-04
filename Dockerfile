# Pull base image
FROM python:3

# Ensures that the python output is sent to terminal and that no *.pyc files are created
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create root directory for our project in the container
RUN mkdir /code

# Set the working directory to /code
WORKDIR /code

# Copy the current directory contents into the container at /code
ADD . /code/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run entrypoint script to do the rest of the setup for django + database
RUN chmod +x ./bin/docker-entrypoint.sh
RUN chmod +x ./bin/wait-for-it.sh
ENTRYPOINT ["./bin/docker-entrypoint.sh"]
