# Generated by Django 4.0.5 on 2022-07-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_alter_personal_info_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='section',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
    ]
