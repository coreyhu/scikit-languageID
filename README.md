# Language detector exercise

Hosted on [Heroku](https://language-detector.herokuapp.com/).

Uses [custom buildbpack](https://github.com/thenovices/heroku-buildpack-scipy) for scipy dependency.

This is a simple Flask app that will predict the language of a sentence using sci-kit Learn.

## Steps

1) Create a new virtual environment and install requirements:

```
virtualenv dwheroku
source ./dwheroku/bin/activate
pip install -r requirements.txt
```

2) Open the ml folder. It contains 2 files and 1 folder:
- language_detector_test.py
- language_detector.py
- paragraphs

3) Inspect the content of the paragraphs folder. That's our starting data
You'll have to figure out a way to extract features from the text

4) try running "python language_detector_test.py" and see that it's not working: no saved model is present. You will need to build a model and save it.

5) Open the "language_detector.py" file. This is where most of the work will be. Complete each task in sequence untill you get a satisfactory value for the test score.

6) Once you have a saved model, run again "python language_detector_test.py" and see that it detects the language of the sentences. You can also try to give your own sentence by running "python language_detector_test.py 'insert here whatever sentence you want' "

7) It's now time to run our server locally. Run "python controller.py", it will load the model and start a web-server.

8) Visit http://127.0.0.1:5000/ with your browser and test that you can submit a sentence in any language. If your model is well trained it should tell you the language of the sentence

9) Explore the "controller.py" file. Can you figure out what it does?

10) Explore the rest of the code. Can you figure out what the other files do?

11) Deploy to Heroku! (requires heroku install & signup)

```
git init
heroku create
git add .
git commit -m "initial commit"
git push heroku master
```
