# NOC-Generator
This Streamlit app automates the creation of No Objection Certificates (NOCs) for podcast guests using Azure OpenAI. It collects guest details, generates a legally styled NOC, allows review and editing, and outputs a professional PDF, ready to download and use.

## Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/saishagoel27/NOC-Generator.git
cd NOC-Generator
```

2. **Create and activate a virtual environment**:

```bash
python -m venv venv
.venv\Scripts\activate  # On Windows
# OR
source .venv/bin/activate  # On macOS/Linux
```

3. **Install the dependencies**:

```bash
pip install -r requirements.txt
```

4. **Add your Azure OpenAI credentials**:

   Create a `config.py` file with:

```python
API_KEY = "your-azure-openai-api-key"
API_ENDPOINT = "https://your-endpoint.openai.azure.com/"
API_VERSION = "2023-05-15"
ENGINE = "your-deployment-name"
```

## Run the App

```bash
streamlit run app.py
```


For structure reference, see `config_example.py` in the repo.

---
