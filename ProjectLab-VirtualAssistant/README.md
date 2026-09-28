# 🤖 Masae — Educadora Financeira Virtual 💰

O Masae é um protótipo de assistente virtual com Inteligência Artificial criado para apoiar pessoas que estão começando a aprender sobre educação financeira.

A proposta é oferecer explicações simples sobre finanças e economia, auxiliar na organização financeira e utilizar uma base de conhecimento estruturada para contextualizar as respostas.

> Projeto desenvolvido como parte do desafio Construa Seu Assistente Virtual Com Inteligência Artificial.

## 🎯 Objetivo
O Masae foi desenvolvido para auxiliar a pessoa usuária a:

- Compreender conceitos básicos de finanças e economia
- Organizar receitas e despesas
- Acompanhar metas financeiras
- Compreender aspectos básicos de produtos financeiros
- Tomar decisões mais conscientes sobre sua organização financeira

O agente possui finalidade educacional e não substitui um profissional financeiro.

---

## 🤵‍♀️ Persona
Masae é uma educadora financeira virtual.

Sua personalidade é:

- Educada
- Paciente
- Didática
- Respeitosa
- Cordial

Seu objetivo é explicar assuntos financeiros de maneira acessível, evitando linguagem excessivamente técnica.

---

## 🧠 Base de Conhecimento

O projeto utiliza dados mockados organizados em arquivos JSON e CSV:

```
data/
├── historico_atendimento.csv
├── perfil_investidor.json
├── produtos_financeiros.json
├── transacoes.csv
├── conceitos_financeiros.json
├── conceitos_economia.json
└── organizacao_financeira.json
```

A base contém informações sobre:

- Perfil e objetivos financeiros
- Metas
- Transações
- Histórico de atendimentos
- Organização financeira
- Conceitos de educação financeira
- Conceitos básicos de economia
- Características de produtos financeiros

> Os dados são fictícios e utilizados exclusivamente para demonstração do protótipo.

---

## 📝 Prompts

As instruções do agente foram desenvolvidas para orientar o comportamento da Masae e reduzir respostas inventadas.

Entre as principais regras estão:

- Utilizar as informações disponíveis na base de conhecimento
- Não inventar informações
- Admitir quando não houver dados suficientes
- Explicar conceitos de forma simples
- Não realizar operações financeiras
- Não prometer resultados
- Não indicar diretamente a compra de ativos financeiros

A documentação dos prompts está disponível na pasta **[docs](./docs/prompts.md)**

## 📂 Estrutura do Projeto

```
ProjectLab-VirtualAssistant/
├── data/                                   # Base de conhecimento mockada
├── docs/                                   # Documentação do projeto
├── src/                                    # Código-fonte da aplicação
└── README.md                               # Este arquivo
```

---

## 🛠️ Tecnologias

- Python
- Streamlit
- Pandas
- JSON
- CSV
- Ollama / qwen3.5:2b

---

## 🔬 Avaliação

A avaliação do projeto considera cenários como:

| Cenário |	Comportamento esperado |
| ------- | ---------------------- |
| Conceito financeiro |	Explicar utilizando a base |
| Meta financeira | Utilizar os dados disponíveis |
| Gastos | Consultar as transações |
| Conceito econômico | Utilizar a base de economia |
| Produto financeiro | Explicar suas características |
| Pedido de recomendação direta | Evitar recomendação de ativo |
| Informação inexistente | Informar que não possui dados suficientes |
| Pergunta fora do escopo |	Informar a limitação do agente |

Os principais critérios considerados são **aderência à base, clareza, segurança e ausência de informações inventadas.**

---

## ⚠️ Limitações e aprendizados
Este projeto foi desenvolvido como um MVP educacional, dentro de uma janela de desenvolvimento limitada.

Durante a implementação, foram encontradas limitações relacionadas principalmente à execução local de modelos de linguagem e aos recursos de hardware disponíveis no ambiente de desenvolvimento. Por esse motivo, nem todas as etapas planejadas puderam ser concluídas ou refinadas como inicialmente previsto.

Ainda assim, a experiência foi extremamente importante para compreender, na prática, que construir um assistente de IA envolve muito mais do que apenas escrever um prompt.

O projeto permitiu experimentar conceitos como:

- Definição de um problema real
- Criação de uma persona
- Organização de uma base de conhecimento
- Construção de prompts
- Prevenção de alucinações
- Integração entre dados e modelo de linguagem
- Desenvolvimento de uma interface conversacional
- Avaliação de respostas
- Tomada de decisões técnicas sob restrições reais

A Masae representa, portanto, uma primeira versão do projeto, que pode evoluir futuramente com uma integração mais robusta com modelos de linguagem, RAG, busca semântica, memória de conversação e avaliações automatizadas.

Mais do que buscar uma solução perfeita, este projeto representa o aprendizado obtido durante o processo de aprender fazendo. 🚀