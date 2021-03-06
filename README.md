# Overview

The intention of this project is to create a chatbot based on movie reviews so that you can ask questions and have a free conversation about this topic.

## Motivation

Recently I had to buy a new internet service, so I tried to do it using the available chatbot of the company. I noticed the conversation with the chatbot was based on rules and conditions. Hence, for each question I was doing to the bot, it was sending to me a list of options I needed to choose to go to the next step of the conversation. The experience was not good for me and it did not solve my problem.
So, I started search for possible solutions, just for curiosity, and I found some contents in the internet talking about the training of a chatbot using Natural Language Processing (NLP). After this reading, I decided to take the challenge and train my on chatbot for natural conversations.

## The chat bot works as follows:
1. an input message is provided by the user;
2. the chat bot receives this message and saves it in a datafile for future improvements;
3. the message is preprocessed to serve the neural network and be labeled as a question
(1) or answer (0).
4. the same original message is also preprocessed to serve the algorithm of
similarity;
	1.in any of the preprocessing, in the case of messages that cannot be
be used, as numbers only, only special characters, etc.,
a standard emergency message is returned to the user.
	2. this standard message is fetched from a list of standard messages;
5. The preprocessed message is labeled and depending on the label it is compared
with the list of messages of the same label. for example, if the message is labeled
as a question, it is compared to the questions dataset
6. If a similar message is found, the chat bot returns the associated response to this message.
7. If there is no similar message, a standard kind message is returned
to the user.
8. All messages

## Concepts
### Pre-processing data
The dataset is pre-processed in pairs of entry-output messages, for example "what is it?"-"a dog". Those messages are used to map the closest answer to a given messages from the user.

### Page Rank
A graph of similar messages was done to feed the Page Rank algorithm, so the most relevant messages are ranked on the top of the list. The rank is used to in the output message. 

### Cossine similarity
The Cossine similarity is used to match the entry message of the user against the most similar message in the dataset. This value is summed with the Page Rank of the message.
This processed is done for all messages and the message with the highest value (Page Rank + similarity) is returned to the user.

## How it was be done
1. Used a dataset with fictional conversations about movies
2. Processed the data to build the sequence of conversations
3. Applied capitalization, lemmatization and stemming to reduce the variation of words
4. Enriched the dataset with more features (similarity of sentences)
5. Trained each message with its corresponding answer using a Neural Network
6. Built a user interface to allow the interaction with the chatbot
7. Deployed the chatbot in a free and public domain (Heroku)

## The chatbot
### Used libraries
- pandas
- re
- keras
- nump
- sklearn
- Scipy
- train_test_split
- math

## Interface
The chat bot is deployed at https://chatbotnaive.herokuapp.com/, so try this :)
<br/><br/>
![alt text](https://i.ibb.co/8BsCQ8h/chatbotui.png)

## Installing the chatbot locally

```bash
pip3 install -r requirements.txt
```
Note: for Windows, install the Xming and export the DISPLAY. The server must be running before launch the UI. More details in this ticket: https://stackoverflow.com/questions/39804366/tclerror-no-display-name-and-no-display-environment-variable-on-windows-10-bas/39805613.

## Running the app server

```bash
cd scr/
python3 app.py
```
access the url informed by the server. For example http://127.0.0.1:5000/

## Running the chatbot in CLI

```bash
cd scr/
python3 run_cli.py
```
## Running the chatbot in a Desktop UI

```bash
export DISPLAY=0.0
cd scr/
python3 run_ui.py
```

## Running the tests and coverage

```bash
cd src/
sh coverage.sh
```

The coverage report is generated in htmlcov/index.html

The current coverage is:
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


## Attention

- This chat bot was developed using WSL Ubuntu, so it is not guaranteed to work on different environment.
- To retrain the chat bot it is necessary to use the notebooks following the order of the files 001, 002... and maybe the notebooks will need to be adapted dependin on your dataset.
- The notebooks generate the 3 datasets used by the chat bot: movie_lines_pre_processed_for_test.tvs, page_rank_questions.txt and page_rank_answers.txt. If retraining, get the generated files in notebooks/chatdata and put in src/chatdata.
- The model.h5 and the tokenizer.pickle are also generated by the notebooks and it is needed to copy both in src/chatdata.
- This chat bot was developed using 30000 messages due to performance issues, so pay attention to your dataset if you are retrainign the chat bot.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Mark the repository with a star if liked it.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## References
- Dataset https://www.kaggle.com/Cornell-University/movie-dialog-corpus?select=movie_lines.tsv
- https://shanebarker.com/blog/deep-learning-chatbot/
- https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44