import sys
import os
import time
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC,SVC
from sklearn.metrics import classification_report
from sklearn.externals import joblib
classifier = "stored.pkl"

class classsify(object):
    def __init__(self):
        pass

class svmmodel(classsify):
    def train(self,manual=False):
        # if manual==False:
            try:
                self.clf = joblib.load(classifier)
            except:
                # clf = Pipeline([("tfidf", TfidfVectorizer(sublinear_tf=True)),("svc", LinearSVC())])
                # clf = Pipeline([("tfidf", TfidfVectorizer(sublinear_tf=True)),("svc", SVC(kernel='linear', probability=True))])
                data_dir="review_polarity/txt_sentoken"
                classes = ['pos', 'neg']
                train_data = []
                train_labels = []
                test_data = []
                test_labels = []
                for curr_class in classes:
                    dirname = os.path.join(data_dir, curr_class)
                    for fname in os.listdir(dirname):
                        with open(os.path.join(dirname, fname), 'r') as f:
                            content = f.read()
                            if fname.startswith('cv9'):
                                test_data.append(content)
                                test_labels.append(curr_class)
                            else:
                                train_data.append(content)
                                train_labels.append(curr_class)
                # clf = Pipeline([("tfidf", TfidfVectorizer(sublinear_tf=True)),("svc", LinearSVC(C=1.0))])
                self.clf = Pipeline([("tfidf", TfidfVectorizer(sublinear_tf=True)),("svc", SVC(kernel='linear', probability=True))])
                self.clf.fit(train_data, train_labels)
                pred = self.clf.predict(test_data)
                print(classification_report(test_labels, pred))
                joblib.dump(self.clf,"stored.pkl")
    def predict(self,test):
                return (self.clf.predict(test),self.clf.predict_proba(test)[0])
trainedclf=svmmodel()
trainedclf.train()
# print trainedclf.predict(["It was good"]) 
