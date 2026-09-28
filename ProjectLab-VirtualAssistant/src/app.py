import json
import pandas as pd
import requests
import streamlit as st

# ======= CONFIGURAÇÃO =======
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen3.5:2b"

# ======= LOAD DATA =======

def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

perfil = carregar_json("./data/perfil_investidor.json")
produtos = carregar_json("./data/produtos_financeiros.json")
conceitos_financeiros = carregar_json("./data/conceitos_financeiros.json")
conceitos_economia = carregar_json("./data/conceitos_economia.json")
organizacao_financeira = carregar_json("./data/organizacao_financeira.json")

transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")

# ======= MONTAR CONTEXTO =======

contexto = f"""
=== PERFIL DO CLIENTE ===
Nome: {perfil['nome']}
Idade: {perfil['idade']}
Profissão: {perfil['profissao']}
Renda mensal: R$ {perfil['renda_mensal']:.2f}
Perfil de investidor: {perfil['perfil_investidor']}
Objetivo principal: {perfil['objetivo_principal']}
Patrimônio total: R$ {perfil['patrimonio_total']:.2f}
Reserva de emergência atual: R$ {perfil['reserva_emergencia_atual']:.2f}
Aceita risco: {perfil['aceita_risco']}

Metas:
{json.dumps(perfil['metas'], indent=2, ensure_ascii=False)}


=== TRANSAÇÕES ===
{transacoes.to_string(index=False)}


=== HISTÓRICO DE ATENDIMENTOS ===
{historico.to_string(index=False)}


=== PRODUTOS FINANCEIROS ===
{json.dumps(produtos, indent=2, ensure_ascii=False)}


=== CONCEITOS FINANCEIROS ===
{json.dumps(conceitos_financeiros, indent=2, ensure_ascii=False)}


=== CONCEITOS DE ECONOMIA ===
{json.dumps(conceitos_economia, indent=2, ensure_ascii=False)}


=== ORGANIZAÇÃO FINANCEIRA ===
{json.dumps(organizacao_financeira, indent=2, ensure_ascii=False)}
"""

# ======= SYSTEM PROMPT =======
SYSTEM_PROMPT = """

"""

# ======= CHAMAR OLLAMA =======
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()["response"]

# ======= INTERFACE =======
st.set_page_config(
    page_title="Masae - Educadora Financeira",
    page_icon="💰"
)

st.title("💰 Masae - Educadora Financeira 💰")

if pergunta := st.chat_input("Como eu posso lhe ajudar hoje?"):
    st.chat_message("user").write(pergunta)
    with st.spinner("Masae está analisando sua pergunta...."):
        st.chat_message("assistant").write(perguntar(pergunta))
