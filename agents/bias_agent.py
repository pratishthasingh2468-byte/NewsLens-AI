"""
bias_agent.py

Bias Detection Agent

Analyzes a news article for:
- Political bias
- Emotional language
- Subjective wording
- Neutrality
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.bias_prompt import BIAS_PROMPT

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Initialize Gemini Model
# --------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
)


# --------------------------------------------------
# Helper Function
# --------------------------------------------------
def extract_text(response) -> str:
    """
    Safely extract plain text from a LangChain AIMessage.
    Always returns a string.
    """

    if response is None:
        return ""

    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text = []

        for item in content:

            if hasattr(item, "text"):
                text.append(item.text)

            elif isinstance(item, dict):
                text.append(item.get("text", ""))

            else:
                text.append(str(item))

        return "\n".join(text)

    return str(content)


# --------------------------------------------------
# Bias Detection Agent
# --------------------------------------------------
def detect_bias(news_text: str) -> str:
    """
    Analyze a news article for political,
    emotional, ideological, or framing bias.

    Args:
        news_text: News article text.

    Returns:
        Bias analysis as plain text.
    """

    news_text = str(news_text)

    if not news_text.strip():
        return "No news article was provided."

    prompt = f"""
{BIAS_PROMPT}

News Article:
{news_text}

Analyze the article for:

- Political bias
- Emotional language
- Loaded wording
- One-sided reporting
- Missing viewpoints

Provide a balanced explanation.
"""

    try:

        response = llm.invoke(prompt)

        return extract_text(response)

    except Exception as e:

        return f"Error while detecting bias:\n\n{e}"


# --------------------------------------------------
# Test
# --------------------------------------------------
if __name__ == "__main__":

    sample_news = """
The government announced a new economic policy expected to create millions of jobs.
Supporters praised the decision as historic, while critics argued it could increase
inflation and public debt.
"""

    print("=" * 60)
    print("Bias Analysis")
    print("=" * 60)

    result = detect_bias(sample_news)

    print(result)