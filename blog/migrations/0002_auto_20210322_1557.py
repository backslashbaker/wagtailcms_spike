# Generated by Django 3.1.7 on 2021-03-22 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglistingpage',
            name='background_image',
            field=models.ForeignKey(blank=True, help_text='Header background image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
