# Generated by Django 3.0.5 on 2020-05-13 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("trading_bot", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="simulation",
            old_name="end_amount_eur_average",
            new_name="end_amount_quote_average",
        ),
        migrations.RenameField(
            model_name="simulation",
            old_name="start_amount_eur",
            new_name="start_amount_quote",
        ),
    ]
