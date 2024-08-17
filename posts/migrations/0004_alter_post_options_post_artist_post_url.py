# Generated by Django 5.0.6 on 2024-08-16 01:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="post",
            name="artist",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="url",
            field=models.URLField(max_length=500, null=True),
        ),
    ]