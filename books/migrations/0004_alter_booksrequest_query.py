# Generated by Django 3.2.8 on 2021-11-10 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_booksrequest_fault'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksrequest',
            name='query',
            field=models.CharField(max_length=100),
        ),
    ]