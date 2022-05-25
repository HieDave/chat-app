# Generated by Django 4.0.4 on 2022-05-25 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
        ('inbox', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='last_message',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='inboxes', to='message.message'),
        ),
    ]
