# Generated by Django 4.2 on 2023-04-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('trainer', models.CharField(max_length=200)),
                ('teammates', models.ManyToManyField(to='app.players')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nb_pool', models.IntegerField()),
                ('team_per_pools', models.IntegerField()),
                ('place', models.CharField(blank=True, max_length=100)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('teams', models.ManyToManyField(to='app.team')),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb', models.IntegerField()),
                ('tournament', models.CharField(max_length=100)),
                ('teams', models.ManyToManyField(to='app.team')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('pool', models.PositiveIntegerField()),
                ('teams', models.ManyToManyField(to='app.team')),
            ],
        ),
    ]