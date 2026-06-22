import os
from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI(
    title="Radiology Report Summarisation API",
    description="Summarises radiology findings into a concise clinical impression."
)

MODEL_PATH = "graceogungbesan1809-debug/flan-t5-radiology"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model     = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

device = "cuda" if torch.cuda.is_available() else "cpu"
model  = model.to(device)
model.eval()


class FindingsRequest(BaseModel):
    findings: str


class ImpressionResponse(BaseModel):
    impression: str


@app.get("/")
def root():
    return {"status": "Radiology summarisation API is running"}


@app.post("/summarise", response_model=ImpressionResponse)
def summarise(request: FindingsRequest):
    if not request.findings or not request.findings.strip():
        return {"impression": "Error: 'findings' field must not be empty."}

    prompt = "generate a concise clinical impression from these radiology findings: " + request.findings
    inputs = tokenizer(
        prompt, return_tensors="pt", truncation=True, max_length=512
    ).to(device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens       = 32,
            min_new_tokens       = 3,
            length_penalty       = 2.0,
            num_beams            = 4,
            no_repeat_ngram_size = 3,
            early_stopping       = True,
        )

    impression = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return {"impression": impression}