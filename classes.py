from __future__ import annotations


class Senha:
    __texto: str

    def __init__(self, texto: str):
        self.__texto = texto

    def get_texto_simples(self):
        return self.__texto

    @staticmethod
    def create(texto: str) -> Senha | None:
        tamanho_senha_minimo = 4
        tamanho_senha_maxima = 16

        if tamanho_senha_minimo <= len(texto) <= tamanho_senha_maxima:
            return Senha(texto)

    @staticmethod
    def mock(texto: str) -> Senha:
        return Senha(texto)


# Esta classe representa o usuário, contem as características gerais de um usuário.
# Não se trata de uma classe abstrata pois no momento ela não possui características
# que necessitam ser modificadas por uma classe filha.
class Usuario:
    def __init__(self, nome: str, senha: Senha, id_suap: str):
        self.__nome = nome
        self.__senha = senha
        self.__id_suap = id_suap

    # À ser refatorado para getters e setters nativos do python.
    def get_nome(self):
        return self.__nome

    def get_senha(self):
        return self.__senha

    def get_id_suap(self):
        return self.__id_suap


class Aluno(Usuario):
    def __init__(self, nome: str, senha: Senha, id_suap: str):
        super().__init__(nome, senha, id_suap)


class Servidor(Usuario):
    def __init__(self, nome: str, senha: Senha, id_suap: str):
        super().__init__(nome, senha, id_suap)


# Objeto intermediario que permite que um administrador administre e modifique
# algum usuário.
class ModificadorUsuario:
    def __init__(self, user: Usuario) -> None:
        self.__user = user

    def set_nome(self, nome: str):
        self.__user.__nome = nome

    def set_id_suap(self, id_suap: str):
        self.__user.__id_suap = id_suap


class Administrador(Usuario):
    def __init__(self, nome: str, senha: Senha, id_suap: str):
        super().__init__(nome, senha, id_suap)

    def modificar_usuario(self, user: Usuario) -> ModificadorUsuario:
        return ModificadorUsuario(user)

    def criar_sala(self, numero, nome, descricao, andar, bloco) -> Sala:
        return Sala(numero, nome, descricao, andar, bloco)

    def criar_projeto(self, nome, descricao, professores):
        return Projeto(nome, descricao, professores)


# MAPA
class Bloco:
    def __init__(self, identificador, salas):
        self.__identificador = identificador
        self.__salas = salas

    def get_salas(self):
        return self.__salas


class Andar:
    def __init__(self, numero, salas):
        self.__numero = numero
        self.__salas = salas

    def get_salas(self):
        return self.__salas


class Sala:
    def __init__(self, numero, nome, descricao, andar, bloco):
        self.__numero = numero
        self.__nome = nome
        self.__descricao = descricao
        self.__andar = andar
        self.__bloco = bloco

    def get_info(self):
        return self.__descricao


class Departamento:
    def __init__(
        self, nome, descricao, horario_inicial, horario_final, responsaveis, sala
    ):
        self.__nome = nome
        self.__horario_inicial = horario_inicial
        self.__horario_final = horario_final
        self.__responsaveis = responsaveis
        self.__descricao = descricao
        self.__sala = sala


class Projeto:
    def __init__(self, nome: str, descricao: str, professores):
        self.__nome = nome
        self.__descricao = descricao
        self.__professores_responsaveis = professores

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_descricao(self, descricao: str):
        self.__descricao = descricao


class GrupoDePesquisa:
    def __init__(self, nome: str, descricao: str, projetos, professores):
        self.__nome = nome
        self.__projetos = projetos
        self.__descricao = descricao
        self.__professores_responsaveis = professores

    def add_projeto(self, projeto):
        self.__projetos.append(projeto)

    def remove_projeto(self, projeto):
        self.__projetos.remove(projeto)

    def add_professores_responsaveis(self, professores):
        self.__professores_responsaveis.extend(professores)

    def get_projetos(self):
        return self.__projetos
