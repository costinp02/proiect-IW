# Generated by Django 4.1.7 on 2023-03-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cnp',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
