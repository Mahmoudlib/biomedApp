from django.db import migrations, models
from django.utils.text import slugify


def populate_device_slugs(apps, schema_editor):
    Device = apps.get_model('core', 'Device')
    seen = set()

    for device in Device.objects.all().order_by('pk'):
        base_slug = slugify(device.name) or f"device-{device.pk}"
        slug = base_slug
        counter = 2
        while slug in seen or Device.objects.exclude(pk=device.pk).filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        device.slug = slug
        device.save(update_fields=['slug'])
        seen.add(slug)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_device_image_source_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name="Identifiant d'URL"),
        ),
        migrations.RunPython(populate_device_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='device',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name="Identifiant d'URL"),
        ),
    ]
