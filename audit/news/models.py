from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=100)
    date = models.DateField('Дата')
    text = models.TextField('Новость')

    def __str__(self):
        return self.title