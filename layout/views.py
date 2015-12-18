from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def features(request):
    return render(request, 'features.html', {})


def project_insight(request):
    return render(request, 'project_insight.html', {})
