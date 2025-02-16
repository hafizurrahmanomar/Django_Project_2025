from django.shortcuts import render

# Create your views here.

def about(request):
    context={
         "Name":"Hafizur Rahman",
         "title":"I am a DevOps Engineer"
    }   
   
    return render(request, 'about.html',context)
