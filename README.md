#  Secure AI Code Generator

A secure Python code generation web application built using **Streamlit** that generates code from user prompts, checks syntax, performs a basic security scan, and assigns a trust score to evaluate the generated code quality.



##  Features

- Generate Python code from natural language prompts  
- Syntax validation using Python AST  
- Security scanning for unsafe functions  
- Dynamic trust score calculation  
- Clean and interactive Streamlit UI  
- Fast response without heavy API dependency  



##  Tech Stack

- Python  
- Streamlit  
- AST (Abstract Syntax Tree)  
- Custom security checker  
- Rule-based trust scoring  



##  Project Structure

```bash
secure-ai-code-generator/
│── app.py
│── generator.py
│── checker.py
│── scorer.py
│── requirements.txt
│── README.md
