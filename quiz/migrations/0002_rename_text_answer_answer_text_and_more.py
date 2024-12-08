# Generated by Django 5.0.7 on 2024-12-07 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='text',
            new_name='answer_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='description',
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]