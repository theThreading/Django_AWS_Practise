from django.shortcuts import render
from . import ml_predict
def home(request):
    return render(request,'index.html');
#def MakePrediction(pclass,sex,age,sibsp,parch,fare,embarked,title):
#   <p>Pclass</p>
# <input type="text" name="Pclass">
# <p>Sex</p>
# <input type="text" name="Sex">
# <p>Age</p>
# <input type="text" name="Age">
# <p>Sibsp</p>
# <input type="text" name="Sibsp">
# <p>Parents/Children</p>
# <input type="text" name="Parch">
# <p>Fare</p>
# <input type="text" name="Fare">
# <p>Embarked</p>
# <input type="text" name="Embarked">
# <p>Title</p>
# <input type="text" name="Title">
def results(request):
    Pclass = int(request.GET['Pclass']);
    Sex = int(request.GET['Sex']);
    Age = int(request.GET['Age']);
    Sibsp = int(request.GET['Sibsp']);
    Parch = int(request.GET['Parch']);
    Fare = float(request.GET['Fare']);
    Embarked = int(request.GET['Embarked']);
    Title = int(request.GET['Title']);
    prediction = ml_predict.MakePrediction(Pclass,Sex,Age,Sibsp,Parch,Fare,Embarked,Title);
    Result_message = "";
    if prediction == 1:
        Result_message += "This passenger survived";
    else:
        Result_message += "This passenger perished";

    return render(request,'results.html',{'ResultMessage':Result_message});
