# Use a slim Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Accept the HF model name as a build argument with a sensible default
ARG HF_MODEL_NAME="srajam696/mlops-emotion-distilbert"

# Set it as an environment variable so the inference script can access it
ENV HF_MODEL_NAME=${HF_MODEL_NAME}

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install only inference dependencies (we don't need datasets for inference)
# Make sure transformers and torch are in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ src/

# Set the default command to run the inference script
CMD ["python", "src/inference.py"]
