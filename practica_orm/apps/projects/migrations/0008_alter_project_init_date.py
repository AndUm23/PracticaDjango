# Generated by Django 4.2.11 on 2024-04-14 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_alter_project_init_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="init_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]