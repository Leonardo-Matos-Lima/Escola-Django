from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from rest_framework import status
from django.urls import reverse
from rest_framework.test import force_authenticate


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(
            username = 'admin',
            password = 'admin'
        )
        self.url = reverse('Estudantes-list')


    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação de um usuario com as credenciais corretas"""
        usuario = authenticate(username = 'admin', password = 'admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)


    def test_autenticacao_user_com_username_incorreto(self):
        """Teste que verifica a autenticação de um usuario com o username incorreto"""
        usuario = authenticate(username = 'adm', password = 'admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)


    def test_autenticacao_user_com_password_incorreto(self):
        """Teste que verifica a autenticção de um usuario com o password incorreto"""
        usuario = authenticate(username = 'admin', password = 'adm')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)


    def test_requisicao_get_autorizada(self):
        """Teste que verifica uam requisição GET autorizada"""
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)