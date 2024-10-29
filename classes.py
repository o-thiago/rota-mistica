from __future__ import annotations

from abc import ABC


class Senha:
    __texto: str

    def __init__(self, texto: str):
        self.__texto = texto

    def get_texto_simples(self):
        return self.__texto

    @staticmethod
    def create(texto: str) -> Senha | None:
        TAMANHO_SENHA_MINIMO = 4
        TAMANHO_SENHA_MAXIMA = 16

        if TAMANHO_SENHA_MINIMO <= len(texto) <= TAMANHO_SENHA_MAXIMA:
            return Senha(texto)

    @staticmethod
    def mock(texto: str) -> Senha:
        return Senha(texto)


# Esta classe representa o usuário, é uma classe abstrata e tem as características gerais de um usuário.
class Usuario(ABC):
    def __init__(self, nome: str, senha: Senha, id_suap: str):
        self.__nome = nome
        self.__senha = senha
        self.__id_suap = id_suap

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























































