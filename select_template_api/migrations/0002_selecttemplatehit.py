# Generated by Django 2.2.1 on 2019-05-09 14:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('select_template_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectTemplateHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('task_uuid', models.UUIDField(editable=False)),
                ('query_id', models.CharField(max_length=50)),
                ('query_sequence', models.CharField(max_length=2000)),
                ('query_range', models.CharField(max_length=100)),
                ('funfam_id', models.CharField(max_length=100)),
                ('funfam_name', models.CharField(max_length=500)),
                ('pdb_id', models.CharField(max_length=4)),
                ('auth_asym_id', models.CharField(max_length=4)),
                ('template_sequence', models.CharField(max_length=2000)),
                ('template_seqres_offset', models.IntegerField(default=0)),
            ],
        ),
    ]
