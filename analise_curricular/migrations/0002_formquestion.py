# Generated by Django 5.1.3 on 2025-07-20 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analise_curricular', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('question_type', models.CharField(choices=[('text', 'Texto'), ('number', 'Número'), ('select', 'Seleção'), ('checkbox', 'Checkbox'), ('radio', 'Rádio')], max_length=20)),
                ('order', models.PositiveIntegerField(default=0)),
                ('required', models.BooleanField(default=True)),
                ('options', models.JSONField(blank=True, null=True)),
                ('conditions', models.JSONField(blank=True, null=True)),
                ('selecao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='analise_curricular.selecao')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
