import nltk
import random
import string
import warnings

warnings.filterwarnings('ignore')

f = open("C:\\Users\\khaja_3ut2btu\\Downloads\\chatbotdataset.txt",'r', errors='ignore')
rawd = f.read()
rawd = rawd.lower()

sent_tok = nltk.sent_tokenize(rawd)
word_tok = nltk.word_tokenize(rawd)

sentToken = sent_tok[:4]

wordToken = word_tok[:4]



lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "nods", "hi there", "hello", "I am glad! you are talking to me"]
h_input=("how are you", "how are you feeling", "how are you doing", "are you doing good", "are you fine")
h_output=["yeah,i am fine, tell me about yourself", "im doing good", "i am fine", "im good"]


def greeting(sent):
    for word in sent.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)




from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def resp(user_resp):
    chatbot_resp = ''
    sent_tok.append(user_resp)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
    tfidf = TfidfVec.fit_transform(sent_tok)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        chatbot_resp = chatbot_resp + "I am sorry! I don't understand you"
        return chatbot_resp

    else:
        chatbot_resp = chatbot_resp + sent_tok[idx]
        return chatbot_resp


if __name__ == "__main__":
    flag = True
    print("Hello, there my name is csebot. I will answer your queries. If you want to exit, type Bye!")
    while (flag == True):
        user_resp = input()
        user_resp = user_resp.lower()
        if (user_resp != 'bye'):
            if user_resp == 'thanks' or user_resp == 'thank you':
                flag = False
                print("csebot: You're welcome!")
            else:
                if (greeting(user_resp) != None):
                    print("csebot:" + greeting(user_resp))
                else:
                    print("csebot:", end='')
                    print(resp(user_resp))
                    sent_tok.remove(user_resp)
        else:
            flag = False
            print("csebot: Bye! Have a great time!")
