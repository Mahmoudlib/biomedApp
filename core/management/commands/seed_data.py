from django.core.management.base import BaseCommand
from core.models import Device, Company

class Command(BaseCommand):
    help = 'Seeding initial biomedical devices and companies data for BioMed Senegal'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        
        # Clear old sample data if re-run
        Device.objects.all().delete()
        Company.objects.all().delete()

        # Seed Devices
        devices_data = [
            {
                "name": "Électrocardiographe (ECG) 12 Pistes",
                "category": "Cardiologie",
                "badge_label": "Essentiel",
                "is_featured": True,
                "views_count": 1850,
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAmhrBUd84eCkaDDXEzl-eA2nWwruMEUyFu4uWo2ZflOQXH46Ac6WVaHoigfASlImLfBzMXJn9NWxWtJZnSNY86W2OsuKpnUhEcxPFK0rHlOLtSkqSJm0oJ9RfKXoNH1EJrYSwAxWuFL3bizxnNrv-VNDRqMDkb5UzA9sUmWUvhgkOxO8w0T0trt1svdotPywOrzRc3XQwIy6V1vxpiaqJHfc8Vr8Oyz-p_KHDjir7GmO21d9Qv8_5mldyE3EOV_138nnKLVLl9-g",
                "description": "Appareil biomédical de diagnostic cardiovasculaire permettant d'enregistrer l'activité électrique du cœur à travers 12 dérivations simultanées. Indispensable pour la détection précoce des arythmies, de l'ischémie myocardique et de l'infarctus.",
                "working_principle": "Le signal cardiaque électrique généré par le nœud sinusal se propage à travers les fibres musculaires. Des électrodes cutanées (4 de membres et 6 précordiales) captent les micro-variations de potentiel (de l'ordre du millivolt). Ces signaux analogiques sont amplifiés, filtrés contre le bruit réseau (50/60 Hz) et convertis par un processeur numérique pour un affichage sur écran et impression thermique.",
                "maintenance_protocol": "1. Nettoyage des câbles et électrodes après chaque utilisation avec une solution désinfectante non corrosive.\n2. Contrôle hebdomadaire du niveau de papier thermique et calibration du zéro.\n3. Inspection mensuelle des câbles patients pour déceler toute usure ou rupture d'isolation.\n4. Vérification annuelle de la précision d'amplification et test de sécurité électrique (courants de fuite selon norme IEC 60601-1).",
                "source_url": "https://www.who.int/medical_devices/publications/en/",
                "verified_by": "Comité National d'Expertise Biomédicale (Dakar)"
            },
            {
                "name": "Analyseur Biochimique Automatique",
                "category": "Laboratoire",
                "badge_label": "New Tech",
                "is_featured": True,
                "views_count": 2140,
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCCnskvMaLqBLnr00zNpv_B6M_zMWFJYmhrYT-YFjF--5mWGS0xA2GvRFF-klPKD5i3HOoyNXHaROe1OKG9PnbgjToGQJIfLs9vfRLNfeIJ8ra4tohoVz53DwqBtCTWdn7qf1b-abEq7-RjXf7ZjJXSIqblHzNdaYno6WIgiCIM9oE7Vah3CKpVWN9qWPtcCDg0Ss_HDVWFef6GLyfrsrrPwn_txRnyy9OsTsx7ZFpOHHiwXE_yPzT2us_dMP7Ltpt0V_OydpL5hg",
                "description": "Système automatisé à haut débit pour le dosage des paramètres biochimiques sanguins et urinaires (glycémie, urée, créatinine, transaminases, bilan lipidique).",
                "working_principle": "Utilise la spectrophotométrie d'absorption moléculaire. Les réactifs spécifiques et les échantillons sont pipetés automatiquement dans des cuvettes réactionnelles thermostatées à 37°C. La variation d'absorbance de la réaction colorimétrique est mesurée par une photodiode à des longueurs d'onde précises selon la loi de Beer-Lambert (A = ε·c·L).",
                "maintenance_protocol": "1. Purge et rinçage quotidien des circuits de fluide avec eau déionisée et détergent dédié.\n2. Calibration hebdomadaire avec sérums de contrôle de qualité (Niveaux Pathologique et Normal).\n3. Remplacement mensuel de la lampe photométrique et contrôle des filtres d'absorbance.\n4. Lubrification trimestrielle des bras d'aspiration robotisés.",
                "source_url": "https://www.ifcc.org/ifcc-scientific-division/",
                "verified_by": "Association des Biologistes du Sénégal"
            },
            {
                "name": "Échographe Doppler Couleur Polyvalent",
                "category": "Imagerie",
                "badge_label": "Haute Précision",
                "is_featured": False,
                "views_count": 1420,
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCcZImEckgD1Yb6BDU0yNFpnmR7d_bpsBw2D7JCKf7cjp6_RWyq2bw7mkCs-KS3vrIt4ePxsJ2Bfs5VZYUC6rG8SfzxrzLFYT7nXQBRFTpehFNqDBLP-pNmX4OJKZGzoIiWkaYBG132ujgNQMuoFMKDoRhThM0JkyeC_wVSAIUIABrV3hQ8IXaEBRWW1w6O-F67wzkPcb6eui2WSZAUsscEmlqhexVzBGk-GG6fbJRyWzNfo2PORJNUG1ci4h-p3PG8WwGmTVqkXw",
                "description": "Système d'imagerie ultrasonore en temps réel équipé de sondes convexes, linéaires et endocavitaires. Permet l'exploration abdominale, obstétricale et vasculaire par Doppler pulsé et couleur.",
                "working_principle": "Repose sur l'effet piézoélectrique. Des cristaux synthétiques situés dans la sonde émettent des impulsions d'ultrasons (2.5 à 15 MHz) qui se propagent dans le corps humain. Les échos réfléchis aux interfaces de différentes impédances acoustiques sont captés, amplifiés et convertis en images en coupe (mode B) et cartographie vasculaire (mode Doppler).",
                "maintenance_protocol": "1. Inspection visuelle quotidienne des cristaux et du câble de sonde (absence de fissure du gel conductif).\n2. Désinfection de haut niveau des sondes de contact avec lingettes bactéricides certifiées.\n3. Dépoussiérage mensuel des filtres à air du système de refroidissement vidéo.\n4. Calibration semestrielle du gain et des courbes de compensation de profondeur (TGC).",
                "source_url": "https://www.isuog.org/clinical-resources.html",
                "verified_by": "Société Sénégalaise de Radiologie & Imagerie Médicale"
            },
            {
                "name": "Défibrillateur Cardiaque Biphasique avec DSA",
                "category": "Réanimation",
                "badge_label": "Urgence VIP",
                "is_featured": False,
                "views_count": 1690,
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuC7_oQ4xma8jbDLg4yTgtsgOnou9MQcXZ4KY_9Z27NXFVEdVuiAGFg3xP8MP4MA3HeTjdaem8AYsmfscZki0wg6GxncX2ZlXhQmBURaTLm3fwozHM1ixSFdohn0meJBTdziqo7J6TYTpmHYJU22pyhaSIoe4AWwPCtvQqXY3vzh5424leyhYTQXkcXr33kR4HGpvkqeHsaHOZPerslTEUxqwqjvkIHDV-WD7rB_uIYYQWPEGfGPM5byLkdCY7WKWn4zTMKZL4myQw",
                "description": "Dispositif médical d'urgence délivrant un choc électrique externe pour restaurer un rythme cardiaque sinusal normal lors d'une fibrillation ventriculaire ou d'une tachycardie ventriculaire sans pouls.",
                "working_principle": "Un condensateur haute tension emmagasine l'énergie électrique programmée (jusqu'à 200 Joules). Lors de la décharge par les électrodes/pales, l'onde électrique biphasique traverse le myocarde dans un sens puis dans le sens inverse, dépolarisant simultanément les cellules cardiaques pour redémarrer le stimulateur naturel du cœur.",
                "maintenance_protocol": "1. Auto-test quotidien automatique (état de la batterie et tension des condensateurs).\n2. Vérification visuelle quotidienne du voyant d'état (vert/rouge) et péremption des électrodes adhésives.\n3. Test mensuel d'impulsion sur charge fictive de 50 Ohms avec mesure de l'énergie réelle délivrée.\n4. Remplacement de la batterie interne au lithium tous les 3 ans.",
                "source_url": "https://www.resus.org.uk/guidelines",
                "verified_by": "SAMU National du Sénégal"
            },
            {
                "name": "Bistouri Électrique / Générateur Électrochirurgical",
                "category": "Bloc opératoire",
                "badge_label": "Chirurgie",
                "is_featured": False,
                "views_count": 980,
                "image": "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=800&q=80",
                "description": "Équipement de bloc opératoire produisant des courants haute fréquence (HF) pour la coupe et la coagulation thermique tissulaire en chirurgie générale, gynécologique et orthopédique.",
                "working_principle": "Utilise un courant alternatif HF (300 kHz à 3 MHz) appliqué via une électrode active de faible surface. L'effet Joule concentré élève instantanément la température cellulaire, causant la vaporisation (coupe) ou la dénaturation protéique (coagulation), tandis qu'une plaque neutre assure le retour sécurisé du courant.",
                "maintenance_protocol": "1. Test du système de surveillance de la plaque neutre (REM / CQM) avant chaque intervention.\n2. Contrôle visuel de l'isolation du câble de pédale et des manches monopolaire/bipolaire.\n3. Vérification trimestrielle de la puissance de sortie mesurée sur analyseur électrochirurgical HF.\n4. Contrôle annuel d'étanchéité électrique et de prise de terre.",
                "source_url": "https://www.aorn.org/",
                "verified_by": "Ordre des Médecins du Sénégal"
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
