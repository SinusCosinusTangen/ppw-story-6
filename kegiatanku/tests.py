from django.test import TestCase, Client
from .models import peserta, tags

# Create your tests here.
class cobaTestCase(TestCase):
    def test_eksistensi_url(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_eksistensi_halaman(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'kegiatanku/index.html')

    def test_eksistensi_tulisan(self):
        response = Client().get('')
        html_return = response.content.decode('utf8')
        self.assertIn("Responden", html_return)

    def test_eksistensi_models_peserta(self):
        peserta.objects.create(nama="James", domisili="somewhere beetwen me and you")
        self.assertEquals(peserta.objects.all().count(), 1)

    def test_eksistensi_model_tags(self):
        tags.objects.create(nama_kegiatan="smh", deskripsi="sesuatu")
        self.assertEquals(tags.objects.all().count(), 1)

class tambah(TestCase):
    def test_eksistensi_url_tambah(self):
        response = Client().get('/tambah/')
        self.assertEquals(response.status_code, 200)

    def test_eksistensi_peserta(self):
        response = Client().get('/tambah/')
        self.assertEquals(response.status_code, 200)

    def test_eksistensi_template_kegiatan(self):
        response = Client().get('/tambahKegiatan/')
        self.assertTemplateUsed(response, 'kegiatanku/kegiatan.html')

    def test_eksistensi_template_peserta(self):
        response = Client().get('/tambah/')
        self.assertTemplateUsed(response, 'kegiatanku/form.html')

    def test_eksistensi_form_kegiatan(self):
        response = Client().get('/tambahKegiatan/')
        html_response = response.content.decode('utf8')
        self.assertIn("nama", html_response)
        self.assertIn("Simpan", html_response)

    def test_eksistensi_form_peserta(self):
        response = Client().get('/tambah/')
        html_response = response.content.decode('utf8')
        self.assertIn("domisili", html_response)
        self.assertIn("Simpan", html_response)

    def test_simpan_kegiatan(self):
        Client().post('/tambahKegiatan/', {'nama_kegiatan': 'Belajar', 'deskripsi': 'fun'})
        self.assertEquals(tags.objects.all().count(), 1)
