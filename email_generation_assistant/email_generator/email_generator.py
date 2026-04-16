import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class EmailGenerator:
    def __init__(self, model_name="llama-3.1-8b-instant"):
        """
        Initializes the EmailGenerator with a specific model.

        Available models:
        - llama-3.1-8b-instant (fast)
        - llama-3.1-70b-versatile (high quality)
        """
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model_name = model_name

        # Advanced Prompt Template
        self.prompt_template = """
### ROLE ###
You are a world-class Executive Assistant and Professional Communications Expert.

### TASK ###
Generate a professional email based on the provided inputs.

### INPUTS ###
- Intent: {intent}
- Key Facts:
{key_facts}
- Tone: {tone}

### GUIDELINES ###
1. Create a strong subject line
2. Use proper greeting
3. Integrate all key facts naturally
4. Maintain tone
5. Provide professional closing

### OUTPUT ###
Generate only the final email.
"""

    def generate_email(self, intent: str, key_facts: list[str], tone: str) -> str:
        formatted_key_facts = "\n".join([f"- {fact}" for fact in key_facts])

        prompt = self.prompt_template.format(
            intent=intent,
            key_facts=formatted_key_facts,
            tone=tone
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional email assistant."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"Error generating email: {e}"