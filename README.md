# 🛠 Smart Bathroom Renovation Pricing Engine (RAG + Groq)

This project is an **AI-powered smart renovation pricing engine** that takes a **messy voice transcript** of a renovation request, retrieves relevant pricing & material data using **RAG (Retrieval-Augmented Generation)**, and generates a **structured renovation quote** in JSON format.  

It uses:
- **Groq LLM API** for fast & accurate quote generation
- **Hugging Face embeddings + ChromaDB** for context retrieval
- **Pydantic** for JSON schema validation
- **Custom logic** for:
  - Labor cost calculation
  - VAT rate application
  - Minimum margin protection

---

## 🚀 Features
- **Free-form voice transcript input**
- **RAG-powered retrieval** from structured data (`materials.json` & `price_template.csv`)
- **Schema-validated JSON output**
- **Automatic labor cost calculation**
- **VAT rate based on location**
- **Margin protection** to avoid underpricing
- **Output saved to `output/sample_quote.json`**

---

## 📂 Project Structure
.
├── rag/
│   ├── retriever.py        # Loads embeddings & retrieves context from vector DB
│   ├── schema.py           # Defines Quote schema using Pydantic
│   ├── labor_calc.py       # Calculates labor cost
│   ├── vat_rules.py        # Returns VAT rates by country
│   ├── embedder.py         # Creates vector DB
├── materials.json          # Example materials dataset
├── price_template.csv      # Example price template dataset
├── app.py                  # Main script to run the engine
├── requirements.txt        # Python dependencies
└── output/
    └── sample_quote.json   # Generated quote output

---

## ⚙️ Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/smart-pricing-engine.git
cd smart-pricing-engine
```

2️⃣ **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Set up environment variables**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Usage

Run the script:
```bash
python app.py
```

You will be prompted:
```
🧠 Enter the voice transcript for the renovation project:
```

Example input:
```
Client wants to renovate a small 4m² bathroom. Remove old tiles, redo plumbing for the shower, replace the toilet, install a vanity, repaint the walls.
```

---

## 📤 Output
The generated quote will be saved in:
```
output/sample_quote.json
```

Example output:
```json
{
  "zone": "bathroom",
  "tasks": [
    {
      "name": "Tile Removal",
      "labor": {
        "hours": 5,
        "rate_per_hour": 40,
        "total": 200
      },
      "material_cost": 0,
      "vat_rate": 0.2,
      "margin": 100,
      "total_price": 360
    }
  ],
  "margin": 100,
  "currency": "EUR"
}
```

---

## 📚 How It Works
1. **Transcript Input** → You enter a free-form renovation request.
2. **Context Retrieval (RAG)** → The system fetches relevant pricing & material info.
3. **LLM Processing (Groq)** → The model generates a quote following the `Quote` schema.
4. **Post-Processing**:
   - Labor cost calculation (`labor_calc.py`)
   - VAT application (`vat_rules.py`)
   - Margin protection logic
5. **Output Saving** → Final JSON quote is stored in `output/sample_quote.json`.

---

## 🧠 Technologies Used
- **Python**
- **LangChain + ChromaDB** (RAG implementation)
- **Hugging Face Sentence Transformers** (Embeddings)
- **Groq LLM API**
- **Pydantic** (Schema validation)
- **dotenv** (Env variable management)

---

## 📌 Notes
- First run may require generating the vector database:
```python
# Inside app.py
#from rag.embedder import create_vectorstore
#create_vectorstore()
```
- The system is configured for **France (FR)** VAT rates but can be extended.

---

## 🏗 Future Improvements
- Multi-language support
- Integration with speech-to-text for direct audio input
- Web UI for quote generation
- More granular task breakdowns

---

## 📜 License
MIT License. See `LICENSE` for details.
