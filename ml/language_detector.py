
import numpy as np
from sklearn.datasets import load_files


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC

from sklearn.metrics import confusion_matrix
from pandas import DataFrame

import gzip
import dill


try:
    dataset = load_files('./wikidata/short_paragraphs')
except OSError as ex:
    print(ex)
    print("Couldn't import the data, did you unzip the wikidata.zip folder?")
    exit(-1)


docs = dataset['data']
target = dataset['target']


docs_train, docs_test, y_train, y_test = train_test_split(docs, target, test_size=.2, random_state=0)


vec = TfidfVectorizer(ngram_range=(1, 5), analyzer='char', use_idf=True)

vec.decode(docs_train)




mlp = MLPClassifier()

model = make_pipeline(vec, mlp)

model.fit(docs_train, y_train)

y_predicted = model.predict(docs_test)



target_names = [dataset.target_names[i] for i in np.unique(y_train)]
print(classification_report(y_test, y_predicted, target_names=target_names))



cm = confusion_matrix(y_test, y_predicted)
predicted_names = ['p_' + s for s in target_names]
dfcm = DataFrame(cm, columns=predicted_names, index=target_names)
print(dfcm)

# TASK: Is the score good? Can you improve it changing
#       the parameters or the classifier?
#       Try using cross validation and grid search

# from sklearn.model_selection import cross_validate, GridSearchCV
# cv = cross_validate(mlp, docs, target, n_jobs=-1)



# TASK: Use dill and gzip to persist the trained model in memory.
#       1) gzip.open a file called my_model.dill.gz
#       2) dump to the file both your trained classifier
#          and the target_names of the dataset (for later use)
#    They should be passed as a list [model, dataset.target_names]

with gzip.open('my_model.dill.gz', 'wb') as f:
    dill.dump([model, dataset.target_names], f)
