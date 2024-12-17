from .models import Application
from django.forms import ModelForm, TextInput, Select

class Application_form(ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'company_name', 'email', 'phone', 'service_type', 'comment']

        widgets = {
            "name": TextInput(attrs={
                'class': 'da',
                'placeholder': 'ФИО'
            }),
            "company_name": TextInput(attrs={
                'class': 'da',
                'placeholder': 'Название компании'
            }),
            "email": TextInput(attrs={
                'class': 'da',
                'placeholder': 'Электронная почта'
            }),
            "phone": TextInput(attrs={
                'class': 'da',
                'placeholder': 'Номер телефона'
            }),
            "service_type": Select(attrs={
                'class': 'da',
            }, choices=[
                ("", "Тип услуги"),
                ("Финансовый Аудит", "Финансовый Аудит"),
                ("Бухгалтерский учет", "Бухгалтерский учет"),
                ("Консалтинг по налоговым вопросам", "Консалтинг по налоговым вопросам"),
                ("Анализ финансовых показателей", "Анализ финансовых показателей"),
                ("Поддержка в разработке бизнес-плана", "Поддержка в разработке бизнес-плана"),
            ]),
            "comment": TextInput(attrs={
                'class': 'da',
                'placeholder': 'Комментарий'
            }),
        }