from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')  # Or return HttpResponse("Hello!")
