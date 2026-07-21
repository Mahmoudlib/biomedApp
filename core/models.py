from django.db import models

class Device(models.Model):
    CATEGORY_CHOICES = [
        ('Laboratoire', 'Laboratoire'),
        ('Imagerie', 'Imagerie médicale'),
        ('Bloc opératoire', 'Bloc opératoire'),
        ('Cardiologie', 'Cardiologie'),
        ('Réanimation', 'Réanimation & Urgences'),
    ]

    name = models.CharField(max_length=255, verbose_name="Nom de l'appareil")
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Laboratoire', verbose_name="Spécialité / Catégorie")
    image = models.URLField(max_length=500, blank=True, verbose_name="URL de l'image")
    description = models.TextField(verbose_name="Description clinique & aperçu")
    working_principle = models.TextField(verbose_name="Principe de fonctionnement")
    maintenance_protocol = models.TextField(verbose_name="Protocole de maintenance préventive")
    source_url = models.URLField(max_length=500, verbose_name="Lien de la source obligatoire")
    verified_by = models.CharField(max_length=255, default="Comité d'Expertise Biomédicale du Sénégal (AETQBM)", verbose_name="Vérifié par")
    views_count = models.PositiveIntegerField(default=1200, verbose_name="Nombre de vues")
    badge_label = models.CharField(max_length=50, default="New Tech", verbose_name="Badge / Étiquette")
    is_featured = models.BooleanField(default=False, verbose_name="Appareil en vedette / Appareil du jour")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Appareil biomédical"
        verbose_name_plural = "Appareils biomédicaux"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom de l'entreprise")
    logo = models.URLField(max_length=500, blank=True, verbose_name="URL du Logo")
    specialization = models.CharField(max_length=255, verbose_name="Spécialisation / Domaine d'activité")
    email = models.EmailField(verbose_name="Email de contact")
    website = models.URLField(max_length=500, blank=True, verbose_name="Site Web officiel")
    linkedin_url = models.URLField(max_length=500, blank=True, verbose_name="Page LinkedIn")
    description = models.TextField(verbose_name="Description & Services")
    region = models.CharField(max_length=100, default="Dakar", verbose_name="Région / Ville (Sénégal)")
    address = models.CharField(max_length=255, verbose_name="Adresse physique")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Téléphone")
    is_leader = models.BooleanField(default=False, verbose_name="Leader du secteur")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Entreprise biomédicale"
        verbose_name_plural = "Entreprises biomédicales"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.region}"
