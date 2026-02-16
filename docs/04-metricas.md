# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [V] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [V] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [V] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto BBDC3 no Ibovespa?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [V] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O assistente explicou corretamente os gastos com alimentação, usando apenas os dados do transacoes.csv.
- Respeitou o SYSTEM PROMPT ao não recomendar investimentos específicos, apenas explicar como funcionam.
- Manteve um tom leve, amigável e educacional em todas as respostas.
- Adaptou as explicações ao contexto do cliente (idade, objetivo, perfil, histórico).
- Lidou de forma correta com perguntas fora do escopo (como previsão do tempo), redirecionando para finanças pessoais.
- Explicou produtos financeiros e conceitos (Tesouro Selic, CDB, ações, Ibovespa) sem indicar onde investir.

**O que pode melhorar:**
- Ainda aparece formatação quebrada ou com caracteres repetidos (“R 570,00”, “R 120paraR 200”). Isso indica que o modelo precisa de limpeza de saída ou post-processing antes de exibir.
- Em algumas respostas ele repetiu valores de forma desnecessária (ex.: R$ 570,00 duas vezes na mesma frase).
- Em alguns trechos, poderia confirmar a compreensão do cliente no final, como pedido no SYSTEM PROMPT.
- Em respostas longas, poderia ser mais direto e objetivo — ainda está um pouco verboso.
- Vale incluir um limite de tokens ou instrução explícita para evitar repetições e quebras estranhas em números, o que ainda ocorre.
