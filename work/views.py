from django.shortcuts import render
from work.form import todoForm

# Create your views here.
def home(request):
    form=todoForm()
    return render(request,"home.html",{'form':form})
    
