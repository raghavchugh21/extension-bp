import _pickle as pickle
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import sys

def predict(headline):
    try:
        f = open('trainedmodel','rb')
        clf = pickle.load(f)
        f = open('vectorizer','rb')
        vectorizer = pickle.load(f)
        return clf.predict_proba(vectorizer.transform(headline))[0][1]
    except IOError:
        print("Model not present, run train.py first")


if __name__ == "__main__":
    x=int(predict([sys.argv[1]])*100)
    print (str(x))
    if(x>70):
        print("Clickbait")
    else:
        print("Not Clickbait")