# Generated by Django 3.2.5 on 2022-01-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0012_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
