import streamlit as st

from rag.retrieve import retrieve_context
from agents.summarizer import summarize_news
from agents.bias_agent import detect_bias
from agents.verifier import verify_news
from agents.safety import safety_check

st.set_page_config(
    page_title="NewsLens AI",
    page_icon="📰",
    layout="wide",
)

# ---------- Minimal visual styling ----------
st.markdown("""
<style>
    .stApp {
        background: #f5f7fb;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }

    .main-title {
        font-size: 2.4rem;
        font-weight: 750;
        color: #172554;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 1.8rem;
    }

    .input-heading {
        color: #1e293b;
        font-size: 1.1rem;
        font-weight: 650;
        margin-bottom: 0.5rem;
    }

    div[data-testid="stTextArea"] textarea {
        border: 1px solid #cbd5e1;
        border-radius: 10px;
        background: #ffffff;
        font-size: 15px;
    }

    div.stButton > button {
        background: #2563eb;
        color: white;
        border: none;
        border-radius: 9px;
        font-weight: 600;
        padding: 0.65rem 1rem;
    }

    div.stButton > button:hover {
        background: #1d4ed8;
        color: white;
        border: none;
    }

    div[data-testid="stTabs"] button {
        font-weight: 600;
    }

    .result-heading {
        color: #1e3a8a;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.7rem;
    }

    .footer {
        color: #94a3b8;
        text-align: center;
        font-size: 0.85rem;
        margin-top: 2.5rem;
    }
</style>
""", unsafe_allow_html=True)


# ---------- Header ----------
st.markdown(
    "<div class='main-title'>📰 NewsLens AI</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>AI-powered news analysis using Gemini and Retrieval-Augmented Generation (RAG)</div>",
    unsafe_allow_html=True,
)

st.divider()


# ---------- Article input ----------
st.markdown(
    "<div class='input-heading'>Paste your news article</div>",
    unsafe_allow_html=True,
)

news_article = st.text_area(
    "News article",
    height=260,
    placeholder="Paste the complete news article here...",
    label_visibility="collapsed",
)

analyze = st.button(
    "🚀 Analyze News",
    use_container_width=True,
)


# ---------- Analysis ----------
if analyze:

    if not news_article.strip():
        st.warning("Please paste a news article before starting the analysis.")
        st.stop()

    with st.spinner("Retrieving relevant documents..."):
        context = retrieve_context(news_article)

    with st.spinner("Generating article summary..."):
        summary = summarize_news(news_article, context)

    with st.spinner("Analyzing possible bias..."):
        bias = detect_bias(news_article)

    with st.spinner("Verifying article claims..."):
        verification = verify_news(news_article, context)

    with st.spinner("Checking content safety..."):
        safety = safety_check(news_article)

    st.success("News analysis completed successfully!")

    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📝 Summary",
        "⚖️ Bias Analysis",
        "✅ Verification",
        "🛡️ Safety",
        "📚 Retrieved Context",
    ])

    with tab1:
        st.markdown("<div class='result-heading'>Article Summary</div>",
                    unsafe_allow_html=True)
        st.write(summary)

    with tab2:
        st.markdown("<div class='result-heading'>Bias Analysis</div>",
                    unsafe_allow_html=True)
        st.write(bias)

    with tab3:
        st.markdown("<div class='result-heading'>Fact Verification</div>",
                    unsafe_allow_html=True)
        st.write(verification)

    with tab4:
        st.markdown("<div class='result-heading'>Safety Analysis</div>",
                    unsafe_allow_html=True)
        st.write(safety)

    with tab5:
        st.markdown("<div class='result-heading'>Retrieved Documents</div>",
                    unsafe_allow_html=True)

        if context:
            st.write(context)
        else:
            st.info("No relevant documents were retrieved.")

st.markdown(
    "<div class='footer'>NewsLens AI · Multi-Agent News Analysis</div>",
    unsafe_allow_html=True,
)
