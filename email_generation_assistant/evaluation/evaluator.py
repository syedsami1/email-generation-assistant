import os
import csv
import re
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class EmailEvaluator:
    def __init__(self, judge_model="llama-3.1-8b-instant"):
        """
        Judge model is used for scoring (fast + cheap)
        """
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.judge_model = judge_model

    # -------------------------------
    # Metric 1: Relevance (Fact Recall)
    # -------------------------------
    def calculate_relevance(self, generated_email, key_facts):
        found_count = 0

        for fact in key_facts:
            prompt = f"""
Check if the following fact is clearly present in the email.

Fact: "{fact}"

Email:
{generated_email}

Answer ONLY Yes or No.
"""
            response = self.client.chat.completions.create(
                model=self.judge_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )

            answer = response.choices[0].message.content.lower()
            if "yes" in answer:
                found_count += 1

        return found_count / len(key_facts) if key_facts else 1.0

    # -------------------------------
    # Metric 2: Professional Quality
    # -------------------------------
    def evaluate_quality(self, generated_email, tone):
        prompt = f"""
Rate how professional and well-structured this email is.

Also consider if it matches the tone: "{tone}"

Give a score from 1 to 5.
Return ONLY the number.

Email:
{generated_email}
"""
        response = self.client.chat.completions.create(
            model=self.judge_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        try:
            score = float(re.search(r"\d+", response.choices[0].message.content).group())
            return (score - 1) / 4.0
        except:
            return 0.0

    # -------------------------------
    # Metric 3: Personalization
    # -------------------------------
    def evaluate_personalization(self, generated_email):
        prompt = f"""
Does this email feel personalized and context-aware, or generic?

Score from 1 (generic) to 5 (highly personalized).
Return ONLY the number.

Email:
{generated_email}
"""
        response = self.client.chat.completions.create(
            model=self.judge_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        try:
            score = float(re.search(r"\d+", response.choices[0].message.content).group())
            return (score - 1) / 4.0
        except:
            return 0.0

    # -------------------------------
    # Run Evaluation
    # -------------------------------
    def run_evaluation(self, model_name, scenarios):
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        from email_generator.email_generator import EmailGenerator

        generator = EmailGenerator(model_name=model_name)
        results = []

        print(f"\nRunning evaluation for {model_name}...\n")

        for scenario in scenarios:
            print(f"Processing Scenario {scenario['id']}...")

            generated_email = generator.generate_email(
                scenario["intent"],
                scenario["key_facts"],
                scenario["tone"]
            )

            relevance = self.calculate_relevance(
                generated_email, scenario["key_facts"]
            )
            quality = self.evaluate_quality(
                generated_email, scenario["tone"]
            )
            personalization = self.evaluate_personalization(
                generated_email
            )

            avg_score = (relevance + quality + personalization) / 3

            results.append({
                "scenario_id": scenario["id"],
                "model": model_name,
                "relevance": round(relevance, 3),
                "quality": round(quality, 3),
                "personalization": round(personalization, 3),
                "average_score": round(avg_score, 3)
            })

        return results

    # -------------------------------
    # Save Results
    # -------------------------------
    def save_results(self, results, filename):
        keys = results[0].keys()

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)

        print(f"\nResults saved to {filename}")


# -------------------------------
# MAIN
# -------------------------------
def main():
    import sys
    sys.path.append(os.getcwd())

    from evaluation.evaluation_scenarios import SCENARIOS

    evaluator = EmailEvaluator()

    # Model A (fast)
    results_a = evaluator.run_evaluation(
        "llama-3.1-8b-instant",
        SCENARIOS
    )
    evaluator.save_results(results_a, "evaluation/results_model_a.csv")

    # Model B (better quality)
    results_b = evaluator.run_evaluation(
        "openai/gpt-oss-120b",
        SCENARIOS
    )
    evaluator.save_results(results_b, "evaluation/results_model_b.csv")


if __name__ == "__main__":
    main()