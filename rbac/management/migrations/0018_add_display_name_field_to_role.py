# Generated by Django 2.2.4 on 2020-07-14 17:48

from django.db import migrations, models


def update_display_name(apps, schema_editor):
    # get role model
    Role = apps.get_model("management", "Role")

    # iterate through all Access
    for role in Role.objects.all():
        # get the permission context from the permission
        role.display_name = role.name
        role.save()


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0017_auto_20200717_1842"),
    ]

    operations = [
        migrations.AddField(
            model_name="role", name="display_name", field=models.CharField(default="", max_length=150, unique=True),
        ),
        migrations.RunPython(update_display_name),
    ]
