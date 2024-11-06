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
    Senha,
    Servidor,
    Usuario,
)

colorama.init()

usuarios_cadastrados: dict[str, Usuario] = {}


def cadastrar_usuario(usuario: Usuario):
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
blocoA = Bloco("A", [])
blocoB = Bloco("B", [])
blocoC = Bloco("C", [])

# Definindo os departamentos
departamentoA = Departamento("depex", "estágios", None, None, ["Monnike"], None)
departamentoB = Departamento("depesp", "pesquisas", None, None, None, None)
departamentoC = Departamento(
    "CPALM" "Patrimônio e Almoxarifado", None, None, None, None, None
)
departamentoD = Departamento(
    "DPLAD", "Planejamento e Administração", None, None, None, None
)
departamentoE = Departamento(
    "CGTI", "Gestão de Tecnologia da Informação", None, None, None, None
)
departamentoF = Departamento(
    "NAPNE",
    "Atendimento às Pessoas com Necessidades Educacionais Específicas",
    None,
    None,
    None,
    None,
)
departamentoG = Departamento(
    "CRA", "Coordenação de Registros Acadêmicos", None, None, None, None
)

grupo_de_pesquisaA = GrupoDePesquisa(
    "GPMECATRONICA", "Projeto", ["Estrogênias"], ["Camila, Fernando"]
)
grupo_de_pesquisaB = GrupoDePesquisa("GOTEC", "Projeto", None, ["Caio"])


# Definindo andares
primeiro_andar = Andar(0, [])
segundo_andar = Andar(1, [])


while True:
    print(
        Fore.GREEN
        + """Acesse ao mapa de departamentos
  1 - Login
  2- Registrar usuário"""
    )
    escolha = int(input(""))

    # login para entrar
    if escolha == 1:
        print("LOGIN")
        id_suap = input("Usuário: ")
        senha = input("Senha: ")

        if (id_suap + senha) in usuarios_cadastrados:
            print(Fore.YELLOW + "Você está Logado" + Fore.RESET)
            break

        else:
            print(Fore.RED + "Usuário não encontrado" + Fore.RESET)
    # cadastrar usuário
    elif escolha == 2:
        print("""Registrar usuário no sistema
    1- Servidor
    2- Aluno""")
        tipo_cadastro = int(input())

        id_suap = input("Usuário: ")
        nome = input("Nome: ")
        senha = None

        while True:
            if senha := Senha.create(input(Fore.GREEN + "Senha: ")):
                print(Fore.YELLOW + nome, "você está cadastrado pode ir pro login")
                break
            else:
                print(Fore.RED + "Senha inválida" + Fore.RESET)

        if tipo_cadastro == 1:
            cadastrar_usuario(Servidor(nome, senha, id_suap))
        elif tipo_cadastro == 2:
            cadastrar_usuario(Aluno(nome, senha, id_suap))
        else:
            print(Fore.BLUE + "Tente novamente")

    else:
        print(Fore.BLUE + "Tente novamente")
