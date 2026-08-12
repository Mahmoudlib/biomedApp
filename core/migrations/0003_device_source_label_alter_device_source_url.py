from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_company_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='source_url',
            field=models.URLField(blank=True, max_length=500, verbose_name='Lien de la source'),
        ),
        migrations.AddField(
            model_name='device',
            name='source_label',
            field=models.CharField(blank=True, max_length=255, verbose_name='Source textuelle'),
        ),
    ]
