import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "I":"you",
    "I am":"you are",
    "I was":"You were",
    "I'm":"You are",
    "I'd":"you would",
    "I've":"you have",
    "I'll":"you will",
    "my":"Your",
    "You are":"I am",
    "You were":"I was",
    "You've":"I have",
    "You'll":"I will",
    "Your":"my",
    "Yours":"mine",
    "You":"me",
    "me":"you"
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"Hi|Hey|Hello",
        ["Hello", "Hey there",]
    ],
    [
        r"What is your name?",
        ["I am a bot created by Codingal Edu. pvt. lim. You can call me Jarvis",]
    ],
    [
        r"How are you?",
        ["I'm doing goodnHow aboout you?"]
    ],
    [
        r"Sorry(.*)",
        ["It's alright", "It's Ok", "No worries",]
    ],
    [

r"I am fine",

["Great to hear that, How can I help you?",]

],

[

r"i'm (.*) doing good",

["Nice to hear that","How can I help you?:)",]

],

[

r"(.*) age?",

["I'm a computer program dudenSeriously you are asking me this?",]

],

[

r"what (.*) want ?",

["Make me an offer I can't refuse",]

],

[

r"(.*) created ?",

["Shravan created me using Python's NLTK library ","top secret ;)",]

],

[

r"(.*) (location|city) ?",

['Bangalore, Karnataka',]

],

[

r"how is weather in (.*)?",

["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]

],

[

r"i work in (.*)?",

["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]

],

[

r"(.*)raining in (.*)",

["No rain since last week here in %2","Damn its raining too much here in %2"]

],

[

r"how (.*) health(.*)",

["I'm a computer program, so I'm always healthy ",]

],

[

r"(.*) (sports|game) ?",

["I'm a very big fan of Football and Cricket",]

],

[

r"who (.*) sportsperson ?",

["Messy","Ronaldo","Roony", "Virat", "M.S. Dhoni", "Rohit"]

],

[

r"who (.*) (moviestar|actor)?",

["Benedict Cumberbatch"]

],

[

r"i am looking for online guides and courses to learn data science, can you suggest?",

["Jarvis_Tech has many great articles with each step explanation along with code, you can explore"]

],

[

r"quit",

["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]

],

]

def chat(): 
    print("Hi! I am a cahtbot made by Codingal Edu. Pvt. Lim. for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__": 
    chat()