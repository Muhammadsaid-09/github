from django.db import models

class Users(models.Model):
    POL=(
        ('',''),
        ('Мужской','Мужской'),
        ('Женский','Женский'),
    )

    objects = None
    name=models.CharField("",max_length=255)
    surname=models.CharField('',max_length=255)
    address=models.CharField("",max_length=255)
    pol=models.CharField("",max_length=255,choices=POL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
