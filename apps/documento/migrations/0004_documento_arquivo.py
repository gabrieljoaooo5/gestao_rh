# Generated by Django 3.2.9 on 2021-11-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0003_alter_documento_pertence'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documento'),
            preserve_default=False,
        ),
    ]
