from datasets import load_dataset

def load_pubmedqa():
    dataset = load_dataset("pubmed_qa", split="train[:1%]")
    return dataset