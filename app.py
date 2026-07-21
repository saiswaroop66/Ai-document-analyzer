import streamlit as st
from pdf_reader import extract_pdf_text
from summarizer import generate_summary

st.set_page_config(
    page_title="AI Document Summarizer",
    page_icon="📄",
    layout="wide"
)

# ------------------------
# Custom CSS
# ------------------------

st.markdown("""
<style>
.main{
    padding-top:20px;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#4CAF50;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:30px;
}

.summary-box{
    background:#f4f4f4;
    padding:20px;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">📄 AI Document Summarizer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload a PDF or Text file and generate an AI-powered summary.</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "txt"]
)

if uploaded_file:

    # Extract Text
    if uploaded_file.type == "application/pdf":
        text = extract_pdf_text(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")

    st.success("Document Loaded Successfully!")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📑 Original Text")

        st.text_area(
            "",
            value=text,
            height=450
        )

    with col2:

        st.subheader("🤖 AI Summary")

        summary_length = st.selectbox(
            "Summary Length",
            [
                "Short",
                "Medium",
                "Detailed"
            ]
        )

        if st.button("Generate Summary", use_container_width=True):

            with st.spinner("Generating Summary..."):

                summary = generate_summary(
                    text,
                    summary_length
                )

            st.success("Summary Generated!")

            st.text_area(
                "",
                value=summary,
                height=450
            )

            st.download_button(
                "⬇ Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain",
                use_container_width=True
            )

else:

    st.info("Upload a PDF or TXT file to begin.")