# Generated by Django 4.2.2 on 2023-06-18 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roxy', '0010_alter_card_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='comments_no',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]