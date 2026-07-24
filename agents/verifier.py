"""
verifier.py

Fact Verification Agent

Uses retrieved context from the RAG pipeline
to evaluate whether the news article's claims
appear supported.
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.verifier_prompt import VERIFIER_PROMPT

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
    temperature=0.1,
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
# Fact Verification Agent
# --------------------------------------------------
def verify_news(news_text: str, context: str = "") -> str:
    """
    Verify a news article using retrieved RAG context.

    Args:
        news_text: Original news article.
        context: Retrieved supporting context.

    Returns:
        Verification report.
    """

    news_text = str(news_text)
    context = str(context)

    if not news_text.strip():
        return "No news article was provided."

    if not context.strip():
        context = (
            "No supporting documents were retrieved. "
            "Evaluate only the internal consistency of the article. "
            "Clearly mention that external verification could not be performed."
        )

    prompt = f"""
{VERIFIER_PROMPT}

Retrieved Context:
{context}

News Article:
{news_text}

Instructions:

- Compare the article with the retrieved context.
- Identify claims that are supported.
- Identify claims that cannot be verified.
- Mention possible inconsistencies.
- Give an overall confidence level.
- Never invent facts.
"""

    try:

        response = llm.invoke(prompt)

        return extract_text(response)

    except Exception as e:

        return f"Error while verifying the article:\n\n{e}"


# --------------------------------------------------
# Test
# --------------------------------------------------
if __name__ == "__main__":

    sample_news = """
Artificial Intelligence is transforming healthcare by improving disease
detection and assisting doctors with medical image analysis.
"""

    sample_context = """
AI is widely used in healthcare for medical imaging,
early disease detection, predictive analytics,
and clinical decision support.
"""

    print("=" * 60)
    print("Fact Verification")
    print("=" * 60)

    result = verify_news(sample_news, sample_context)

    print(result)