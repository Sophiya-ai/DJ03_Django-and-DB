from django.urls import path
from . import views
# . импорт из той папки, в которой находимся


urlpatterns = [
    path('workWithStatic/',views.wStatic, name='wStatic'),
    path('pros/', views.pros_cons, name='pros'),
    path('projects/', views.projects, name='projects'),
    path('problems/', views.problems, name='problems'),
]