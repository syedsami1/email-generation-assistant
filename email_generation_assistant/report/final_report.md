# 📊 Email Generation Assistant: Final Report

This report presents the design, implementation, evaluation, and comparative analysis of an AI-powered Email Generation Assistant. The system generates professional emails based on structured inputs (Intent, Key Facts, Tone) using Groq-compatible LLMs.

---

## 1. Prompt Template

The system uses an **advanced prompt engineering approach** combining:

- Role-based prompting  
- Few-shot example  

### Prompt Design

The model is instructed to act as a:

> “World-class Executive Assistant and Professional Email Writer”

It is guided to:
- Generate structured emails (Subject, Greeting, Body, Closing)
- Integrate all key facts naturally
- Maintain consistent tone

### Few-shot Example

A reference example is included in the prompt demonstrating:
- Input → Intent, Facts, Tone  
- Output → Fully structured professional email  

This improves:
- Consistency  
- Structure adherence  
- Output quality  

---

## 2. Custom Evaluation Metrics

A custom evaluation framework was implemented using an **LLM-as-a-Judge** approach.

| Metric | Definition | Logic | Range |
|------|--------|------|------|
| **Relevance (Fact Recall)** | Measures inclusion of key facts | LLM checks presence of facts | 0–1 |
| **Professional Quality** | Grammar, tone, structure | LLM rates 1–5 → normalized | 0–1 |
| **Personalization** | Measures specificity vs generic output | LLM rates 1–5 → normalized | 0–1 |

---

## 3. Model Comparison and Analysis

### Models Evaluated

- **Model A:** `llama-3.1-8b-instant` (fast baseline)
- **Model B:** `openai/gpt-oss-120b` (high-quality model)

---

## Observations from Outputs

### Model A (llama-3.1-8b-instant)
- Occasionally produced **incomplete or poorly structured emails**
- Sometimes **missed subject line**
- Responses were **generic**
- Less consistent formatting

---

### Model B (openai/gpt-oss-120b)
- Generated **well-structured emails consistently**
- Included:
  - Subject line
  - Clear formatting
  - Strong professional tone
- Demonstrated:
  - Better **context understanding**
  - Better **fact integration**
  - Strong **personalization**

Example improvements observed:
- Added quantified achievements
- Used clearer professional language
- Maintained consistent tone

---

## Key Failure Mode (Model A)

The primary limitation of Model A was:

- Weak structure (missing subject / formatting)
- Generic responses
- Inconsistent tone adherence

---

## Final Recommendation

We recommend **openai/gpt-oss-120b** for production use because:

- Superior email structure  
- Better personalization  
- Stronger tone consistency  
- More professional output quality  

Although Model A is faster, the quality gap is significant for real-world applications.

---

## 4. Evaluation Data

Evaluation was conducted on **10 scenarios**.

Raw results are available in:

- `evaluation/results_model_a.csv`
- `evaluation/results_model_b.csv`

Each file contains:
- Scenario ID  
- Relevance score  
- Quality score  
- Personalization score  
- Average score  

---

## 5. Conclusion

This project demonstrates:

- Effective prompt engineering using role + few-shot techniques  
- A custom evaluation framework tailored for email generation  
- A meaningful comparison between two LLM models  

The results show that **larger, higher-capability models significantly improve output quality**, especially for structured communication tasks like email generation.

This system is suitable for real-world applications such as:
- Automated communication tools  
- AI assistants  
- Business email generation systems  