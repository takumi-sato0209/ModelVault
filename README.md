# ModelVault

## Description
ModelVault is a lightweight Python library for versioning, storing, and retrieving machine learning models locally with simple metadata tracking.

## Features
- Save models with automatic versioning  
- Load specific versions or the latest model  
- Store metadata (author, metrics, tags)  
- List available models and versions  
- Clean up old versions  

## Installation
```bash
pip install modelvault
```

## Usage
```python
from modelvault import ModelVault

vault = ModelVault("./models")
vault.save("my_model", model_object, {"accuracy": 0.92, "author": "Alice"})
latest = vault.load_latest("my_model")
specific = vault.load("my_model", version=2)
print(vault.list_versions("my_model"))