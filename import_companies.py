import os
import django

# Configuration de l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biomedApp.settings')
django.setup()

from core.models import Company

companies_data = [
    {
        "name": "Technologie Services",
        "logo": "",
        "specialization": "Fourniture, installation et maintenance d'équipements biomédicaux et de laboratoire",
        "email": "contact@technologieservices-sn.com",
        "website": "https://technologieservices-sn.com",
        "linkedin_url": "https://www.linkedin.com/company/technologie-services-senegal/",
        "description": "Entreprise spécialisée dans la distribution, la maintenance préventive et curative, ainsi que l'installation d'équipements médicaux avancés (imagerie médicale, blocs opératoires, réanimation). Partenaire clé des établissements de santé publics et privés au Sénégal.",
        "region": "Dakar",
        "address": "Avenue Cheikh Anta Diop, Dakar, Sénégal",
        "phone": "+221 33 825 00 00",
        "is_leader": True,
    },
    {
        "name": "Matériel Médical Hospitalier (MMH)",
        "logo": "",
        "specialization": "Distribution de matériel médico-chirurgical et consommables hospitaliers",
        "email": "info@mmh-senegal.com",
        "website": "https://www.mmh-senegal.com",
        "linkedin_url": "https://www.linkedin.com/company/materiel-medical-hospitalier/",
        "description": "MMH est un acteur majeur dans la fourniture d'équipements pour blocs opératoires, mobilier hospitalier, instrumentation chirurgicale et dispositifs de réanimation. L'entreprise assure également le service après-vente (SAV) et le suivi technique des installations.",
        "region": "Dakar",
        "address": "Rue Aimé Césaire, Fann Résidence, Dakar, Sénégal",
        "phone": "+221 33 864 50 50",
        "is_leader": True,
    },
    {
        "name": "Afrique Conception Distribution (ACD)",
        "logo": "",
        "specialization": "Distribution d'équipements de laboratoire, imagerie et solutions biomédicales clés en main",
        "email": "contact@acd-biomed.com",
        "website": "https://www.acd-biomed.com",
        "linkedin_url": "https://www.linkedin.com/company/afrique-conception-distribution/",
        "description": "Afrique Conception Distribution (ACD) accompagne la modernisation des infrastructures sanitaires en fournissant des équipements de haute technologie biomédicale, de biologie médicale et de radiologie, accompagnés d'un service d'ingénierie et de maintenance dédié.",
        "region": "Dakar",
        "address": "Zone Industrielle de Sotiba, Route de Rufisque, Dakar, Sénégal",
        "phone": "+221 33 832 12 34",
        "is_leader": True,
    },
    {
        "name": "Carrefour Médical",
        "logo": "",
        "specialization": "Imagerie médicale, cardiologie, exploration fonctionnelle et réanimation",
        "email": "carrefour.medical@orange.sn",
        "website": "https://www.carrefourmedical.sn",
        "linkedin_url": "https://www.linkedin.com/company/carrefour-medical-senegal/",
        "description": "Carrefour Médical est un équipementier médical de référence au Sénégal. Il commercialise des scanners, IRM, échographes, moniteurs multiparamétriques et respirateurs de grandes marques internationales, tout en assurant l'assistance technique et la formation du personnel soignant.",
        "region": "Dakar",
        "address": "Sacre Cœur 3, VDN, Dakar, Sénégal",
        "phone": "+221 33 827 88 88",
        "is_leader": True,
    },
    {
        "name": "Dimenter",
        "logo": "",
        "specialization": "Biologie médicale, réactifs de laboratoire et maintenance d'automates d'analyse",
        "email": "dimenter@dimenter.sn",
        "website": "https://www.dimenter.sn",
        "linkedin_url": "https://www.linkedin.com/company/dimenter-senegal/",
        "description": "Société spécialisée dans l'équipement de laboratoires d'analyses médicales (hématologie, biochimie, immuno-analyse), la fourniture de réactifs certifiés et la gestion de contrats de maintenance préventive pour automates de laboratoire.",
        "region": "Dakar",
        "address": "Point E, Rue de Diourbel, Dakar, Sénégal",
        "phone": "+221 33 824 15 15",
        "is_leader": False,
    },
    {
        "name": "Delta Médical",
        "logo": "",
        "specialization": "Gynécologie-obstétrique, stérilisation et équipements hospitaliers généraux",
        "email": "contact@deltamedical.sn",
        "website": "https://www.deltamedical.sn",
        "linkedin_url": "https://www.linkedin.com/company/delta-medical-sn/",
        "description": "Fournisseur d'équipements pour la santé maternelle et infantile, tables d'opération, autoclaves de stérilisation et systèmes d'aspiration médicale.",
        "region": "Dakar",
        "address": "Bourguiba, Immeuble Delta, Dakar, Sénégal",
        "phone": "+221 33 824 90 90",
        "is_leader": False,
    },
    {
        "name": "BioTech Sénégal",
        "logo": "",
        "specialization": "Maintenance biomédicale, métrologie et contrôle qualité des dispositifs médicaux",
        "email": "support@biotech-senegal.com",
        "website": "https://www.biotech-senegal.com",
        "linkedin_url": "https://www.linkedin.com/company/biotech-senegal/",
        "description": "Entreprise de services spécialisée dans l'ingénierie biomédicale, l'audit du parc matériel des structures de santé et le contrôle réglementaire des dispositifs médicaux.",
        "region": "Thiès",
        "address": "Quartier Escale, Thiès, Sénégal",
        "phone": "+221 33 951 20 20",
        "is_leader": False,
    }
]

created_count = 0
updated_count = 0

for company_info in companies_data:
    obj, created = Company.objects.update_or_create(
        name=company_info["name"],
        defaults=company_info
    )
    if created:
        print(f"Entreprise créée : {obj.name}")
        created_count += 1
    else:
        print(f"Entreprise mise à jour : {obj.name}")
        updated_count += 1

print(f"\nTerminé ! {created_count} créées, {updated_count} mises à jour.")
