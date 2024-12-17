# Curso: Técnico integrado de informática 2°Ano Matutino
# Programação Orientada Objeto
# Alunos:
# Anna Beatriz Ferreira;
# Estéfany Simões;
# Moisés Lopes;
# Thiago Macedo Mendes.

import colorama
from colorama import Fore

from classes import (
    Aluno,
    Andar,
    Bloco,
    Departamento,
    GrupoDePesquisa,
    Projeto,
    Senha,
    Servidor,
    Usuario,
)

colorama.init()

usuarios_cadastrados: dict[str, Usuario] = {}


def cadastrar_usuario(usuario: Usuario):
     try:
        if not usuario.get_nome() or not usuario.get_id_suap() or not usuario.get_senha().get_texto_simples():
            raise ValueError("ID SUAP, senha ou nome não podem estar vazios")
            
         chave = usuario.get_id_suap() + usuario.get_senha().get_texto_simples()
        if chave in usuarios_cadastrados:
            raise ValueError("Usuário já cadastrado")



    usuarios_cadastrados[
        usuario.get_id_suap() + usuario.get_senha().get_texto_simples()
    ] = usuario


for usuario_predefinido in [
    Servidor("Silvio", Senha.mock(str(1234)), str(2000)),
    Servidor("Moises suputa", Senha.mock(str(123456789)), str(2023106060055)),
    Servidor("Moises poopyhead", Senha.mock(str(123456789)), str(2023106060056)),
    Servidor("Moises ich bin schön", Senha.mock(str(123456789)), str(2023106060057)),
    Servidor("Moises ickhead", Senha.mock(str(123456789)), str(2023106060058)),
    Aluno("Moises gato rau", Senha.mock(str(123456789)), str(2023106060059)),
    Aluno("Moises milquentos", Senha.mock(str(123456789)), str(2023106060060)),
    Aluno("Moises creeido", Senha.mock(str(123456789)), str(2023106060061)),
    Aluno("Moises ", Senha.mock(str(1234)), str(2023106)),
]:
    cadastrar_usuario(usuario_predefinido)

# Definindo os blocos
blocos = [Bloco("A"), Bloco("B"), Bloco("C")]

# Definindo os departamentos
depertamentos = [
    Departamento("depex", "estágios", [], [], None),
    Departamento("depesp", "pesquisas", [], [], None),
    Departamento("CPALM", "Patrimônio e Almoxarifado", [], [], None),
    Departamento("DPLAD", "Planejamento e Administração", [], [], None),
    Departamento("CGTI", "Gestão de Tecnologia da Informação", [], [], None),
    Departamento(
        "NAPNE",
        "Atendimento às Pessoas com Necessidades Educacionais Específicas",
        [],
        [],
        None,
    ),
    Departamento("CRA", "Coordenação de Registros Acadêmicos", [], [], None),
]

# Definindo grupos de pesquisa
grupos_de_pesquisa = [
    GrupoDePesquisa(
        "GPMECATRONICA",
        "Projeto",
        [],
        [Projeto("Estrogênias", "Projeto de pesquisa", ["Camila"])],
        ["Camila, Fernando"],
    ),
    GrupoDePesquisa("GOTEC", "Projeto", [], [], ["Caio"]),
]


# Definindo andares
andares = [Andar(0), Andar(1)]


def colorir_texto(cor: str, texto: str) -> str:
    return f"{cor}{texto}{Fore.RESET}"


def escrever(cor: str, texto: str):
    print(colorir_texto(cor, texto))


def alertar_erro(mensagem: str):
    escrever(Fore.RED, f"Erro: {mensagem}")


def escolha_simples(escolhas: list[str]) -> int:
    escolha = None

    while not escolha:
        for i, opcao in enumerate(escolhas):
            escrever(Fore.GREEN, f"{i + 1} - {opcao}")

        possivel_escolha: int | None = None
        try:
            possivel_escolha = int(input("Escolha: "))
        except ValueError:
            alertar_erro("Digite um número!")
        else:
            if not (1 <= possivel_escolha <= len(escolhas)):
                alertar_erro(
                    f"Escolha ínvalida! (Escolha no intervalo: {1}-{len(escolhas)})"
                )
            else:
                escolha = possivel_escolha

    return escolha - 1


while True:
    escrever(Fore.GREEN, "Acesso do mapa de departamentos")
    escolha = escolha_simples(["Login", "Registrar usúario"])

    # login para entrar
    if escolha == 0:
        print("LOGIN")

        id_suap = input("Usuário: ")
        senha = input("Senha: ")

        if (id_suap + senha) in usuarios_cadastrados:
            escrever(Fore.YELLOW, "Você está logado")
        else:
            escrever(Fore.RED, "Usuário não encontrado")
    # cadastrar usuário
    elif escolha == 1:
        escrever(Fore.GREEN, "Registrar usúario no sistema")
        tipo_cadastro = escolha_simples(["Servidor", "Aluno"])

        id_suap = input("Usuário: ")
        nome = input("Nome: ")
        senha = None

        while True:
            if senha := Senha.create(input(Fore.GREEN + "Senha: ")):
                escrever(Fore.YELLOW, f"{nome} você está cadastrado pode ir pro login")
                break
            else:
                escrever(Fore.RED, "Senha inválida")

        if tipo_cadastro == 0:
            cadastrar_usuario(Servidor(nome, senha, id_suap))
        elif tipo_cadastro == 1:
            cadastrar_usuario(Aluno(nome, senha, id_suap))
            
#listar 
for colecao in colecoes_nativas:
    tipo = type(colecao)


if tipo == list:
        cor = Fore.RED
    elif tipo == tuple:
        cor = Fore.YELLOW
    elif tipo == set:
        cor = Fore.GREEN
    elif tipo == dict:
        cor = Fore.CYAN
    elif tipo == str:
        cor = Fore.MAGENTA
    elif tipo == range:
        cor = Fore.BLUE
    else:
        cor = Fore.WHITE

    print(f"Valor: {cor}{colecao}{Fore.RESET}, Tipo: {Fore.RESET}{cor}{tipo}{Fore.RESET}")
