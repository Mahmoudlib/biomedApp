from django.core.management.base import BaseCommand

from core.models import Company, Device


class Command(BaseCommand):
    help = "Seeding initial biomedical devices and companies data for BioMed Senegal"

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")

        # Clear old sample data if re-run
        Device.objects.all().delete()
        Company.objects.all().delete()

        # Seed Devices (matching user's local database)
        devices_data = [
            {
                "name": "AUTOMATE DE BIOCHIMIE",
                "category": "Laboratoire",
                "badge_label": "New Tech",
                "image": "https://img.medicalexpo.com/images_me/photo-g/75772-12513096.jpg",
                "description": "L'automate de biochimie est un équipement de laboratoire destiné à mesurer automatiquement différents paramètres biochimiques dans le sang, le sérum, le plasma ou les urines. Il permet la réalisation rapide et fiable d'analyses indispensables au diagnostic et au suivi des patients.",
                "working_principle": "Après l'introduction de l'échantillon, l'automate distribue automatiquement les réactifs appropriés. Les réactions chimiques produites sont mesurées, généralement par photométrie ou turbidimétrie, puis converties en concentrations grâce aux courbes d'étalonnage intégrées.",
                "maintenance_protocol": "•\tNettoyer les aiguilles de prélèvement. \r\n•\tVérifier les niveaux de réactifs and de solutions de lavage. \r\n•\tContrôler les cuvettes de réaction. \r\n•\tEffectuer le contrôle qualité quotidien.",
                "source_url": "https://grenoblecognition.fr/automate-biochimie-definition-fonctionnement/",
                "verified_by": "APEGBM",
                "is_featured": True,
                "views_count": 391,
            },
            {
                "name": "ANALYSEUR D'HÉMATOLOGIE",
                "category": "Laboratoire",
                "badge_label": "Haute Technologie",
                "image": "https://tse1.mm.bing.net/th/id/OIP.bo5fnY_osufm_WpLJwsgrQHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
                "description": "L'analyseur d'hématologie est un automate de laboratoire permettant de réaliser automatiquement la numération et la caractérisation des cellules sanguines. Il est utilisé pour les examens de NFS (Numération Formule Sanguine) et contribue au diagnostic de nombreuses pathologies hématologiques.",
                "working_principle": "L'échantillon sanguin est aspiré puis analysé grâce à des techniques telles que l'impédance électrique, la cytométrie en flux et la spectrophotométrie. Les cellules sont comptées, différenciées et les résultats sont automatiquement calculés puis affichés.",
                "maintenance_protocol": "•\tNettoyer les sondes d'aspiration. \r\n•\tVérifier les niveaux de réactifs. \r\n•\tEffectuer le contrôle qualité interne. \r\n•\tÉliminer les déchets liquides.",
                "source_url": "https://www.antonmedical.com/fra/article-5678177209625242.html",
                "verified_by": "AEPGBM",
                "is_featured": False,
                "views_count": 275,
            },
            {
                "name": "CENTRIFUGEUSE",
                "category": "Laboratoire",
                "badge_label": "New Tech",
                "image": "https://th.bing.com/th/id/OIP.-wGuxfeqB3q_atm4Z2kSAwHaHa?w=170&h=180&c=7&r=0&o=7&dpr=1.6&pid=1.7&rm=3",
                "description": "La centrifugeuse est un équipement de laboratoire utilisé pour séparer les différents constituants d'un échantillon (sang, urine ou autres liquides biologiques) en fonction de leur densité grâce à la force centrifuge. Elle est indispensable dans les laboratoires d'analyses médicales, de recherche et de biologie clinique.",
                "working_principle": "La centrifugeuse met en rotation un rotor à grande vitesse afin de générer une force centrifuge. Sous l'effet de cette force, les particules les plus denses migrent vers le fond du tube tandis que les constituants les plus légers restent en surface, permettant ainsi leur séparation.",
                "maintenance_protocol": "•\tNettoyer la chambre et le rotor après utilisation. \r\n•\tVérifier l'état des godets et des adaptateurs. \r\n•\tContrôler le verrouillage du couvercle. \r\n•\tS'assurer du bon équilibrage des charges.",
                "source_url": "https://fr.kindle-tech.com/faqs/how-does-a-centrifuge-work-and-for-what-purpose",
                "verified_by": "APEGBM",
                "is_featured": False,
                "views_count": 113,
            },
            {
                "name": "MONITEUR MULTIPARAMETRIQUE",
                "category": "Réanimation",
                "badge_label": "New Tech",
                "image": "https://th.bing.com/th/id/OIP.0gz8THuUizcw3X2dWsnY0AHaFj?w=241&h=181&c=7&r=0&o=7&dpr=1.6&pid=1.7&rm=3",
                "description": "Le moniteur multiparamétrique est un dispositif de surveillance permettant le suivi continu des principaux paramètres physiologiques du patient pendant une intervention chirurgicale ou en soins intensifs. Il contribue à la détection précoce des anomalies et à la sécurité du patient.",
                "working_principle": "Le moniteur recueille les données provenant de différents capteurs (ECG, SpO₂, pression artérielle, température, fréquence respiratoire, etc.). Les signaux sont traités par l'unité centrale puis affichés en temps réel. Des alarmes visuelles et sonores sont déclenchées lorsque les paramètres dépassent les limites définies.",
                "maintenance_protocol": "•\tVérifier les câbles et les capteurs. \r\n•\tContrôler le fonctionnement de l'écran et des alarmes. \r\n•\tNettoyer les accessoires réutilisables. \r\n•\tVérifier le niveau de charge de la batterie.",
                "source_url": "https://www.medical.fr/annonces/6156524-neuf-moniteur-multiparametrique-de-surveillance-edan-im50-ecg-pni-spo2-resp-avec-co2-capnographie-special-jo-paris-2024",
                "verified_by": "APGBM",
                "is_featured": False,
                "views_count": 1201,
            },
            {
                "name": "BISTOURI ÉLECTRIQUE",
                "category": "Bloc opératoire",
                "badge_label": "New Tech",
                "image": "https://tse3.mm.bing.net/th/id/OIP._BkhEqPqTboxmQmJsr6GNwHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
                "description": "Le bistouri électrique est un équipement chirurgical utilisant un courant électrique à haute fréquence pour réaliser la coupe des tissus et assurer la coagulation des vaisseaux sanguins. Il permet de limiter les pertes sanguines et d'améliorer la précision des gestes chirurgicaux.",
                "working_principle": "Le générateur produit un courant électrique à haute fréquence transmis à une électrode active. Au contact des tissus, ce courant génère une chaleur localisée permettant soit la coupe, soit la coagulation selon le mode sélectionné. Le courant retourne ensuite vers le générateur par une plaque de retour en mode monopolaire ou par une seconde électrode en mode bipolaire.",
                "maintenance_protocol": "•\tVérifier les câbles et les électrodes. \r\n•\tContrôler la plaque-patient. \r\n•\tTester les commandes et la pédale. \r\n•\tVérifier les alarmes.",
                "source_url": "https://www.medlikim.com/produit/bistouri-electrique/",
                "verified_by": "APEGBM",
                "is_featured": False,
                "views_count": 1203,
            },
        ]

        for d in devices_data:
            Device.objects.create(**d)
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {len(devices_data)} devices."))

        # Seed Companies (matching user's local database)
        companies_data = [
            {
                "name": "Afrique Conception Distribution (ACD)",
                "specialization": "Études, distribution et gestion d’équipements d’imagerie, de soins et d'infrastructures biomédicales clés en main",
                "region": "Dakar",
                "address": "Sicap Liberté 4 – Lot B 104",
                "email": "contact@acd.sn",
                "website": "https://acd.sn/",
                "linkedin_url": "https://www.linkedin.com/company/afrique-conception-distribution/",
                "phone": "+221 33 825 74 52",
                "is_leader": True,
                "logo": "https://acd.sn/wp-content/uploads/2025/04/acd_1.png",
                "description": "Afrique Conception Distribution (ACD) accompagne la modernisation des infrastructures sanitaires en fournissant des équipements de haute technologie biomédicale, de biologie médicale et de radiologie, accompagnés d'un service d'ingénierie et de maintenance dédié.",
            },
            {
                "name": "Carrefour Médical",
                "specialization": "Imagerie médicale, cardiologie, exploration fonctionnelle et réanimation",
                "region": "Dakar",
                "address": "N°229 Entrée CICES - VDN - Dakar - Sénégal",
                "email": "carrefour.medical@orange.sn",
                "website": "https://www.carrefourmedical.sn",
                "linkedin_url": "https://www.linkedin.com/company/carrefourmedical/",
                "phone": "+221 33 869 04 40",
                "is_leader": True,
                "logo": "https://www.carrefourmedical.sn/wp-content/uploads/2021/12/logo-cm.png",
                "description": "Carrefour Médical est un équipementier médical de référence au Sénégal. Il commercialise des scanners, IRM, échographes, moniteurs multiparamétriques et respirateurs de grandes marques internationales, tout en assurant l'assistance technique et la formation du personnel soignant.",
            },
            {
                "name": "Delta Médical",
                "specialization": "Gynécologie-obstétrique, stérilisation et équipements hospitaliers généraux",
                "region": "Dakar",
                "address": "11 RUE DE THIONG, DAKAR, 110000, SN",
                "email": "contact@deltamedical.sn",
                "website": "https://www.deltamedical.sn",
                "linkedin_url": "https://www.linkedin.com/company/delta-medical-senegal/about/",
                "phone": "+221 33 889 37 37",
                "is_leader": False,
                "logo": "https://www.deltamedical.sn/wp-content/uploads/2024/04/logo.png",
                "description": "Fournisseur d'équipements pour la santé maternelle et infantile, tables d'opération, autoclaves de stérilisation et systèmes d'aspiration médicale.",
            },
            {
                "name": "Dimenter",
                "specialization": "Biologie médicale, réactifs de laboratoire et maintenance d'automates d'analyse",
                "region": "Dakar",
                "address": "Immeuble H – Sacré Cœur 1 BP 1329 – Dakar - Sénégal",
                "email": "dimenter@dimenter.sn",
                "website": "https://www.diminter.com/",
                "linkedin_url": "https://www.linkedin.com/company/diminter/",
                "phone": "+221 33 825 77 63 / 78 427 92 92",
                "is_leader": False,
                "logo": "https://www.diminter.com/wp-content/uploads/elementor/thumbs/logo-2-rfa5vczuz67i5toot4jt2up8f8xxt7j5ziqdmish6o.png",
                "description": "Société spécialisée dans l'équipement de laboratoires d'analyses médicales (hématologie, biochimie, immuno-analyse), la fourniture de réactifs certifiés et la gestion de contrats de maintenance préventive pour automates de laboratoire.",
            },
            {
                "name": "Matériel Médical Hospitalier (MMH)",
                "specialization": "Distribution de matériel médico-chirurgical et consommables hospitaliers",
                "region": "Dakar",
                "address": "SIPRES 2, Lot N°3 Liberté 6 En face Mosquée Abass Sall BP : 50856 Dakar, Sénégal",
                "email": "mmh@mmh-africa.sn",
                "website": "https://mmh-africa.sn/",
                "linkedin_url": "https://www.linkedin.com/company/mmh-africa/",
                "phone": "+221 33 827 44 88 / (+221) 78 161 02 98",
                "is_leader": True,
                "logo": "https://mmh-africa.sn/wp-content/uploads/2026/03/logoMMH-site.png",
                "description": "MMH est un actor majeur dans la fourniture d'équipements pour blocs opératoires, mobilier hospitalier, instrumentation chirurgicale et dispositifs de réanimation. L'entreprise assure également le service après-vente (SAV) et le suivi technique des installations.",
            },
            {
                "name": "Technologie Services",
                "specialization": "Fourniture, installation et maintenance d'équipements biomédicaux, avec un accompagnement global pour vos projets clés en main",
                "region": "Dakar",
                "address": "N°94-95 Sacré-Cœur Pyrotechnie Keur Gorgui, Dakar",
                "email": "info@techservsn.com",
                "website": "https://www.techservsn.com/",
                "linkedin_url": "https://www.linkedin.com/company/techserv-sn/about/",
                "phone": "+221 33 865 05 05",
                "is_leader": True,
                "logo": "https://www.techservsn.com/images/LogoTS.png",
                "description": "Entreprise spécialisée dans la distribution, la maintenance préventive et curative, ainsi que l'installation d'équipements médicaux avancés (imagerie médicale, blocs opératoires, réanimation). Partenaire clé des établissements de santé publics et privés au Sénégal.",
            },
        ]

        for c in companies_data:
            Company.objects.create(**c)
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {len(companies_data)} companies."))

        # Create default superuser if it doesn't exist
        from django.contrib.auth.models import User

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@biomed-app.com", "adminpass")
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created with password 'adminpass'"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' already exists"))
