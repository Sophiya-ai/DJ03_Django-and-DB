from django.shortcuts import render, redirect
from .models import New_post  #импортируем класс
from .forms import New_postForm

# Create your views here.
def home(request):
    news = New_post.objects.all()   #Создаём переменную для получения всех записей
    return render(request,'NewApp/news.html', {'news' : news})  #Прописываем словарь для передачи информации в html-шаблон

def add_news(request):
    error = ''
    if request.method == 'POST':
        form = New_postForm(request.POST) #сохраняем всю информацию от пользователя
        if form.is_valid():
            form.save()
            return redirect('newshomepage')
        else:
            error = "Данные заполнены некорректно"
    form = New_postForm()
    return render(request, 'NewApp/add_news.html', {'form' : form, 'errors': error})