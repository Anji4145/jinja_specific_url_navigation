from django.shortcuts import render

# Create your views here.
def anime_list(request):
    return render(request,'anime_list.html')