import json
import os
import pandas as pd
from datasets import load_dataset


def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Strip punctuation
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def main():
    print("Loading dair-ai/emotion dataset...")
    # Load a small text classification dataset
    dataset = load_dataset("dair-ai/emotion", "split")

    # We will just use train and test splits for simplicity, or just train and
    # validation
    df_train = dataset['train'].to_pandas()
    df_val = dataset['validation'].to_pandas()

    print("\n--- RAW DATA INSPECTION ---")
    print(f"Training set size: {len(df_train)}")
    print(f"Validation set size: {len(df_val)}")
    print("Structure of first row:", df_train.iloc[0].to_dict())

    print("\nClass distribution (Train):")
    print(df_train['label'].value_counts(normalize=True))

    # Check for missing values
    print("\nMissing values in train:")
    print(df_train.isnull().sum())

    print("\n--- DATA CLEANING ---")
    # 1. Handle missing values (drop them)
    df_train = df_train.dropna()
    df_val = df_val.dropna()

    # 2. Remove duplicates
    initial_len = len(df_train)
    df_train = df_train.drop_duplicates(subset=['text'])
    print(f"Removed {initial_len - len(df_train)} duplicate rows from train.")

    # 3. Lowercase and strip punctuation
    df_train['text'] = df_train['text'].apply(clean_text)
    df_val['text'] = df_val['text'].apply(clean_text)

    print("\nSample cleaned text:")
    print(df_train['text'].head(3).tolist())

    # Save id2label mapping
    # The dataset features provide the class names
    features = dataset['train'].features['label']
    id2label = {i: name for i, name in enumerate(features.names)}

    os.makedirs("data", exist_ok=True)
    mapping_path = "id2label.json"
    with open(mapping_path, "w") as f:
        json.dump(id2label, f, indent=4)
    print(f"\nSaved label mapping to {mapping_path}")

    # Save the prepared datasets locally
    train_path = "data/train_clean.csv"
    val_path = "data/val_clean.csv"
    df_train.to_csv(train_path, index=False)
    df_val.to_csv(val_path, index=False)
    print(f"Saved cleaned datasets to {train_path} and {val_path}")

    print("\nData Preparation Complete!")


if __name__ == "__main__":
    main()
