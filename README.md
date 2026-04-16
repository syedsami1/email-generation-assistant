# 🚀 Email Generation Assistant 

An AI-powered system that generates **professional emails** from structured inputs using LLMs, with a custom evaluation framework and model comparison.

---

## ✨ Features

- Generate emails using:
  - Intent
  - Key Facts
  - Tone
- Advanced prompt engineering (Role + Few-shot)
- Compare two LLMs:
  - `llama-3.1-8b-instant`
  - `openai/gpt-oss-120b`
- Custom evaluation using 3 metrics
- CSV-based performance analysis

---

## 📁 Project Structure

```

email_generation_assistant/
│
├── email_generator/
│   ├── email_generator.py   # Core generation logic
│   └── main.py              # CLI interface
│
├── evaluation/
│   ├── evaluator.py         # Evaluation pipeline
│   ├── evaluation_scenarios.py
│   ├── results_model_a.csv
│   └── results_model_b.csv
│
├── report/
│   └── final_report.md      # Detailed analysis
│
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pip install groq python-dotenv
````

---

### 2. Set API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

### 🔹 1. Run Interactive Email Generator

```bash
python -m email_generator.main
```

Then enter:

```
Intent: Job application
Facts:
- 3 years experience
- Skilled in Python
- done
Tone: formal
```

---

### 🔹 2. Run Evaluation

```bash
python evaluation/evaluator.py
```

---

## 📊 Evaluation Metrics

| Metric               | Description                      |
| -------------------- | -------------------------------- |
| Relevance            | Checks if key facts are included |
| Professional Quality | Grammar, tone, structure         |
| Personalization      | Measures specificity vs generic  |

---

## 🧠 Model Comparison

| Model                | Description        |
| -------------------- | ------------------ |
| llama-3.1-8b-instant | Fast baseline      |
| openai/gpt-oss-120b  | High-quality model |

---

## 📈 Key Findings

* Model B (`gpt-oss-120b`) produced:

  * Better structured emails
  * Stronger tone adherence
  * Higher personalization

* Model A:

  * Faster
  * But more generic and less consistent

---

## ✅ Recommendation

Use **openai/gpt-oss-120b** for production due to superior quality and reliability.

---

## 📄 Report

Detailed report available at:

```
report/final_report.md
```

Includes:

* Prompt template
* Metric definitions
* Raw evaluation data
* Comparative analysis

---

## 🚀 Tech Stack

* Python
* Groq API
* LLM-based evaluation (LLM-as-a-Judge)


