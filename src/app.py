import streamlit as st
import json
import os

# Carrega base
base_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'devsecops_conceitos.json')
# fallback para data na raiz
if not os.path.exists(base_path):
    base_path = os.path.join(os.path.dirname(__file__), '..', 'devsecops_conceitos.json')

with open(base_path, 'r', encoding='utf-8') as f:
    BASE = json.load(f)

def responder(pergunta):
    pergunta = pergunta.lower()
    for item in BASE:
        if item["pergunta"].lower() in pergunta or any(p in pergunta for p in item["pergunta"].lower().split()[:2]):
            return f"**[{item['fase']}]** {item['resposta']}"
    return "Ainda não tenho essa informação na minha base sobre DevSecOps, mas posso te explicar as 5 fases: Planejamento, Desenvolvimento, Testes, Implantação e Operações."

st.set_page_config(page_title="SecOps Assistant")
st.title("🛡️ SecOps Assistant")
st.write("Assistente para iniciantes em DevSecOps - 5 fases do ciclo seguro")

pergunta = st.text_input("Digite sua dúvida sobre DevSecOps:")

if pergunta:
    st.success(responder(pergunta))

st.divider()
st.caption("Base: data/devsecops_conceitos.json | Feito por Nikolas Peixoto - DIO")
