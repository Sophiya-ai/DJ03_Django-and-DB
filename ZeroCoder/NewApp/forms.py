from .models import New_post
from django.forms import ModelForm, TextInput,Textarea, DateTimeInput

class New_postForm(ModelForm):
    class Meta:
        model = New_post
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title' : TextInput(attrs={'class' : "form-control", 'placeholder':"Введите заголовок новости"}),
            'short_description' : TextInput(attrs={'class' : "form-control", 'placeholder':"Введите краткое описание новости"}),
            'text' : Textarea(attrs={'class' : "form-control", 'placeholder':"Введите текст новости"}),
            'pub_date' : DateTimeInput(attrs={'class' : "form-control", 'placeholder':"Дата публикации"}),
        }