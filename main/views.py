from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306209441',
        'name': 'Farrel Ahmad Ilyasa',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)