# Generated by Django 4.1.1 on 2022-10-07 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_tarea_usuario_delete_peliculas_delete_usuarios_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='incio',
            new_name='inicio',
        ),
    ]
