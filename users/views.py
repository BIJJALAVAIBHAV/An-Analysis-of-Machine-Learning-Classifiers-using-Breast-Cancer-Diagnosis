from django.shortcuts import render, HttpResponse
from .forms import DiagnosisUserRegistrationForm
from django.contrib import messages
from .models import DiagnosisUserRegistrationModel
from django.conf import settings
from .AlgorithmCode import MyAlgorithms
# Create your views here.
import matplotlib.pylab as plt

def UserRegisterActions(request):
    if request.method == 'POST':
        form = DiagnosisUserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            # return HttpResponseRedirect('./CustLogin')
            form = DiagnosisUserRegistrationForm()
            return render(request, 'DiagnosisRegister.html', {'form': form})
        else:
            print("Invalid form")
    else:
        form = DiagnosisUserRegistrationForm()
    return render(request, 'DiagnosisRegister.html', {'form': form})

def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = DiagnosisUserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})

def UserHome(request):
    return render(request, 'users/UserHome.html', {})


def UserDatapreprocess(request):
    path = settings.MEDIA_ROOT + "\\" + 'data.csv'
    obj = MyAlgorithms()
    html = obj.startPreprocess(path=path)
    # obj.MlpTest(path=path)
    # obj.DeepNeuralNetwork(path=path)
    return render(request,'users/PreProcessedData.html',{'data':html})

def UserClassificationReports(request):
    path = settings.MEDIA_ROOT + "\\" + 'data.csv'
    obj = MyAlgorithms()
    myDict = obj.modelExecutions(path=path)

    return render(request,"users/ClassificationReport.html",{'myDict':myDict})


def UserNeuralNetworks(request):
    path = settings.MEDIA_ROOT + "\\" + 'data.csv'
    obj = MyAlgorithms()
    dict_perc = obj.MlpTest(path=path)
    dict_dnn = obj.DeepNeuralNetwork(path=path)
    dict_perc.update(dict_dnn)
    print("FInal Result ", dict_perc)
    return render(request,"users/DNNReport.html",{'myDict':dict_perc})