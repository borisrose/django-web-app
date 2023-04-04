# Generated by Django 4.1.2 on 2022-10-30 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_group_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='name',
        ),
        migrations.AddField(
            model_name='seller',
            name='address',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='email',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='firstname',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]