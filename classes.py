from __future__ import annotations

from dataclasses import dataclass


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

    def criar_sala(self, numero, andar, bloco) -> Sala:
        return Sala(numero, andar, bloco)

    def criar_projeto(self, nome, descricao, professores):
        return Projeto(nome, descricao, professores)


@dataclass
class Bloco:
    # O identificador do bloco no IFRO (A, B, C...)
    id: str


@dataclass
class Andar:
    numero: int


@dataclass
class Sala:
    andar: int
    bloco: Bloco
    numero: int | None = None
    grupo: GrupoDePesquisa | None = None

    def mostrar_informacoes(self):
        print(f"Sala {self.numero}, Andar {self.andar}, Bloco {self.bloco.id}")



# Representa o horário de funcionamento de alguma entidade.
# Por exemplo, o DEPAE pode funcionar das 8 as 12, GOTEC das 8 as 18 e assim vai.
@dataclass
class IntervaloFuncionamento:
    inicial: int
    final: int


@dataclass
class Departamento:
    nome: str
    descricao: str
    horarios: list[IntervaloFuncionamento]
    # A tipagem disso aqui deve ser mudada futuramente. Mas vai depender da estrutura
    # que o projeto vai tomar...
    responsaveis: list[str]
    sala: int | None

    def mostrar_informacoes(self):
        print(f"Departamento: {self.nome}\nDescricao: {self.descricao}")


@dataclass
class Projeto:
    nome: str
    descricao: str
    professores: list[str]


@dataclass
class GrupoDePesquisa:
    nome: str
    descricao: str
    horarios: list[IntervaloFuncionamento]
    projetos: list[Projeto]
    professores: list[str]
    salas: list[Sala]


    def adicionar_projeto(self, projeto: Projeto):
        self.projetos.append(projeto)

    def remover_projeto(self, projeto: Projeto):
        self.projetos.remove(projeto)
    
    def mostrar_informacoes(self):
        print(f"Grupo: {self.nome}\nDescricao: {self.descricao}\nProfessores: {', '.join(self.professores)}\nLocalizações: {', '.join([f"sala {i+1} - (andar: {s.andar}, bloco: {s.bloco.id})" for i, s in enumerate(self.salas)])}")

