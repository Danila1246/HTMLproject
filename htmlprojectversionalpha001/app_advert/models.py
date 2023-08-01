from django.db import models

class Advertisment(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auction = models.BooleanField('торг', help_text='Отметьте, если уместен торг')

# Create your models here.
