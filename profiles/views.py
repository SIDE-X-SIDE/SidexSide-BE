from django.shortcuts import render

# Create your views here.
def create_profile(request):
    return render(request, 'profiles/index.html')

