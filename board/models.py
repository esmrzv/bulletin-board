from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    price = models.DecimalField(max_digits=10, verbose_name='цена', decimal_places=2)
    description = models.TextField(verbose_name='описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор объявления')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Feedback(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор отзыва')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.text} - {self.author}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
