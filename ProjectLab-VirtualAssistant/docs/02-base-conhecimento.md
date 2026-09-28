# Base de Conhecimento

## Dados Utilizados

A base de conhecimento combina dados mockados do cliente com conteúdos educacionais sobre finanças e economia.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Consultar assuntos e interações financeiras anteriores |
| `perfil_investidor.json` | JSON | Contextualizar renda, patrimônio, objetivos e perfil do cliente |
| `produtos_financeiros.json` | JSON | Consultar características dos produtos financeiros disponíveis no banco fictício |
| `transacoes.csv` | CSV | Analisar receitas, despesas e categorias de gastos |
| `conceitos_financeiros.json` | JSON | Explicar conceitos de educação financeira |
| `conceitos_economia.json` | JSON | Explicar conceitos básicos de economia |
| `organizacao_financeira.json` | JSON | Auxiliar na organização de salário, gastos, orçamento e metas financeiras |

Os dados de cliente e produtos são **mockados e utilizados exclusivamente para demonstração do protótipo.**

---

## Adaptações nos Dados

Os dados fornecidos pelo desafio serão complementados com conteúdos específicos de educação financeira e economia básica.

Também foram realizados ajustes nos dados mockados existentes para melhorar a consistência das informações e permitir uma personalização mais adequada das respostas.

O agente poderá utilizar o perfil, objetivos, histórico e movimentações do cliente para contextualizar suas respostas, mas não deverá transformar esses dados automaticamente em recomendações de investimento.

Os produtos financeiros serão utilizados para explicar características e categorias de produtos e, quando apropriado, indicar que o cliente procure orientação profissional para avaliar uma opção específica.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos CSV e JSON serão carregados pela aplicação e disponibilizados ao agente conforme a necessidade da interação.

Os dados do cliente poderão ser combinados com a base educacional para gerar um contexto específico para cada pergunta.

### Como os dados são usados no prompt?

Os dados relevantes serão incluídos no contexto enviado ao modelo de linguagem.

O agente deverá:

1. Utilizar os dados do cliente quando forem relevantes para a pergunta
2. Consultar a base educacional para explicar conceitos
3. Utilizar os dados de produtos para apresentar informações objetivas sobre suas características
4. Evitar inventar informações que não estejam disponíveis
5. Nunca indicar um produto financeiro específico como sendo a melhor opção ou garantir resultados
6. Recomendar orientação profissional quando a situação exigir uma análise financeira individualizada

---

## Exemplo de Contexto Montado

```
CLIENTE

Nome: João Silva
Idade: 32 anos
Profissão: Analista de Sistemas
Renda mensal: R$ 5.000,00
Perfil de investidor: Moderado
Objetivo principal: Construir reserva de emergência
Patrimônio total: R$ 15.000,00
Reserva de emergência atual: R$ 10.000,00

META

Reserva de emergência:
- Valor desejado: R$ 15.000,00
- Valor atual: R$ 10.000,00
- Prazo: junho de 2026

CONCEITO CONSULTADO

Reserva de emergência:
Valor financeiro destinado a cobrir despesas inesperadas,
devendo priorizar segurança e disponibilidade.

PRODUTO CONSULTADO

CDB Liquidez Diária:
- Categoria: Renda fixa
- Risco informado: Baixo
- Liquidez: Diária
- Aporte mínimo: R$ 100,00

INSTRUÇÃO

1. Utilize os dados acima para contextualizar a resposta
2. Não indique um produto como a melhor opção para o cliente
3. Explique suas características e, quando necessário, oriente o cliente a procurar um profissional para avaliar as opções disponíveis.
```