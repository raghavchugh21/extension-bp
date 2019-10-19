from sklearn.feature_extraction.text import TfidfVectorizer
import _pickle as pickle
from sklearn import metrics
from sklearn import svm
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

print ("\nLoading dataset\n")
vectorizer = TfidfVectorizer()


titles = {
    "0":[],
    "1":[]
}
with open ('ClickbaitDataset.txt',encoding='utf8') as f:
    titles["1"] = f.read().splitlines()
with open ('NonClickbaitDataset.txt',encoding='utf8') as f:
    titles["0"] = f.read().splitlines()
print("\nDataset Loaded, Preprocessing Data")
train_labels = [0]*len(titles["0"]) + [1]*len(titles["1"])
train_set = titles["0"] + titles["1"]
#train_set, train_labels, validation_set, validation_labels = train_test_split(train_set, train_labels, test_size=0.20)
print("Train size: " + str(len(train_labels)))
#print("Validation size: " + str(len(validation_labels)))

train_set = vectorizer.fit_transform(train_set, train_labels)
print("\nData proprocessed!")
#validation_set = vectorizer.transform(validation_set)
print  ("\nTrain matrix shape: " + str(train_set.shape))
params = {'kernel': 'rbf', 'C': 2, 'gamma': 1}
clf = svm.SVC(C=params['C'], kernel=params['kernel'], gamma=params['gamma'], probability=True)
# print("Evaluating parameters\n")
# re_fit_model = True
# with open("vectorizer", 'wb') as f:
#     pickle.dump(vectorizer, f)
# gsc = GridSearchCV(
#         estimator=SVR(kernel='rbf'),
#         param_grid={
#             'C': [0.1, 1, 100, 1000],
#             'epsilon': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10],
#             'gamma': [0.0001, 0.001, 0.005, 0.1, 1, 3, 5]
#         },
#         cv=5, scoring='neg_mean_squared_error', verbose=0, n_jobs=-1)
# grid_result = gsc.fit(train_set, train_labels)
# best_params = grid_result.best_params_
# print("The parameters are\n")
# print(best_params)
# clf = svm.SVC(C=best_params['C'], kernel=best_params['kernel'], gamma=best_params['gamma'], probability=True)
# print("now training model")
print("Fitting Model")
clf.fit(train_set, train_labels)
with open("trainedmodel", 'wb') as f:
    pickle.dump(clf, f)
print("Model Created")  
with open('trainedmodel','rb') as f:
    clf=pickle.load(f)
print("Making predictions")
predictions = clf.predict(train_set)
print ("\nTrain set")
print ("\nAccuracy Score: " + str(metrics.accuracy_score(predictions, train_labels)))
print ("F1 Score: " + str(metrics.f1_score(predictions, train_labels)))
print ("Recall: " + str(metrics.recall_score(predictions, train_labels)))
print ("Precision: " + str(metrics.precision_score(predictions, train_labels)))