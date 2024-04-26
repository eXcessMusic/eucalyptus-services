# Generated by Django 5.0.4 on 2024-04-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('artwork', models.ImageField(upload_to='events/<str:id>/')),
                ('url', models.URLField()),
                ('location', models.CharField(max_length=150)),
            ],
        ),
    ]