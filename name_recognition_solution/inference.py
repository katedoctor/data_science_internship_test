from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

# Define the path to the directory containing the model files (config.json and model weights)
model_dir = './model_weights'

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForTokenClassification.from_pretrained(model_dir)

# Define your input text for inference
input_text = "I climbed Mount Everest"

# Tokenize the input text
inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)

# Extract the predicted labels (NER tags)
predicted_labels = torch.argmax(outputs.logits, dim=2).squeeze().tolist()

# Convert the predicted labels to token labels using the tokenizer
predicted_tokens = tokenizer.convert_ids_to_tokens(predicted_labels)

# Print the results
print(predicted_tokens)

