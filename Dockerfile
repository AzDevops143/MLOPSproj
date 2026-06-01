FROM python:3.11-slim
WORKDIR /app
ARG HF_MODEL_NAME="srajam696/mlops-emotion-distilbert"
ENV HF_MODEL_NAME=${HF_MODEL_NAME}
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
CMD ["python", "src/inference.py"]
