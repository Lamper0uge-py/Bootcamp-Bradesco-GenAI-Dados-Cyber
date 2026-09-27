# 🔎 Detecção de Fraudes em Transações de Cartão

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte do Bootcamp Bradesco - GenAI, Dados & Cyber e tem como objetivo explorar a detecção de fraudes em transações de cartão de crédito.

O principal desafio do problema é o forte desbalanceamento entre as classes: a grande maioria das transações é normal, enquanto uma pequena parcela corresponde a fraudes. Por esse motivo, a acurácia não é suficiente para avaliar o modelo.

Neste projeto, o foco foi principalmente em precision, recall e F1-score da classe de fraude.

---

## ▶️ Como executar

1. Clone ou baixe este repositório
2. Abra o notebook **anomaly_detection.ipynb**
3. Instale as bibliotecas necessárias, caso ainda não estejam disponíveis
4. Execute as células do notebook na ordem
5. O dataset será carregado diretamente pelo link utilizado no código

---

## 📂 Estrutura do projeto

```
ProjectLab-AnomalyDetection/                
├── anomaly_detection.ipynb                 # Notebook desenvolvido
└── README.md                               # Este arquivo
```

---

## 🎲 Dataset

Foi utilizado o dataset de transações de cartão de crédito disponibilizado pela atividade.

O dataset foi carregado diretamente pelo link:

**[Dataset](https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv)**

> O arquivo não foi incluído no repositório.

As principais colunas utilizadas são:

- **Time:** tempo decorrido desde a primeira transação
- **Amount:** valor da transação
- **V1 a V28:** variáveis transformadas por PCA
- **Class:** variável alvo, sendo 0 para transação normal e 1 para fraude

### Preparação dos dados

Durante a preparação dos dados foram realizadas as seguintes etapas:

- Carregamento da base com Pandas
- Exploração inicial dos dados
- Análise da proporção entre transações normais e fraudulentas
- Criação da variável Amount_log utilizando transformação logarítmica
- Separação entre variáveis preditoras (X) e variável alvo (y)
- Divisão dos dados em treino e teste utilizando stratify
- Padronização dos dados com StandardScaler

A divisão utilizada foi de 70% para treinamento e 30% para teste.

---

## 🤖 Modelos utilizados

Foram comparados três modelos de classificação:

1. Regressão Logística
2. Random Forest
3. XGBoost

Para lidar com o desbalanceamento, foram utilizados pesos para dar maior importância à classe de fraude.

Na Regressão Logística e no Random Forest foi utilizado **class_weight="balanced"**. No XGBoost foi utilizado **scale_pos_weight**, calculado a partir da quantidade de exemplos das classes no conjunto de treinamento.

---

## 🔬 Avaliação dos modelos

As principais métricas utilizadas foram:

- Precision: entre as transações classificadas como fraude, quantas realmente eram fraude
- Recall: entre as fraudes existentes, quantas foram identificadas pelo modelo
- F1-score: equilíbrio entre precision e recall

O recall recebeu atenção especial porque, em um problema de detecção de fraude, deixar de identificar uma transação fraudulenta é um aspecto importante.

### Resultados

| Modelo | Precision | Recall |	F1-score |
| ------ | --------- | ------ | -------- |
| Regressão Logística | 0.0655 | 0.8784 | 0.1219 |
| Random Forest | 0.6824 | 0.7838 | 0.7296 |
| XGBoost | 0.2805 | 0.8378 | 0.4203 |

> Os valores acima foram obtidos diretamente da execução do notebook.

### Análise

Nos resultados obtidos, o Random Forest apresentou a maior precision e o maior F1-score entre os três modelos, enquanto a Regressão Logística apresentou o maior recall.

O Random Forest apresentou recall de 0.78, precision de 0.68 e F1-score de 0.72 para a classe de fraude. Esses resultados mostram que a avaliação de um modelo de detecção de fraude envolve um equilíbrio entre identificar corretamente as fraudes e evitar um número elevado de falsos positivos.

---

## 📈 Curvas ROC e Precision-Recall

Também foram analisadas as curvas:

- ROC
- Precision-Recall

A curva ROC foi utilizada para observar a relação entre verdadeiros positivos e falsos positivos em diferentes limiares. A curva Precision-Recall foi especialmente importante devido ao forte desbalanceamento da base.

Os gráficos estão disponíveis no notebook.

---

## 🔧 Ajuste do limiar de decisão

Além do limiar padrão de 0.5, foram testados diferentes valores:

- 0.2
- 0.3
- 0.4
- 0.5
- 0.6

Os resultados foram comparados utilizando precision, recall e F1-score.

O limiar escolhido foi 0.6, pois apresentou o maior F1-score entre os valores testados. O resultado obtido nesse limiar foi:

- Precision: 0.37
- Recall: 0.82
- F1-score: 0.51

---

## 📊 Explicabilidade com SHAP

Foi utilizado SHAP para entender quais variáveis tiveram maior influência nas previsões do modelo XGBoost. A análise global mostrou que as variáveis com maior importância foram:

1. V14
2. V4
3. V12
4. V20
5. V10

Também foi analisada uma previsão individual para observar como as variáveis contribuíram para a decisão do modelo.

> Os gráficos gerados pelo SHAP estão disponíveis no notebook.

---

## 🌱 O que foi desenvolvido além do exemplo da aula

Em relação ao exemplo apresentado pela Expert, foram realizadas algumas modificações e adaptações no processo de treinamento e avaliação:

- Utilização de `class_weight="balanced"` na Regressão Logística
- Utilização de `class_weight="balanced"` no Random Forest
- Cálculo do `scale_pos_weight` do XGBoost com base na proporção das classes no conjunto de treinamento, em vez de utilizar um valor fixo
- Padronização das variáveis após a separação entre treino e teste, ajustando o `StandardScaler` somente com os dados de treinamento
- Comparação dos três modelos em uma tabela utilizando precision, recall e F1-score
- Teste de diferentes limiares de decisão no XGBoost e escolha do limiar com base no F1-score
- Explicação de uma previsão individual utilizando SHAP

---

## 📝 Conclusão

O projeto mostrou que, em um problema de detecção de fraude com classes fortemente desbalanceadas, a acurácia isoladamente pode não representar adequadamente a qualidade do modelo. Por isso, foram utilizadas principalmente precision, recall e F1-score para avaliar a classe de fraude.

Os experimentos permitiram comparar diferentes modelos e observar como a alteração do limiar de decisão influencia o equilíbrio entre identificar fraudes e gerar falsos positivos.

> Os resultados apresentados neste README foram obtidos a partir da execução do notebook desenvolvido para o projeto.