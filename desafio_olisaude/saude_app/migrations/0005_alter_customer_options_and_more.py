# Generated by Django 4.1.1 on 2022-10-15 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("saude_app", "0004_auto_20221011_1435"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={"verbose_name": "Lista de Cliente"},
        ),
        migrations.AlterField(
            model_name="problemhearth",
            name="code_costumer",
            field=models.ForeignKey(
                default="0001",
                on_delete=django.db.models.deletion.CASCADE,
                to="saude_app.customer",
                verbose_name="Nome do Cliente",
            ),
        ),
        migrations.AlterField(
            model_name="problemhearth",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
