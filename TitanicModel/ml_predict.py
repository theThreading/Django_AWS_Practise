def MakePrediction(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle;
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]];
    randomforest = pickle.load(open('titanic_model.sav','rb'));
    predictions = randomforest.predict(x);

    return predictions;
