from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_device_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='image_source_label',
            field=models.CharField(blank=True, max_length=255, verbose_name="Source de l'image"),
        ),
    ]
