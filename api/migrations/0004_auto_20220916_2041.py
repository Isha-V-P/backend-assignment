# Generated by Django 3.2.15 on 2022-09-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zip',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
