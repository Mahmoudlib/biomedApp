from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_device_source_label_alter_device_source_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='image',
            field=models.CharField(blank=True, max_length=500, verbose_name="URL ou chemin de l'image"),
        ),
    ]
