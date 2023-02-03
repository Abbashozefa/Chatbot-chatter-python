from flask import Flask,render_template,request


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time

chatbot=ChatBot('ChatGPT')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus","chatterbot.corpus.english","chatterbot.corpus.english.movies","chatterbot.corpus.english.food","chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )
app=Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get",methods=['POST','GET'])
def webhook():
    
    msg=request.form['msg']
    response = chatbot.get_response(msg)
    return str(response)
    
    
    





if __name__  == "__main__":
    app.run(debug=True)