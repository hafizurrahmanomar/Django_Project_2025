from django.shortcuts import render

def contact(request):
    info=[
        
            "name:Bongo DevOps",
            "phone: 0712345678",
            "email:example@gmail.com",
            "address: 123 Main Street, Nairobi, Kenya",
    ]
    email="bongodevops@gmail.com"
    return render(request, 'contact.html',{'info':info, 'email':email})
