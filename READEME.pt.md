# Visão geral

A intenção deste projeto é criar um chatbot baseado em resenhas de filmes para que você possa fazer perguntas e ter uma conversa livre sobre o assunto.

## Motivação

Recentemente tive que adquirir um novo serviço de internet, então tentei fazê-lo usando o chatbot disponível na empresa. Percebi que a conversa com o chatbot foi baseada em regras e condições. Portanto, para cada pergunta que eu estava fazendo ao bot, ele estava me enviando uma lista de opções que eu precisava escolher para ir para a próxima etapa da conversa. A experiência não foi boa para mim e não resolveu o meu problema.
Então, comecei a pesquisar possíveis soluções, apenas por curiosidade, e encontrei alguns conteúdos na internet falando sobre o treinamento de um chatbot usando Processamento de Linguagem Natural (PNL). Após essa leitura, decidi aceitar o desafio e treinar meu chatbot para conversas naturais.

## O bot de bate-papo funciona da seguinte maneira:
1. uma mensagem de entrada é fornecida pelo usuário;
2. o chat bot recebe esta mensagem e salva em um arquivo de dados para futuras melhorias;
3. a mensagem é pré-processada para servir à rede neural e ser rotulada como uma pergunta
(1) ou resposta (0).
4. a mesma mensagem original também é pré-processada para servir ao algoritmo de
semelhança;
1. em qualquer um dos pré-processamento, no caso de mensagens que não podem ser
ser usado, apenas como números, apenas caracteres especiais, etc.,
uma mensagem de emergência padrão é retornada ao usuário.
2. esta mensagem padrão é obtida de uma lista de mensagens padrão;
5. A mensagem pré-processada é rotulada e, dependendo do rótulo, é comparada
com a lista de mensagens do mesmo marcador. por exemplo, se a mensagem estiver rotulada
como uma pergunta, é comparado ao conjunto de dados de perguntas
6. Se uma mensagem semelhante for encontrada, o bot de bate-papo retorna a resposta associada a esta mensagem.
7. Se não houver mensagem semelhante, uma mensagem tipo padrão é retornada
para o usuário.
8. Todas as mensagens

## Conceitos
### Pré-processamento de dados
O conjunto de dados é pré-processado em pares de mensagens de entrada e saída, por exemplo "o que é?" - "um cachorro". Essas mensagens são usadas para mapear a resposta mais próxima a uma determinada mensagem do usuário.

### Ranking da página
Um gráfico de mensagens semelhantes foi feito para alimentar o algoritmo Page Rank, de forma que as mensagens mais relevantes sejam classificadas no topo da lista. A classificação é usada na mensagem de saída.

### Similaridade de Cossino
A similaridade de Cossino é usada para comparar a mensagem de entrada do usuário com a mensagem mais semelhante no conjunto de dados. Este valor é somado ao Page Rank da mensagem.
Este processamento é feito para todas as mensagens e a mensagem com o valor mais alto (Page Rank + similaridade) é retornada ao usuário.

## Como isso foi feito
1. Usou um conjunto de dados com conversas fictícias sobre filmes
2. Processou os dados para construir a sequência de conversas
3. Aplicar maiúsculas, lematização e lematização para reduzir a variação das palavras
4. Enriqueceu o conjunto de dados com mais recursos (semelhança de frases)
5. Treine cada mensagem com sua resposta correspondente usando uma Rede Neural
6. Construiu uma interface de usuário para permitir a interação com o chatbot
7. Implementou o chatbot em um domínio público e gratuito (Heroku)

## O chatbot
### Bibliotecas usadas
- pandas
- re
- keras
- nump
- sklearn
- Scipy
- train_test_split
- matemática

## Interface
O bot de bate-papo está implantado em https://chatbotnaive.herokuapp.com/, então experimente :)
<br/> <br/>
! [texto alternativo] (https://i.ibb.co/8BsCQ8h/chatbotui.png)

## Instalando o chatbot localmente

`` `bash
pip3 install -r requisitos.txt
`` `
Nota: para Windows, instale o Xming e exporte o DISPLAY. O servidor deve estar em execução antes de iniciar a IU. Mais detalhes neste tíquete: https://stackoverflow.com/questions/39804366/tclerror-no-display-name-and-no-display-environment-variable-on-windows-10-bas/39805613.

## Executando o servidor de aplicativos

`` `bash
cd scr /
python3 app.py
`` `
acessar a url informada pelo servidor. Por exemplo http://127.0.0.1:5000/

## Executando o chatbot na CLI

`` `bash
cd scr /
python3 run_cli.py
`` `
## Executando o chatbot em uma IU de desktop

`` `bash
exportar DISPLAY = 0.0
cd scr /
python3 run_ui.py
`` `

## Executando os testes e cobertura

`` `bash
cd src /
sh Cover.sh
`` `

O relatório de cobertura é gerado em htmlcov / index.html

A cobertura atual é:
```bash
Name                        Stmts   Miss  Cover
-----------------------------------------------
backend/__init__.py             0      0   100%
backend/chatbot.py             40      3    92%
backend/dataset.py             28      0   100%
backend/pre_processing.py      62      0   100%
backend/predict.py             34      3    91%
backend/similarity.py          46      0   100%
backend/utils.py               17      0   100%
settings.py                    16      0   100%
-----------------------------------------------
TOTAL                         243      6    98%
```


## Atenção

- Este bot de bate-papo foi desenvolvido usando WSL Ubuntu, portanto, não é garantido que funcione em ambientes diferentes.
- Para treinar novamente o bot de chat é necessário usar os notebooks seguindo a ordem dos arquivos 001, 002 ... e talvez os notebooks precisem ser adaptados dependendo do seu conjunto de dados.
- Os blocos de notas geram os 3 conjuntos de dados usados ​​pelo bot de bate-papo: movie_lines_pre_processed_for_test.tvs, page_rank_questions.txt e page_rank_answers.txt. Se estiver fazendo um novo treinamento, obtenha os arquivos gerados em notebooks / chatdata e coloque em src / chatdata.
- O model.h5 e o tokenizer.pickle também são gerados pelos notebooks e é necessário copiar ambos em src / chatdata.
- Este bot de bate-papo foi desenvolvido usando 30.000 mensagens devido a problemas de desempenho, então preste atenção ao seu conjunto de dados se você for re-treinar o bot de bate-papo.


## Referências
- Conjunto de dados https://www.kaggle.com/Cornell-University/movie-dialog-corpus?select=movie_lines.tsv
- https://shanebarker.com/blog/deep-learning-chatbot/
- https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44