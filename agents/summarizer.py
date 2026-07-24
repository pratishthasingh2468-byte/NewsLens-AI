"""
summarizer.py
Summary Agent
Generates a concise summary of a news article.
"""
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.summary_prompt import SUMMARY_PROMPT

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
    temperature=0.3,
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

    # Already plain text
    if isinstance(content, str):
        return content

    # If returned as a list
    if isinstance(content, list):
        text = []

        for item in content:

            # AIMessage content blocks
            if hasattr(item, "text"):
                text.append(item.text)

            # Dictionary blocks
            elif isinstance(item, dict):
                text.append(item.get("text", ""))

            # Fallback
            else:
                text.append(str(item))

        return "\n".join(text)

    return str(content)


# --------------------------------------------------
# Summarizer Agent
# --------------------------------------------------
def summarize_news(news_text: str, context: str = "") -> str:
    """
    Generate a concise summary of the news article.

    Args:
        news_text: User news article.
        context: Retrieved RAG context.

    Returns:
        Summary as plain text.
    """

    news_text = str(news_text)
    context = str(context)

    if not news_text.strip():
        return "No news article was provided."

    prompt = f"""
{SUMMARY_PROMPT}

Retrieved Context:
{context}

News Article:
{news_text}

Generate a concise, factual summary.
"""

    try:

        response = llm.invoke(prompt)

        return extract_text(response)

    except Exception as e:

        return f"Error while generating summary:\n\n{e}"


# --------------------------------------------------
# Test
# --------------------------------------------------
if __name__ == "__main__":

    sample_news = """
Artificial Intelligence is transforming healthcare by helping doctors detect
diseases earlier, improving medical imaging, and assisting hospitals with
predictive analytics.
"""

    sample_context = """
AI is increasingly used in hospitals for diagnosis,
medical imaging, and patient outcome prediction.
"""

    print("=" * 60)
    print("Generating Summary...")
    print("=" * 60)

    result = summarize_news(sample_news, sample_context)

    print(result)