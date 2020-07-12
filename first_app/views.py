from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from . import forms

# Create your views here.

def index(request) :
    # my_dict = {'text' : "oh yeah i am inserted"}
    web_list = AccessRecord.objects.order_by('date')

    web_dict = { 'accessrecord' : web_list }

    return render(request,'first_app/index.html',context=web_dict) 

def form_name_view(request) :
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Success!")
            print("Name: " + form.cleaned_data['name'])


    return render(request,'first_app/form_page.html',{'form': form})   
