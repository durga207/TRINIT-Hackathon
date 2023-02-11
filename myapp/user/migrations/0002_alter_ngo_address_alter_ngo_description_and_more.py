# Generated by Django 4.1.6 on 2023-02-11 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='primary_cause',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='trust_score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='website_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
