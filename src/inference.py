import os
from transformers import pipeline

def main():
    input_text = os.environ.get("INPUT_TEXT")
    if not input_text:
        print("No INPUT_TEXT environment variable provided. Using a sample text.")
        input_text = "I feel so happy and excited today!"
        
    model_name = os.environ.get("HF_MODEL_NAME", "srajam696/mlops-emotion-distilbert")
    token = os.environ.get("HF_TOKEN")
    
    print(f"Loading model: {model_name}")
    try:
        # Load the pipeline for text classification
        classifier = pipeline("text-classification", model=model_name, token=token)
        
        # Run inference
        result = classifier(input_text)
        
        print("\n--- Inference Result ---")
        print(f"Input Text: {input_text}")
        print(f"Prediction: {result[0]['label']}")
        print(f"Confidence: {result[0]['score']:.4f}")
        print("------------------------\n")
        
    except Exception as e:
        print(f"An error occurred during inference: {e}")

if __name__ == "__main__":
    main()
