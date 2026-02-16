# 💰 EduFin - Educador Financeiro

Este repositório contém o desenvolvimento completo do **EduFin**, um agente de Inteligência Artificial focado em educação financeira personalizada. O projeto foi desenvolvido como solução para o desafio **BIA do Futuro** na plataforma [DIO](https://www.dio.me/), unindo conceitos de engenharia de prompts, análise de dados e inteligência artificial generativa.

<img width="1919" height="867" alt="Image" src="https://github.com/user-attachments/assets/b53d7aee-f05e-4538-baf1-aa87cf6800d5" />

---

## 📚 Ementa do Projeto
O desenvolvimento foi estruturado em 4 pilares de documentação e implementação:
1. **Modelagem do Agente:** Definição de persona, tom de voz e objetivos de negócio.
2. **Base de Conhecimento:** Estruturação de dados para suporte às decisões da IA.
3. **Engenharia de Prompts:** Criação de diretrizes para respostas precisas e seguras.
4. **Métricas e Avaliação:** Análise de performance e assertividade do educador.

---

## 🧪 Tecnologias e Conteúdos Abordados
### 🛠️ IA & Desenvolvimento
* **LLM:** Integração com modelos GPT (OpenAI) para processamento de linguagem natural.
* **Frameworks:** Utilização de técnicas de RAG (Retrieval-Augmented Generation).
* **Interface:** Prototipagem de chat focada em experiência do usuário (UX).

### 👨‍💻 Áreas de Aplicação
* **Finanças Pessoais:** Diagnóstico de saúde financeira e categorização de gastos.
* **Investimentos:** Sugestão de produtos baseada no perfil de risco do usuário.
* **Análise Preditiva:** Identificação de padrões de consumo e alertas de endividamento.
* **Documentação Técnica:** Escrita de especificações claras para sistemas de IA.

---

## 🧩 Estrutura da Solução
### 📌 Planejamento do Agente
O EduFin atua como um mentor empático. Ele não apenas fornece dados, mas educa o usuário sobre como gerenciar melhor seu patrimônio, utilizando uma linguagem acessível e técnica quando necessário.

### 📌 Base de Dados e RAG
Implementação de uma base de conhecimento robusta que permite ao agente consultar tabelas de produtos financeiros e históricos de transações simulados para dar respostas baseadas em fatos.

### 📌 Engenharia de Prompt
Desenvolvimento de "System Prompts" complexos que garantem que a IA mantenha o foco em finanças, evite dar conselhos ilegais e sempre priorize a segurança financeira do usuário.

---

## 📂 Estrutura de Diretórios
```text
dio-bia
├── data/
│   ├── historico_transacoes.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   └── 04-metricas.md
├── src/
│   ├── app.py
│   └── requirements.txt
└── README.md
```

---

## 🚀 Como Executar
1. **Clone o repositório:**
```bash
git clone https://github.com/soyclaudiodias/dio-bia.git
cd dio-bia
```

2. **Configure o ambiente e as dependências:**
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

3. **Inicie o Agente:**
```bash
# Para visualizar a interface do chatbot
streamlit run src/app.py
```

---

## 👨‍🏫 Créditos
Projeto desenvolvido por **Claudio Dias** durante o Laboratório Prático da **DIO (Digital Innovation One)**.