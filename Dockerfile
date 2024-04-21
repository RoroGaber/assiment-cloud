# Use the official Python image as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /python-image 

# Copy the requirements file into the container
COPY  . .
# Install NLTK 
Run python -m pip install --upgrade pip 
RUN pip install nltk
# Run the Python script when the container launches
CMD ["python", "app.py"]
