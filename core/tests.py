from django.test import TestCase, Client
from django.urls import reverse
from core.models import Device, Company

class BioMedAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.device = Device.objects.create(
            name="Test ECG",
            category="Cardiologie",
            description="Test Description",
            working_principle="Test Principle",
            maintenance_protocol="Step 1\nStep 2",
            source_url="https://who.int",
            verified_by="Test Verifier",
            badge_label="Test Badge"
        )

        self.company = Company.objects.create(
            name="Test BioMed SN",
            specialization="Test Specialization",
            region="Dakar",
            address="Dakar, Senegal",
            email="test@biomed.sn",
            website="https://test.sn",
            linkedin_url="https://linkedin.com/in/test",
            description="Test company description"
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Biomed Sénégal")

    def test_device_list_view(self):
        response = self.client.get(reverse('device_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test ECG")

    def test_device_list_search_filter(self):
        response = self.client.get(reverse('device_list') + '?q=ECG')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test ECG")

        response_empty = self.client.get(reverse('device_list') + '?q=NonExistent')
        self.assertEqual(response_empty.status_code, 200)
        self.assertContains(response_empty, "Aucun appareil trouvé")

    def test_device_detail_view(self):
        response = self.client.get(reverse('device_detail', args=[self.device.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test ECG")
        self.assertContains(response, "Test Principle")
        self.assertContains(response, "https://who.int")

    def test_company_list_view(self):
        response = self.client.get(reverse('company_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test BioMed SN")

    def test_company_detail_view(self):
        response = self.client.get(reverse('company_detail', args=[self.company.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test BioMed SN")
        self.assertContains(response, "mailto:test@biomed.sn")
        self.assertContains(response, "https://test.sn")
        self.assertContains(response, "https://linkedin.com/in/test")
