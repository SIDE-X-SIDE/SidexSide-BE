from django.shortcuts import render

# Create your views here.
def view_index(request):
    print(request.user)
    return render(request, 'profiles/index.html')

