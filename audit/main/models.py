from django.db import models

class Application(models.Model):
    name = models.CharField('ФИО', max_length=100)
    company_name = models.CharField('Название компании', max_length=100)
    email = models.EmailField('Электронная почта', max_length=100)
    phone = models.CharField('Номер телефона', max_length=20)
    service_type = models.CharField('Тип услуги', max_length=50)
    comment = models.TextField('Комментарий', blank=True)

    def __str__(self):
        return self.name
