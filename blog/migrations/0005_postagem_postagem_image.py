# Generated by Django 4.1.1 on 2022-09-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_postagem_postagem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='postagem_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
