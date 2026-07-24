"""
safety.py

Safety Agent

Checks whether a news article contains:
- Hate speech
- Violence
- Harassment
- Toxic language
- Graphic content
- Potential misinformation risks
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.safety_prompt import SAFETY_PROMPT

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

    # Already a string
    if isinstance(content, str):
        return content

    # Gemini sometimes returns a list
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
# Safety Analysis Agent
# --------------------------------------------------
def safety_check(news_text: str) -> str:
    """
    Analyze a news article for potentially unsafe,
    harmful, misleading, or sensitive content.

    Args:
        news_text: Original news article.

    Returns:
        Safety analysis report.
    """

    news_text = str(news_text)

    if not news_text.strip():
        return "No news article was provided."

    prompt = f"""
{SAFETY_PROMPT}

News Article:
{news_text}

Instructions:

- Detect harmful or unsafe content.
- Identify misinformation risks.
- Detect hate speech or harassment.
- Detect violent or graphic descriptions.
- Detect self-harm related content.
- Detect medical or legal misinformation.
- Mention if the article appears generally safe.
- Provide a short explanation.
"""

    try:

        response = llm.invoke(prompt)

        return extract_text(response)

    except Exception as e:

        return f"Error while performing safety analysis:\n\n{e}"


# --------------------------------------------------
# Test
# --------------------------------------------------
if __name__ == "__main__":

    sample_news = """
Researchers have developed a new AI system capable of
detecting early-stage cancer from medical images with
improved accuracy.
"""

    print("=" * 60)
    print("Safety Analysis")
    print("=" * 60)

    result = safety_check(sample_news)

    print(result)