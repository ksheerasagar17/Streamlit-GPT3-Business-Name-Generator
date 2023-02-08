# Use an official Python runtime as the base image
FROM python:3.7-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install Streamlit and required packages
RUN pip install streamlit pandas requests

# Set environment variables for OpenAI API key
ENV OPENAPI_KEY=<your_api_key>

# Run the script when the container launches
CMD [ "python", "./run_ui.py" ]
