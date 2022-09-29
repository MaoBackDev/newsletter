# Generated by Django 3.2.6 on 2022-09-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='newsletter',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default=1, max_length=12),
            preserve_default=False,
        ),
    ]
