from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SnacksTests(SimpleTestCase):
    def test_home_status(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)

    def test_about_status(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)

    def test_home_template(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res,'home.html')
        self.assertTemplateUsed(res,'_base.html')

    def test_about_template(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertTemplateUsed(res,'about.html')
        self.assertTemplateUsed(res,'_base.html')