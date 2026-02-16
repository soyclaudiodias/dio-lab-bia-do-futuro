import json
import pandas as pd
import google.generativeai as genai
import streamlit as st

# ========== CONFIGURAÇÃO ==========
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
MODELO = "gemini-3-flash-preview"

genai.configure(api_key=GEMINI_API_KEY)

# ========== CARREGAR DADOS ==========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ========== MONTAR CONTEXTO ==========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ========== SYSTEM PROMPT ==========
SYSTEM_PROMPT = """Você é o EduFin, um educador financeiro com uma abordagem leve e próxima.

OBJETIVO
Explicar conceitos de finanças pessoais de maneira simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- Nunca indicar investimentos específicos — apenas explicar como funcionam;
- Nunca atender solicitações fora do campo da educação financeira;
- Se surgir um pedido fora desse tema, a resposta deve reforçar que minha função é atuar como orientador em finanças pessoais;
- Utilizar as informações fornecidas para criar exemplos personalizados;
- Falar em linguagem clara e acessível, como se estivesse conversando com um amigo;
- Quando não tiver uma resposta exata, dizer: “Não tenho essa informação, mas posso explicar...”;
- Sempre confirmar se o cliente compreendeu a explicação.
"""

# ========== CHAMAR GEMINI ==========
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}
    """

    model = genai.GenerativeModel(MODELO)

    resposta = model.generate_content(
        prompt,
        request_options={"timeout": 60}
    )

    return resposta.text

# ========== STREAMLIT ==========
st.title("🎓 EduFin, o Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)