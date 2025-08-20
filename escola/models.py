from django.db import models
from django.core.validators import MinLengthValidator

class Estudante(models.Model):
    """
    Criação de campos dos dados que queremos passando o total de caracteres possiveis (max_length).
    Unique = Dado único que ão pode ser repetido assim como o id.
    Blank = Dado não pode ficar em branco.
    """
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11, unique = True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)
    def _str_(self):
        return self.nome
    

class Curso(models.Model):
    """
    Aqui temos os dados sobre um curso e temos um sistema de escoha com 3 opções.
    NIVEL = tupla com tuplas que correspondem as tres opções que temos para o nivel do curso.
    validators = Validação que nos indica o mínimo de caracteres possiveis para o campo (usado quando se quer um 'len' exato de um dado).
    choices = Paramtero que diz que nossa escolha de nivel vai vir da tupla 'NIVEL'.
    null = Parametro que diz que o campo não pode ser nulo.
    default = Parametro que diz que caso não seja especificado o nivel, por padrão ele será 'B' de Básico.
    """
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )        
    codigo = models.CharField(max_length = 10, unique = True, validators = [MinLengthValidator(3)])
    descricao = models.CharField(max_length = 100, blank = False)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')
    def _str_(self):
            return self.codigo
    

class Matricula(models.Model):
    """
    Aqui temos os dados das matriculas e assim como em cursos temos um sistema de tres opções.
    PERIODO = Tupla com tuplas que correspondem as tres opções que temos para período de matrícula.
    on_delete=models.CASCADE = Parametro para apagar todos os dados ao ser deletado a matrícula.
    choices = Paramtero que diz que nossa escolha de nivel vai vir da tupla 'PERIODO'.
    null = Parametro que diz que o campo não pode ser nulo.
    default = Parametro que diz que caso não seja especificado o nivel, por padrão ele será 'M' de Matutino.
    """
    PERIODO = (
            ('M', 'Matutino'),
            ('V', 'Vespertino'),
            ('N', 'Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo =  models.CharField(max_length = 1, choices = PERIODO, blank = False, null = False, default = 'M')