import os
import json
from dotenv import load_dotenv
from groq import Groq
from rag.schema import Quote
from rag.retriever import get_retriever
from rag.labor_calc import calculate_labor_cost
from rag.vat_rules import get_vat_rate
# Optional: first run only to generate DB
#from rag.embedder import create_vectorstore

# ---------- Configuration ----------
MIN_MARGIN_PERCENT = 0.20  # 20% minimum margin
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
retriever = get_retriever()

transcript = input("🧠 Enter the voice transcript for the renovation project:\n")

docs = retriever.invoke(transcript)
context = "\n\n".join([doc.page_content for doc in docs])

client = Groq(api_key=GROQ_API_KEY)
from rag.schema import Quote

prompt = f"""
You are a smart renovation pricing assistant. Given the context data and the client’s voice transcript, generate a renovation quote
using this JSON schema (do not include markdown, only return valid JSON):

{json.dumps(Quote.model_json_schema(), indent=2)}

Transcript:
\"\"\"
{transcript}
\"\"\"

Context:
\"\"\"
{context}
\"\"\"
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates renovation quotes in JSON."},
        {"role": "user", "content": prompt}
    ]
)

llm_output = response.choices[0].message.content

try:
    quote = Quote.model_validate_json(llm_output)

    for task in quote.tasks:
        task.labor.total = calculate_labor_cost(task.labor.hours, task.labor.rate_per_hour)
        task.vat_rate = get_vat_rate("FR")
        subtotal = task.labor.total + task.material_cost
        protected_margin = max(task.margin, subtotal * MIN_MARGIN_PERCENT)
        task.margin = round(protected_margin, 2)
        task.total_price = round(subtotal + protected_margin + (subtotal * task.vat_rate), 2)

    quote.margin = round(sum(task.margin for task in quote.tasks) / len(quote.tasks), 2)

    os.makedirs("output", exist_ok=True)
    with open("output/sample_quote.json", "w") as f:
        json.dump(quote.dict(), f, indent=2)
    print("✅ Quote saved to output/sample_quote.json")

except Exception as e:
    print("❌ Failed to parse response as valid Quote schema:\n")
    print(llm_output)
    print("\nException:\n", e)