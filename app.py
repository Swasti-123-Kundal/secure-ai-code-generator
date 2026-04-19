import streamlit as st
from generator import generate_code
from checker import check_syntax, security_scan
from scorer import calculate_score

st.set_page_config(
    page_title="Secure AI Code Generator",
    page_icon="🔐",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
.stButton>button {
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
}
.code-box {
    background-color:#1e1e1e;
    padding:10px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🔐 Secure AI Code Generator")
st.write("Generate secure Python code with syntax validation and trust score.")

prompt = st.text_area("Enter your coding prompt", height=150)

if st.button("Generate Secure Code"):
    with st.spinner("Generating secure code..."):
        code = generate_code(prompt)

        syntax_ok, syntax_msg = check_syntax(code)
        security_result = security_scan(code)
        score = calculate_score(syntax_ok, security_result)

    st.subheader("🧠 Generated Code")
    st.code(code, language="python")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Syntax Check")
        st.success(syntax_msg)

    with col2:
        st.subheader("🛡 Security Scan")
        st.info(security_result)

    st.subheader("📊 Trust Score")
    st.progress(score / 100)
    st.write(f"### {score}% Secure")