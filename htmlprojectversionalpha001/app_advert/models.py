from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()


class Advertisment(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auction = models.BooleanField('торг', help_text='Отметьте, если уместен торг')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='htmlprojectversionalpha001/')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title}, price={self.price})'

    @admin.display(description='Изображение')
    def imaged(self):
        if self.image:
            print(self.image)
            return format_html('<img src="{url}" style="max-width: 80px; max-height: 80;">', url=self.image.url)
    @admin.display(description='Дата создания')
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.create_at.strftime('%d.%m.%y')
    @admin.display(description='Дата обновления')
    def updated_date(self):
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.update_at.strftime('%d.%m.%y')
# Create your models here.
    class Meta:
        db_table = 'advertisements'