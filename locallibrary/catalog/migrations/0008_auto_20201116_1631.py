# Generated by Django 3.1.2 on 2020-11-16 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
