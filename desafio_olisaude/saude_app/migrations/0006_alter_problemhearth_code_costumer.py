# Generated by Django 4.1.1 on 2022-10-15 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("saude_app", "0005_alter_customer_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problemhearth",
            name="code_costumer",
            field=models.ForeignKey(
                default="Select",
                on_delete=django.db.models.deletion.CASCADE,
                to="saude_app.customer",
                verbose_name="Nome do Cliente",
            ),
        ),
    ]