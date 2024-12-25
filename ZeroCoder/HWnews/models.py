from django.db import models

# Create your models here.
class post_news(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    writer = models.CharField('Имя пользователя', max_length=50)
#Класс CharField помогает создавать поля, в которых можно записать не более 250 символов.
# Мы прописали структуру базы данных, то есть что в ней будет. В проекте описанная таблица пока не существует.
# Чтобы она начала существовать, нам нужны миграции. Миграции создают связь между базой данных
# и между приложением, соединяет их


    #прописываем специальный метод внутри класса, чтобы на сайте отображалось название новости
    def __str__(self):
        return self.title

    #чтобы таблица в админ-панели отображалась на русском, создаём вложенный класс
    class Meta:
        verbose_name = 'Домашняя новость'
        verbose_name_plural = 'Домашние новости'