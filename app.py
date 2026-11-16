import streamlit as st

from rag.retrieve import retrieve_context
from agents.summarizer import summarize_news
from agents.bias_agent import detect_bias
from agents.verifier import verify_news
from agents.safety import safety_check

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="NewsLens AI",
    page_icon="📰",
    layout="wide",
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown("""
<style>

.stApp{
    background-color:#FFEFD5;
}

.main-title{
    font-size:42px;
    font-weight:700;
    color:#222;
}

.subtitle{
    color:#555;
    font-size:18px;
    margin-bottom:20px;
}

.block{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 3px 8px rgba(0,0,0,0.08);
}

textarea{
    font-size:16px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.markdown(
    "<div class='main-title'>📰 NewsLens AI</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>Multi-Agent News Analysis using Gemini + RAG</div>",
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# Input
# ---------------------------------------------------

news_article = st.text_area(
    "Paste a News Article",
    height=280,
    placeholder="Paste your article here..."
)

# ---------------------------------------------------
# Button
# ---------------------------------------------------

if st.button("🚀 Analyze News", use_container_width=True):

    if not news_article.strip():
        st.warning("Please paste a news article.")
        st.stop()

    # ----------------------------------------
    # Retrieve Context
    # ----------------------------------------

    with st.spinner("Retrieving relevant documents..."):

        context = retrieve_context(news_article)

    # ----------------------------------------
    # Summary
    # ----------------------------------------

    with st.spinner("Generating summary..."):

        summary = summarize_news(
            news_article,
            context
        )

    # ----------------------------------------
    # Bias
    # ----------------------------------------

    with st.spinner("Analyzing bias..."):

        bias = detect_bias(
            news_article
        )

    # ----------------------------------------
    # Verification
    # ----------------------------------------

    with st.spinner("Verifying facts..."):

        verification = verify_news(
            news_article,
            context
        )

    # ----------------------------------------
    # Safety
    # ----------------------------------------

    with st.spinner("Checking safety..."):

        safety = safety_check(
            news_article
        )

    # ------------------------------------------------

    st.success("Analysis Complete!")

    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📝 Summary",
        "⚖ Bias",
        "✅ Verification",
        "🛡 Safety",
        "📚 Retrieved Context"
    ])

    with tab1:

        st.markdown("### Summary")
        st.write(summary)

    with tab2:

        st.markdown("### Bias Analysis")
        st.write(bias)

    with tab3:

        st.markdown("### Fact Verification")
        st.write(verification)

    with tab4:

        st.markdown("### Safety Analysis")
        st.write(safety)

    with tab5:

        st.markdown("### Retrieved Documents")

        if context:
            st.write(context)
        else:
            st.info("No relevant documents retrieved.")