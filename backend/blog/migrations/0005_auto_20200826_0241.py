# Generated by Django 3.1 on 2020-08-26 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.CharField(choices=[('education', 'education'), ('lifestyle', 'lifestyle'), ('programming', 'programming'), ('music', 'music')], default='general', max_length=255),
        ),
    ]
