import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #141e30, #243b55);
        color: white;
        text-shadow: 1px 1px 1px black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1498050108023-c5249f4df085");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>

[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
}

.stButton>button {
    background-color: #ff4b4b;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: black;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ADD THIS BELOW
st.markdown("""
<style>
.stDownloadButton>button {
    color: black;
}

.stFileUploader * {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

def create_pdf_report(ai_response):

    pdf_path = "resume_analysis_report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "<b>AI Resume Analysis Report</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    content = Paragraph(
        ai_response.replace("\n", "<br/>"),
        styles['BodyText']
    )

    elements.append(content)

    doc.build(elements)

    return pdf_path
# API KEY
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# MODEL
model = genai.GenerativeModel("gemini-flash-lite-latest")

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# TITLE
st.title("📄 AI Resume Analyzer")
st.markdown("Upload your resume and get AI-powered career feedback.")

st.sidebar.title("About")

st.sidebar.info("""
This AI Resume Analyzer helps users:
- Improve resumes
- Identify missing skills
- Get career suggestions
- Increase ATS score
""")

# FILE UPLOADER
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted
    
    st.success("Resume uploaded successfully!")
    st.subheader("Resume Text")
    st.write(text)

    prompt = f"""
    Analyze this resume.

    Give:
    1. Resume score out of 100
    2. Missing skills
    3. Strengths
    4. Weaknesses
    5. Improvement suggestions
    6. Best suited career roles

    Resume:
    {text}
    Give output in this format:

    Resume Score:
    Missing Skills:
    Strengths:
    Weaknesses:
    Suggestions:
    Career Roles:

    Also analyze ATS friendliness.
    """

    if st.button("Analyze Resume"):

     with st.spinner("Analyzing Resume..."):

        response = model.generate_content(prompt)

        st.subheader("AI Analysis")

        st.write(response.text)

        # CREATE PDF
        pdf_file = create_pdf_report(response.text)

        # DOWNLOAD BUTTON
        with open(pdf_file, "rb") as file:

            st.download_button(
                label="Download PDF Report",
                data=file,
                file_name="AI_Resume_Report.pdf",
                mime="application/pdf"
            )
            