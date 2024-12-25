from django.shortcuts import render
from .models import post_news  #импортируем класс

# Create your views here.
def home(request):
    #return render(request,'HWnews/news.html')
    news = post_news.objects.all()   #Создаём переменную для получения всех записей
    return render(request,'HWnews/news.html', {'news' : news})  #Прописываем словарь для передачи информации в html-шаблон