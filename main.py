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
        [
            Projeto("Estrogênias", "Projeto de pesquisa sobre inclusão das mulheres", ["Cledenilson", "Camila"]),
            Projeto("Biogirl", "projeto que busca uma vida mais verde", ["Daniela Toda", "Camila"]),
            Projeto("fireFlies", "projeto para criação de um robo para a participação da OBR", ["Cledenilson", "Camila"]),
            Projeto("erick", "projeto que busca uma vida mais verde", ["Willians"]),
        ],
        ["Camila, Daniela"],
    ),
    GrupoDePesquisa("GOTEC", "Projeto", [], [], ["Caio"]),
 ]


# Definindo andares
andares = [Andar(0), Andar(1)]


def confirmar_saida():
    while True:
        escolha = input('''Você realmente quer sair? 
1 - Sim
2 - Não: ''')
        if escolha == "1":
            escrever(Fore.YELLOW, "Retornando ao menu principal...")
            return True  
        elif escolha == "2":
            escrever(Fore.YELLOW, "Retornando ao cadastro...")
            return False 
        else:
            alertar_erro("Escolha inválida. Digite 1 para sim ou 2 para não.")



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
    escolha = escolha_simples(["Login", "Registrar usúario", "Sair"])

# login para entrar
    if escolha == 0:
        print("LOGIN")
#o Try está sendo usado de uma forma "fácil" para exibir o erro
        try:
            id_suap = input("Usuário: ")
            senha = input("Senha: ")

            if (id_suap + senha) in usuarios_cadastrados:
                escrever(Fore.YELLOW, "Você está logado")

# elaborar mais a parte do mapa, aqui começa as escolhas
#AAAAA CONSEGUIIII FAZEERRRRR
                while True:
                    print(Fore.WHITE + '''OLA me chamo Estéfany vou te ajudar
O que você está procurando??''')
                    escolha_mapa = escolha_simples(["Grupo de pesquisas", "departamentos", "sair"])
                    if escolha_mapa == 0: 
                        print(Fore.YELLOW, ''' HUMM interresante...
Você escolheu Grupos de Pesquisas.''')
                        for grupo in grupos_de_pesquisa:
                            for projeto in grupo.projetos:
                               print(Fore.GREEN, f"Projeto: {projeto.nome}, Descrição: {projeto.descricao}")
                  
                    elif escolha_mapa == 1: 
                        escrever(Fore.YELLOW, ''' Olha que legal...
Você escolheu Departamentos.''')
                        for dep in depertamentos:
                            escrever(Fore.GREEN, f"Departamento: {dep.nome}, Descrição: {dep.descricao}")

                    elif escolha_mapa == 2:  
                        escrever(Fore.YELLOW, "Saindo do mapa...")
                        break 







        except ValueError as x:
            alertar_erro(str(x))
        except Exception as x:
            alertar_erro (f"erro totalmente desconhecido:{str(x)}")

        #o else que serve tanto pro login incompleto quanto para o "sair" do submenu
        else:
            escrever(Fore.YELLOW, "Processo de login incompleto.")

    # cadastrar usuário
    elif escolha == 1:
        while True:
            escrever(Fore.GREEN, "Registrar usúario no sistema")
            tipo_cadastro = escolha_simples(["Servidor", "Aluno", "sair"])

            if tipo_cadastro == 2:  
                if confirmar_saida():
                    break  
                else:
                    continue

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
            break
    elif escolha == 2:
        escrever(Fore.YELLOW, "Saindo...")
        break
