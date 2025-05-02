
from transformers import AutoTokenizer, AutoModel
import torch

class BioBERTEmbedder:
    def __init__(self, model_name="microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def encode(self, question, context):
        inputs = self.tokenizer(question, context, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.pooler_output
    