# Generated by Django 3.1.6 on 2022-02-23 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_remove_review_new_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
