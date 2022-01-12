from django.shortcuts import render

def index(request):
    title = 'Главная'

    context = {
        'title': title,
    }

    return render(request, 'mainapp/base.html', context=context)