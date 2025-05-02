
import torch
from torch.utils.data import DataLoader
from data_loader import load_pubmedqa
from embedder import BioBERTEmbedder
from classifier import MLPClassifier

def train_model():
    # Load dataset
    dataset = load_pubmedqa()

    # Initialize model components
    embedder = BioBERTEmbedder()
    model = MLPClassifier(input_dim=768)

    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = torch.nn.CrossEntropyLoss()

    # Training loop
    model.train()
    for batch in DataLoader(dataset, batch_size=8):
        questions, contexts, labels = batch["question"], batch["context"], batch["label"]
        embeddings = embedder.encode(questions, contexts)
        optimizer.zero_grad()
        outputs = model(embeddings)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        print(f"Loss: {loss.item()}")

    torch.save(model.state_dict(), "pubmedqa_model.pth")

train_model()
    