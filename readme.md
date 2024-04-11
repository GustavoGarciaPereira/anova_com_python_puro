# Análise de Variância (ANOVA) com Python

Este repositório contém um script Python para realizar uma análise de variância (ANOVA) de um único fator em um conjunto de dados. A análise é feita através de uma abordagem orientada a objetos, facilitando a reutilização do código para diferentes conjuntos de dados ou análises similares.

## Descrição

A análise de variância (ANOVA) é um método estatístico usado para testar se existem diferenças significativas entre as médias de três ou mais grupos independentes. Neste projeto, implementamos uma classe `AnaliseVariacao` que calcula a soma dos quadrados total, a soma dos quadrados entre os grupos, a soma dos quadrados do erro, além de outras estatísticas relevantes como graus de liberdade, variâncias da amostra, médias quadráticas, e o valor F.

## Dependências

-   Python 3.x
-   Pandas

Instale as dependências necessárias utilizando pip:

```python
pip install pandas
```

## Uso

1.  Certifique-se de que o seu conjunto de dados esteja no formato CSV e contenha pelo menos duas colunas: uma com os valores a serem analisados e outra com os grupos correspondentes a esses valores.
2.  Salve o script da classe `AnaliseVariacao` em um arquivo chamado `analise_variacao.py`.
3.  No seu script principal, importe a classe e utilize-a para analisar o seu conjunto de dados.

```python
import pandas as pd
from analise_variacao import AnaliseVariacao
```

# Carregando os dados
```python
df = pd.read_csv('data.csv')
```


# Criando uma instância da classe AnaliseVariacao

```python
analise = AnaliseVariacao(df, 'VALOR_COLUNA', 'GRUPO_COLUNA')
```


# Executando a análise

```python
print(f"Soma dos quadrados total: {analise.calcular_soma_quadrados_total()}")
print(f"Soma dos quadrados entre grupos: {analise.calcular_soma_quadrados_entre_grupos()}")
print(f"Soma dos quadrados do erro: {analise.calcular_soma_quadrados_erro()}")
```

# Continue com as demais estatísticas conforme necessário

Substitua `'VALOR_COLUNA'` e `'GRUPO_COLUNA'` pelos nomes reais das colunas no seu conjunto de dados.