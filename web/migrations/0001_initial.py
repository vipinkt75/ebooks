# Generated by Django 4.2.1 on 2023-05-20 08:58

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='filtter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='filtter')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('tittle', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('ClassName', models.CharField(choices=[('malayalam', 'malayalam'), ('english', 'english'), ('hindi', 'hindi')], max_length=50, verbose_name='category')),
            ],
        ),
    ]