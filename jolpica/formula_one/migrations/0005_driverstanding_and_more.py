# Generated by Django 4.2.8 on 2024-01-21 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("formula_one", "0004_rename_championshipscheme_championshipsystem_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DriverStanding",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("year", models.SmallIntegerField()),
                ("round", models.PositiveSmallIntegerField()),
                ("position", models.SmallIntegerField()),
                ("points", models.FloatField()),
                ("win_count", models.SmallIntegerField()),
                ("highest_finish", models.SmallIntegerField()),
                ("finish_string", models.CharField(max_length=255)),
                ("is_disqualified", models.BooleanField(default=False)),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="driver_standings",
                        to="formula_one.driver",
                    ),
                ),
                (
                    "race",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="driver_standings",
                        to="formula_one.race",
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="driver_standings",
                        to="formula_one.season",
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="driver_standings",
                        to="formula_one.session",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="driverstanding",
            constraint=models.UniqueConstraint(
                fields=("session", "driver"),
                name="driver_standing_unique_session_driver",
            ),
        ),
    ]
