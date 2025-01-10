from django.urls import path
from . import views
# . импорт из той папки, в которой находимся


urlpatterns = [
    path('',views.home, name='newshomepage'),
    path('add_news',views.add_news, name='add_news'),
]