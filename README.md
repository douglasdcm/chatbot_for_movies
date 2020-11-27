# Overview (WORK IN PROGRESS)

The intention of this project is to create a chatbot based on movie reviews so that you can ask questions and have a free conversation about this topic.

## Motivation

Recently I had to buy a new internet service, so I tried to do it using the available chatbot of the company. I noticed the conversation with the chatbot was based on rules and conditions. Hence, for each question I was doing to the bot, it was sending to me a list of options I needed to choose to go to the next step of the conversation. The experience was not good for me and it did not solve my problem.
So, I started search for possible solutions, just for curiosity, and I found some contents in the internet talking about the training of a chatbot using Natural Language Processing (NLP). After this reading, I decided to take the challenge and train my on chatbot for natural conversations.

## How it will be done
1. Use a dataset with fictional conversations about movies
2. Process the data to build the sequence of conversations
3. Apply capitalization, lemmatization and stemming to reduce the variation of words
4. Enrich the dataset with more features (similarity of sentences)
5. Train each message with its corresponding answer using a Neural Network
6. Build a user interface to allow the interaction with the chatbot
7. Deploy the chatbot in a free and public domain (Heroku)

## The chatbot (draft)
### Used libraries
- pandas
- re
- keras
- nump
- sklearn
- Scipy
- train_test_split
- math

## Prototype
![alt text](https://i.ibb.co/X2LMpNx/chatbot-ui.png)

## Running the chatbot

```bash
pip3 install -r requirements.txt
python3 main.py
```


## References
- Dataset https://www.kaggle.com/Cornell-University/movie-dialog-corpus?select=movie_lines.tsv
- https://shanebarker.com/blog/deep-learning-chatbot/
- https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44
- https://gist.github.com/lilgreenland/948333054cdd82284670ed6058f0ab2a

 
=======
## The intention of the project is to create a chatbot based on movie reviews so that you can ask questions and have a free conversation on this topic.

- dataset https://www.kaggle.com/Cornell-University/movie-dialog-corpus?select=movie_lines.tsv
- References
>- https://shanebarker.com/blog/deep-learning-chatbot/
> -https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44
