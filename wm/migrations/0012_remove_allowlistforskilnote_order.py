# Generated by Django 3.2.8 on 2022-01-15 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wm', '0011_allowlistforskilnote_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allowlistforskilnote',
            name='order',
        ),
    ]
