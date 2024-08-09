# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /titanic_app

# Copy the current directory contents into the container at /app
COPY . /titanic_app

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN python install_requirements.py

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80"]
