from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import celular_invalido, nome_invalido, cpf_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        """
        model = Variavel que diz o modelo que queremos serializar.
        fields = Variavel que diz quais dados vão ser incluidos nesse serializador.
        """
        model =  Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self, dados):
        """
        Validação de dados com a biblioteca que nos permite passar uma mensagem de erro.
        """
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({"cpf":"O cpf deve ter 11 digitos!"})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({"nome": "O nome só pode ter letras!"})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({"celular": "O celular deve ter 13 digitos!"})
        return dados
    

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        """
        model = Variavel que diz o modelo que queremos serializar.
        fields = Variavel que diz quais dados vão ser incluidos nesse serializador, o comando '__all__' diz que todos os dados serão incluidos.
        """
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        """
        model = Variavel que diz o modelo que queremos serializar.
        exclude = Variavel que diz quais dados vão ser excluidos nesse serializador, nesse caso está vazio porque todos os dados serão usados.
        """
        model = Matricula
        exclude = []


class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    """
    curso = Variavel que vai procurar e ler apenas a descrição do curso.
    """
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        """
        Retorno que vai pegar o periodo da matricula.
        """
        return obj.get_periodo_display()
    

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    """
    estudante_nome = Variavel que vai procurar e ler apenas o nome de um estudante.
    """
    estudante_nome =serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']


class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model =  Estudante
        fields = ['id', 'nome', 'email', 'celular']