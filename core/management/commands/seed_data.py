from django.core.management.base import BaseCommand
from core.models import Device, Company

class Command(BaseCommand):
    help = 'Seeding initial biomedical devices and companies data for BioMed Senegal'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        
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
                "maintenance_protocol": "•\tNettoyer les aiguilles de prélèvement. \r\n•\tVérifier les niveaux de réactifs et de solutions de lavage. \r\n•\tContrôler les cuvettes de réaction. \r\n•\tEffectuer le contrôle qualité quotidien.",
                "source_url": "https://grenoblecognition.fr/automate-biochimie-definition-fonctionnement/",
                "verified_by": "APEGBM",
                "is_featured": True,
                "views_count": 390
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
                "views_count": 273
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
                "views_count": 113
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
                "views_count": 1201
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
                "views_count": 1203
            }
        ]

        for d in devices_data:
            Device.objects.create(**d)
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {len(devices_data)} devices."))

        # Seed Companies
        companies_data = [
            {
                "name": "BioMed Sénégal SARL",
                "specialization": "Distribution & Maintenance d'Équipements Biomédicaux",
                "region": "Dakar",
                "address": "Avenue Cheikh Anta Diop, Immeuble Horizon, Dakar",
                "email": "contact@biomed-senegal.sn",
                "website": "https://biomed-senegal.sn",
                "linkedin_url": "https://linkedin.com/company/biomed-senegal",
                "phone": "+221 33 825 40 40",
                "is_leader": True,
                "logo": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=200&q=80",
                "description": "Leader sénégalais dans l'importation, l'installation et la maintenance de dispositifs médicaux de pointe. Partenaire agréé des hôpitaux universitaires (CHANN, Fann, Dantec) et des cliniques privées."
            },
            {
                "name": "SenLab Biotech Sénégal",
                "specialization": "Réactifs de Laboratoire & Automates de Diagnostics",
                "region": "Dakar",
                "address": "Zone Industrielle de Sotrac Mermoz, Dakar",
                "email": "info@senlab-biotech.sn",
                "website": "https://senlab-biotech.sn",
                "linkedin_url": "https://linkedin.com/company/senlab-biotech",
                "phone": "+221 33 860 12 12",
                "is_leader": True,
                "logo": "https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?auto=format&fit=crop&w=200&q=80",
                "description": "Spécialiste de la fourniture d'automates de biologie médicale, réactifs de dosage automatisé et solutions intégrées pour laboratoires d'analyses médicales."
            },
            {
                "name": "Sahel Medical Systems (SMS)",
                "specialization": "Imagerie Médicale & Radiologie Numérique",
                "region": "Thiès",
                "address": "Quartier Dixième, Route de Dakar, Thiès",
                "email": "contact@sahelmedical.sn",
                "website": "https://sahelmedical.sn",
                "linkedin_url": "https://linkedin.com/company/sahel-medical-systems",
                "phone": "+221 33 951 88 00",
                "is_leader": False,
                "logo": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=200&q=80",
                "description": "Fournisseur d'équipements de radiologie numérique, d'échographie Doppler et de consommables d'imagerie médicale desservant la région de Thiès et du Sahel."
            },
            {
                "name": "AfriQ Health Technologies",
                "specialization": "Ingénierie Biomédicale & Blocs Opératoires Clé en Main",
                "region": "Saint-Louis",
                "address": "Faubourg Sor, Avenue du Général de Gaulle, Saint-Louis",
                "email": "support@afriqhealth.sn",
                "website": "https://afriqhealth.sn",
                "linkedin_url": "https://linkedin.com/company/afriq-health",
                "phone": "+221 33 961 33 44",
                "is_leader": False,
                "logo": "https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&w=200&q=80",
                "description": "Entreprise spécialisée dans la conception, l'installation de fluides médicaux, l'aménagement de blocs opératoires et le contrat de maintenance préventive."
            }
        ]

        for c in companies_data:
            Company.objects.create(**c)
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {len(companies_data)} companies."))

        # Create default superuser if it doesn't exist
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@biomed-app.com', 'adminpass')
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created with password 'adminpass'"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' already exists"))
