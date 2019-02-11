from django.shortcuts import render

# Create your views here.

def error_404(request):
        return render(request,'homepage/error_404.html', status=404)

def error_500(request):
        return render(request,'homepage/error_500.html', status=500)

