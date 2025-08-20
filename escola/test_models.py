from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste',
            email = 'teste@gmail.com',
            cpf = '74697176090',
            data_nascimento = '2006-04-05',
            celular = '86 55555-5555'        
        )

    def test_verifica_atributos_de_estudante(self):
        """Função de teste que verifica os atributos de Estudante"""
        self.assertEqual(self.estudante.nome, 'Teste')
        self.assertEqual(self.estudante.email, 'teste@gmail.com')
        self.assertEqual(self.estudante.cpf, '74697176090')
        self.assertEqual(self.estudante.data_nascimento, '2006-04-05')
        self.assertEqual(self.estudante.celular, '86 55555-5555')


class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'Py',
            descricao = 'Curso de Python',
            nivel = 'B'
        )

    def test_verifica_atributos_de_curso(self):
        """Função teste que verifica os atributos de Curso"""
        self.assertEqual(self.curso.codigo, 'Py')
        self.assertEqual(self.curso.descricao, 'Curso de Python')
        self.assertEqual(self.curso.nivel, 'B')


class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email = 'testemodelomatricula@gmail.com',
            cpf = '74720328083',
            data_nascimento = '2006-04-06',
            celular = '86 55555-5556'  
        )
        self.curso_matricula = Curso.objects.create(
            codigo = 'CTMM',
            descricao = 'Curso Teste Modelo Matricula',
            nivel = 'B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )

    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste Modelo Matricula')
        self.assertEqual(self.matricula.curso.descricao, 'Curso Teste Modelo Matricula')
        self.assertEqual(self.matricula.periodo, 'M')