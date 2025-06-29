# Generated by Django 5.2.3 on 2025-06-16 05:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name_membership', models.CharField(max_length=50)),
                ('price_membership', models.IntegerField()),
                ('offers_membership', models.IntegerField(null=True)),
                ('membership_duration', models.IntegerField()),
            ],
        ),
    ]
