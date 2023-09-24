from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=200,
    )
    price: float = models.DecimalField(
        verbose_name='цена',
        max_digits=11,
        decimal_places=2,
    )
    class Meta:
        ordering = ('-id',)
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'