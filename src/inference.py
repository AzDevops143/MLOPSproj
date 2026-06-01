import os
from transformers import pipeline


def main():
    input_text = os.environ.get("INPUT_TEXT")
    if not input_text:
        input_text = "I feel so happy and excited today"

    model_name = os.environ.get(
        "HF_MODEL_NAME",
        "srajam696/mlops-emotion-distilbert")
    token = os.environ.get("HF_TOKEN")

    classifier = pipeline("text-classification", model=model_name, token=token)
    result = classifier(input_text)

    print(f"Input Text: {input_text}")
    print(f"Prediction: {result[0]['label']}")
    print(f"Confidence: {result[0]['score']:.4f}")


if __name__ == "__main__":
    main()
