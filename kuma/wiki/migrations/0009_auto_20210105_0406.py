# Generated by Django 2.2.16 on 2021-01-05 04:06

from django.db import migrations


def forward(apps, schema_editor):
    Switch = apps.get_model("waffle", "Switch")
    Switch.objects.filter(
        name__in=[
            "foundation_callout",
            "helpful-survey-2",
            "registration_disabled",
            "store_revision_ips",
            "wiki_spam_training",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("wiki", "0008_auto_20210104_1139"),
    ]

    operations = [migrations.RunPython(forward)]
