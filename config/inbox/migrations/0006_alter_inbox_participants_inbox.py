# Generated by Django 4.0.4 on 2022-05-28 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0005_alter_inbox_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox_participants',
            name='inbox',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inbox.inbox'),
        ),
    ]
