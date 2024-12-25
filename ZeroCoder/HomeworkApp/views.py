from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wStatic(request):
    context = {
        'question': 'Настройка статических файлов в Django',
        'active_page': 'wStatic'
    }
    return render(request, 'HomeworkApp/workWithStatic.html', context)

def pros_cons(request):
    context = {
        'question': 'Прeимущества и недостатки Django',
        'active_page': 'pros'
    }
    return render(request, 'HomeworkApp/pros.html', context)

def projects(request):
    context = {
        'question': 'Django в картинках',
        'active_page': 'projects'
    }
    return render(request, 'HomeworkApp/projects.html', context)

def problems(request):
    context = {
        'question': 'Проблемы Django',
        'active_page': 'problems'
    }
    return render(request, 'HomeworkApp/problems.html', context)
