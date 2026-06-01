import json
import os
from datasets import load_dataset
import string


def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def main():
    print("Loading dair-ai/emotion dataset")
    dataset = load_dataset("dair-ai/emotion", "split")
    df_train = dataset['train'].to_pandas()
    df_val = dataset['validation'].to_pandas()

    print(f"Training set size: {len(df_train)}")
    print(f"Validation set size: {len(df_val)}")

    df_train = df_train.dropna()
    df_val = df_val.dropna()

    df_train = df_train.drop_duplicates(subset=['text'])

    df_train['text'] = df_train['text'].apply(clean_text)
    df_val['text'] = df_val['text'].apply(clean_text)

    features = dataset['train'].features['label']
    id2label = {i: name for i, name in enumerate(features.names)}

    os.makedirs("data", exist_ok=True)
    mapping_path = "id2label.json"
    with open(mapping_path, "w") as f:
        json.dump(id2label, f, indent=4)

    df_train.to_csv("data/train_clean.csv", index=False)
    df_val.to_csv("data/val_clean.csv", index=False)
    print("Data preparation finished")


if __name__ == "__main__":
    main()
