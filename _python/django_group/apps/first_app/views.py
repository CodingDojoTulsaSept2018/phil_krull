from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'first_app/index.html')
def showAll(request):
    return render(request,'first_app/all.html')
def showOne(request):
    return render(request,'first_app/one.html', user_id = user_id)
def editUser(request):
    return render(request, 'first_app/edit.html', user_name = user_name)