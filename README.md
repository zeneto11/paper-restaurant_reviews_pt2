# Identificação de Temas em Comentários de Restaurantes usando BERT e Modelos de Linguagem Generativa

Este repositório contém o código e os datasets utilizados para a análise de comentários em restaurantes, conforme descrito no artigo "Identificação de Temas em Comentários de Restaurantes usando BERT e Modelos de Linguagem Generativa".

## Configuração do Ambiente

Para configurar o ambiente e reproduzir os experimentos, siga os passos abaixo:

```bash
# Criação do ambiente virtual
python -m venv venv
cd venv
source Scripts/activate

# Instalação das dependências
pip install numpy pandas scikit-learn ipykernel maritalk seaborn matplotlib torch transformers python-dotenv
```

## Datasets

Os datasets utilizados neste estudo estão organizados na pasta datasets/folds-4000sentencas. Esses datasets foram obtidos aplicando diferentes técnicas de pré-processamento, como stemming, lematização, uso do spaCy para remoção de classes gramaticais e remoção de stopwords. Apesar de utilizarmos o stemming nos experimentos descritos no artigo, todos os outros datasets com as diferentes técnicas de pré-processamento também estão disponíveis na pasta mencionada.

# Estrutura do Repositório

Este repositório contém os arquivos e diretórios relacionados ao estudo de caso e ao processamento de dados. Abaixo está uma descrição da estrutura e do conteúdo de cada diretório:

- **case_study/**: Contém os notebooks principais usados no estudo de caso.

- **data_processing/**: Scripts para processamento dos dados.

- **datasets/**: Diretório com os datasets utilizados.

  - **folds-4000sentencas/**: Datasets divididos em 5 folds com diferentes técnicas de pré-processamento.
    - **Lemmatization/**: Datasets pré-processados com lematização.
    - **Lemmatization/**: Datasets com apenas verbos, substantivos e adjetivos uasndo a biblioteca spaCy.
    - **Stemming/**: Datasets pré-processados com stemming.
    - **Stopwords/**: Datasets com stopwords removidas.

- **models/**: Diretório com modelos treinados.
  - **1epoch/**: Experimentos com 6 sets diferentes de hiperparâmetros utilizando BERT com 1 epoch.
  - **5epoch/**: Experimentos com 6 sets diferentes de hiperparâmetros utilzando BERT com 5 epochs.
  - **10epoch/**: Experimentos com 6 sets diferentes de hiperparâmetros utilzando BERT com 10 epochs.
  - **logs/**: Contém logs das execuções do modelo MariTalk.
