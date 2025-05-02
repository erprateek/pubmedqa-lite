
from embedder import BioBERTEmbedder
from classifier import MLPClassifier
import torch

def predict(question, context):
    embedder = BioBERTEmbedder()
    model = MLPClassifier(input_dim=768)
    model.load_state_dict(torch.load("pubmedqa_model.pth"))

    embeddings = embedder.encode(question, context)
    model.eval()
    with torch.no_grad():
        output = model(embeddings)
        _, predicted = torch.max(output, 1)
        return ["yes", "no", "maybe"][predicted.item()]
    