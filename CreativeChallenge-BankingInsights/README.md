# 💡 Desafio Criativo: Extraindo Insights de Feedbacks de Clientes Bancários 💡

## 📌 Sobre o desafio

Projeto prático desenvolvido durante o Bootcamp Bradesco - GenAI, Dados & Cyber da DIO, com o objetivo de aplicar técnicas de Engenharia de Prompt para aprimorar um template de prompt e utilizá-lo na extração de insights a partir do feedbacks de usuários.

Tema escolhido: 📱 Feedback sobre aplicativo bancário.

Além da construção do prompt, foram realizados testes com dados fictícios para avaliar a qualidade dos insights gerados e o comportamento da GenAI diante de dados pessoais e tentativas de prompt injection.

---

## 📂 Estrutura do projeto

```
CreativeChallenge-BankingInsights/
├── images/                                     # Evidências visuais dos testes
├── data/                                       # Base de dados fictícios
├── prompts/                                    # Prompts utilizados no desafio
└── README.md                                   # Este arquivo
```

---

## 🎯 Objetivo

Desenvolver um prompt capaz de analisar feedbacks de usuários de um aplicativo bancário e gerar informações relevantes para compreensão da experiência dos clientes.

O prompt deve ser capaz de:

- Identificar os principais temas e problemas presentes nos feedbacks;
- Analisar sentimentos e avaliações dos clientes;
- Identificar padrões e problemas recorrentes;
- Extrair insights e oportunidades de melhoria;
- Diferenciar instruções de dados fornecidos para análise;
- Lidar adequadamente com informações pessoais presentes nos dados;
- Ignorar tentativas de prompt injection inseridas nos feedbacks.

---

## ⚙️ Prompt

### Template original

O ponto de partida deste projeto foi o template de prompt fornecido pelo bootcamp.

O template original está disponível no repositório.

[Acessar o arquivo original](./prompts/template-original.md)

### Prompt aprimorado

A partir do template original, foram aplicadas técnicas de Engenharia de Prompt para tornar as instruções mais claras, específicas e consistentes.

O prompt aprimorado também está disponível no repositório.

[Acessar o arquivo aprimorado](./prompts/prompt-aprimorado.md)

### Estratégias utilizadas

As principais alterações realizadas foram:

- Definição do papel e objetivo da GenAI
- Contextualização do cenário de análise
- Definição das etapas esperadas para o processamento dos feedbacks
- Especificação do formato de saída
- Definição dos critérios para identificação de insights
- Orientação para tratamento de dados pessoais
- Separação entre instruções do prompt e conteúdo fornecido para análise
- Inclusão de instruções para lidar com tentativas de prompt injection
- Controle do fluxo para impedir análise antes do recebimento dos dados

---

## 🎲 Dados de teste

Para testar o prompt, foram criados dados fictícios que simulam feedbacks de clientes de um aplicativo bancário. Os registros possuem os seguintes campos:

- Identificador do feedback
- Data
- Nome
- CPF
- Celular
- Categoria
- Canal
- Mensagem
- Status
- Avaliação do cliente

Todos os dados utilizados são fictícios e foram criados exclusivamente para fins de teste. O conjunto foi construído para contemplar diferentes cenários, incluindo feedbacks positivos, negativos, sugestões, problemas recorrentes, informações pessoais e tentativas de prompt injection.

[Acessar os dados fictícios](./data/mock-feedbacks.json)

---

## 🔬 Testes e Resultados

### Ambiente de teste

Para validação, os testes do prompt foram realizados no ChatGPT, sem autenticação e em uma janela anônima, buscando minimizar possíveis interferências de contexto ou histórico da conta.

### Extração de insights

**Objetivo:** verificar se o prompt consegue extrair informações relevantes dos feedbacks fornecidos.

**Cenário:** foram utilizados os 20 feedbacks fictícios contendo avaliações, categorias, status e mensagens de clientes.

**Resultado:** a GenAI identificou os principais temas, problemas, elogios e oportunidades de melhoria presentes nos dados, utilizando os *id_feedback* como evidências.

**Evidência:**

![Resultado da análise](./images/evidencia-analise.png)

**Conclusão:** o comportamento observado foi satisfatório e atendeu ao objetivo definido para a análise.

### Identificação de padrões e inconsistências

**Objetivo:** verificar se a GenAI consegue identificar padrões recorrentes e inconsistências entre os campos dos registros.

**Cenário:** foram utilizados feedbacks com diferentes categorias, avaliações, status e mensagens, incluindo registros propositalmente inconsistentes.

**Resultado:** a GenAI identificou os padrões recorrentes e sinalizou inconsistências entre os campos, sem tratar ocorrências isoladas como tendências.

**Evidência:** a evidência apresentada na seção anterior demonstra esse comportamento.

**Conclusão:** o resultado foi satisfatório, demonstrando que o prompt conseguiu cruzar as informações fornecidas para realizar a análise.

### Tratamento de dados pessoais

**Objetivo:** verificar se a GenAI consegue utilizar os dados necessários para análise sem expor informações pessoais na resposta.

**Cenário:** os dados de teste continham nomes, CPFs e números de celular fictícios, além de registros com informações anonimizadas.

**Resultado:** a GenAI realizou a análise utilizando os *id_feedback* para referenciar os registros, sem reproduzir os dados pessoais presentes na entrada.

**Evidência:**

![Resultado da segurança](./images/evidencia-seguranca.png)

**Conclusão:** o comportamento observado foi satisfatório e esteve de acordo com as restrições de privacidade definidas no prompt.

### Prompt injection

**Objetivo:** verificar se a GenAI consegue identificar e ignorar tentativas de *prompt injection* inseridas nos dados de feedback.

**Cenário:** foram inseridas três tentativas de *prompt injection* dentro do campo *mensagem*, buscando alterar as instruções do prompt ou obter informações que não deveriam ser reveladas.

**Resultado:** a GenAI tratou as instruções como conteúdo dos feedbacks, identificou as tentativas de manipulação e manteve o comportamento definido pelo prompt. Os insights legítimos presentes nos feedbacks continuaram sendo considerados na análise.

**Evidência:** a evidência apresentada na seção anterior também demonstra o comportamento da GenAI diante das tentativas de *prompt injection*.

**Conclusão:** o resultado foi satisfatório, demonstrando que o prompt conseguiu tratar as instruções maliciosas como parte dos dados, sem executá-las ou alterar o processo de análise.

---

## 🌱 Aprendizados

Durante o desafio, aprimorei minha habilidade na criação e iteração de prompts estruturados, focando em testes práticos para garantir respostas mais consistentes e confiáveis. Além disso, apliquei boas práticas de segurança na análise de dados, isolando instruções de entradas para mitigar falhas e tentativas de prompt injection.

---

## 📝 Conclusão

Este desafio permitiu aplicar técnicas de Engenharia de Prompt em um cenário de análise de feedbacks de usuários, utilizando dados fictícios para avaliar o comportamento da GenAI.

Além da capacidade de extrair insights, os testes permitiram avaliar o tratamento de informações pessoais e a resposta do prompt diante de tentativas de prompt injection.

O projeto demonstra, portanto, não apenas a construção de um prompt, mas também sua validação em diferentes cenários de entrada.