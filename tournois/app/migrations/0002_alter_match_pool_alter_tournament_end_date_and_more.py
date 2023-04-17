# Generated by Django 4.2 on 2023-04-17 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pool'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
