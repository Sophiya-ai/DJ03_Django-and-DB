from django.shortcuts import render
from .models import New_post  #импортируем класс

# Create your views here.
def home(request):
    news = New_post.objects.all()   #Создаём переменную для получения всех записей
    return render(request,'NewApp/news.html', {'news' : news})  #Прописываем словарь для передачи информации в html-шаблон