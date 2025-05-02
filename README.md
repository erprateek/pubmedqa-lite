
# PubMedQA Transformer-Based NLP Pipeline

This project builds a text classification pipeline for biomedical question answering using PubMedQA.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/erprateek/pubmedqa-lite.git
    cd pubmedqa-lite
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Train the model:
    ```bash
    python train.py
    ```

4. Start the FastAPI server:
    ```bash
    uvicorn serve:app --reload
    ```

## Deploy to AWS

1. Initialize Terraform:
    ```bash
    terraform init
    terraform apply
    ```

2. After deployment, access your app at `http://<public-ip>/predict`.

## License
MIT
    