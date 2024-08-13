# Generated by Django 5.0.7 on 2024-08-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_alter_users_address_alter_users_name_alter_users_pol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='pol',
            field=models.CharField(choices=[('', ''), ('man', 'Мужской'), ('woman', 'Женский')], max_length=255, verbose_name=''),
        ),
    ]