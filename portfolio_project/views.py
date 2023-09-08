from django.shortcuts import render, redirect
from portfolioApp.forms import UserInfoForm
from portfolioApp.models import FormModel

def home(request):
    if request.method == "POST":
        print(request.POST)
        form = UserInfoForm(request.POST)
        if form.is_valid():
            data = FormModel()
            data.name = request.POST['name']
            data.Email = request.POST['Email']
            data.subject = request.POST['subject']
            data.message = request.POST['message']
            data.save()
            return redirect('home')

    form = UserInfoForm()
    context = {
        'form':form
    }
    return render(request, 'index.html', context=context)