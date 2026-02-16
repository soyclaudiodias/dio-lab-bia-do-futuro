# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Usado para contextualizar interações anteriores com o cliente. |
| `perfil_investidor.json` | JSON | Serve para adaptar respostas de acordo com o perfil do investidor. |
| `produtos_financeiros.json` | JSON | Permite sugerir produtos compatíveis com o perfil identificado. |
| `transacoes.csv` | CSV | Utilizado para analisar hábitos e padrões de gastos do cliente. |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

- Os arquivos originais foram expandido com dados fictícios para simular cenários mais completos.
- No caso dos CSV, foram adicionadas novas linhas de interações, receitas e despesas, mantendo o mesmo padrão de colunas.
- No caso dos JSON, foram incluídos novos produtos, seguindo a mesma estrutura e estilo dos dados iniciais.
- As modificações tiveram como objetivo enriquecer os exemplos, sem alterar a lógica ou formato dos arquivos originais.
- Todos os acréscimos são mockados (não reais), criados apenas para fins de demonstração e testes.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Pode trabalhar com os dados de duas formas:
- Colando direto no prompt: Copie e cole o conteúdo dos arquivos (CSV ou JSON) na conversa. É simples e rápido, ótimo para testes imediatos ou quando não há muito volume de informação.
- Carregando via código: Salve os arquivos e faça a leitura deles em um ambiente de programação. Dessa forma, você consegue manipular os dados de maneira estruturada, automatizar análises e integrar com sistemas.

```python
import json
import pandas as pd

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
DADOS DO CLIENTE E PERFIL (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSACOES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida
2025-10-28,Shopping,lazer,300.00,saida
2025-11-01,Salário,receita,5000.00,entrada
2025-11-02,Aluguel,moradia,1200.00,saida
2025-11-04,Supermercado,alimentacao,480.00,saida
2025-11-06,Cinema,lazer,70.00,saida
2025-11-09,Farmácia,saude,120.00,saida
2025-11-12,Restaurante,alimentacao,150.00,saida
2025-11-15,Conta de Água,moradia,95.00,saida
2025-11-18,Uber,transporte,60.00,saida
2025-11-22,Academia,saude,99.00,saida
2025-11-25,Combustível,transporte,270.00,saida
2025-11-28,Spotify,lazer,34.90,saida
2025-12-01,Salário,receita,5000.00,entrada
2025-12-02,Aluguel,moradia,1200.00,saida
2025-12-05,Supermercado,alimentacao,500.00,saida
2025-12-07,Viagem,lazer,800.00,saida
2025-12-10,Farmácia,saude,75.00,saida
2025-12-12,Restaurante,alimentacao,200.00,saida
2025-12-15,Conta de Internet,moradia,120.00,saida
2025-12-18,Uber,transporte,55.00,saida
2025-12-20,Academia,saude,99.00,saida
2025-12-23,Combustível,transporte,260.00,saida
2025-12-27,Show,lazer,250.00,saida

HISTORICO DE ATENDIMENTO DO CLIENTE (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim
2025-11-02,chat,Poupança,Cliente quis saber diferença entre poupança e CDB,sim
2025-11-10,telefone,Cartão de crédito,Cliente relatou cobrança indevida,sim
2025-11-18,email,Investimentos,Cliente solicitou material educativo sobre fundos,sim
2025-11-25,chat,Planejamento,Cliente pediu ajuda para organizar gastos mensais,sim
2025-12-03,chat,Reserva de emergência,Cliente perguntou qual valor ideal para começar,sim
2025-12-12,telefone,App travando,Cliente relatou lentidão ao acessar extrato,sim
2025-12-20,email,Segurança,Cliente pediu informações sobre proteção de dados,sim
2025-12-28,chat,Previdência privada,Cliente quis entender diferenças para Tesouro,sim
2026-01-05,chat,Orçamento familiar,Cliente buscou dicas para dividir despesas,sim
2026-01-12,telefone,Transferência,Cliente relatou demora em TED,sim
2026-01-20,email,Atualização cadastral,Cliente alterou endereço residencial,sim
2026-01-28,chat,Investimentos,Cliente pediu explicação sobre risco x retorno,sim
2026-02-03,chat,Metas financeiras,Cliente revisou objetivo de comprar um carro,sim
2026-02-10,telefone,Cartão bloqueado,Cliente solicitou desbloqueio imediato,sim
2026-02-15,email,Extrato,Cliente pediu envio de extrato detalhado por e-mail,sim

PRODUTOS DISPONIVEIS PARA ENSINO (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  },
  {
    "nome": "Debêntures Incentivadas",
    "categoria": "renda_fixa",
    "risco": "medio",
    "rentabilidade": "IPCA + 5%",
    "aporte_minimo": 1000.00,
    "indicado_para": "Investidores moderados que buscam isenção de IR"
  },
  {
    "nome": "ETF de Índice",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Segue índice de ações",
    "aporte_minimo": 50.00,
    "indicado_para": "Quem deseja investir em bolsa de forma diversificada"
  },
  {
    "nome": "Fundo Imobiliário",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "Dividendos mensais variáveis",
    "aporte_minimo": 100.00,
    "indicado_para": "Investidores que buscam renda passiva"
  },
  {
    "nome": "Criptomoedas",
    "categoria": "alternativo",
    "risco": "alto",
    "rentabilidade": "Altamente volátil",
    "aporte_minimo": 50.00,
    "indicado_para": "Perfil arrojado disposto a assumir riscos elevados"
  },
  {
    "nome": "Tesouro IPCA+",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "IPCA + juros fixos",
    "aporte_minimo": 30.00,
    "indicado_para": "Proteção contra inflação no longo prazo"
  },
  {
    "nome": "CDB de Bancos Médios",
    "categoria": "renda_fixa",
    "risco": "medio",
    "rentabilidade": "110% do CDI",
    "aporte_minimo": 500.00,
    "indicado_para": "Quem busca maior rentabilidade com garantia do FGC"
  },
  {
    "nome": "Fundo Cambial",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "Variação do dólar",
    "aporte_minimo": 200.00,
    "indicado_para": "Investidores que querem proteção cambial"
  },
  {
    "nome": "Ações Individuais",
    "categoria": "variavel",
    "risco": "alto",
    "rentabilidade": "Dependente da empresa",
    "aporte_minimo": 50.00,
    "indicado_para": "Investidores experientes que acompanham o mercado"
  },
  {
    "nome": "Fundo de Previdência",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 1%",
    "aporte_minimo": 200.00,
    "indicado_para": "Planejamento de longo prazo para aposentadoria"
  },
  {
    "nome": "COE (Certificado de Operações Estruturadas)",
    "categoria": "alternativo",
    "risco": "medio",
    "rentabilidade": "Atrelada a índices ou ativos",
    "aporte_minimo": 1000.00,
    "indicado_para": "Investidores que buscam proteção parcial do capital"
  }
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto abaixo foi construído a partir dos dados originais da base de conhecimento, mas em uma versão resumida que mantém apenas os pontos mais relevantes. Isso ajuda a otimizar o uso de tokens. No entanto, é importante destacar que, mais do que reduzir o consumo, o essencial é garantir que todas as informações realmente necessárias estejam disponíveis no contexto para que o agente possa atuar de forma completa e precisa.  

```
DADOS DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Construir reserva de emergência
- Reserva atual: R$ 10.000 (meta: R$ 15.000)

RESUMO DE GASTOS:
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90

PRODUTOS DISPONÍVEIS PARA EXPLICAR:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Multimercado (risco médio)
- Fundo de Ações (risco alto)
```
