# Generated by Django 2.2.1 on 2019-06-07 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_template_api', '0008_auto_20190606_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='selecttemplatealignment',
            name='target_sequence',
            field=models.CharField(default=None, max_length=2000),
            preserve_default=False,
        ),
    ]
