# Generated by Django 3.2 on 2021-04-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Link', models.CharField(max_length=255)),
                ('Image', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contents',
            },
        ),
    ]
