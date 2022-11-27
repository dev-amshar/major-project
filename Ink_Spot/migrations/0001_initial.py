# Generated by Django 4.1.2 on 2022-10-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('discount', models.CharField(max_length=10)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='Uploads\\product')),
            ],
        ),
    ]
