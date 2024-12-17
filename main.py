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


def alertar_erro(mensagem: str):
    print(Fore.RED, f"Erro: {mensagem}")

def escolha_simples(escolhas: list[str]) -> int:
    escolha = None
    
    while True:
        for i, opcao in enumerate(escolhas):
            print( f"{i + 1} - {opcao}")

        try:
            possivel_escolha: int | None = int(input("Escolha: "))
        except ValueError:
            alertar_erro("Digite um número!")
        else:
            if not (1 <= possivel_escolha <= len(escolhas)):
                alertar_erro(
                    f"Escolha ínvalida! (Escolha no intervalo: {1}-{len(escolhas)})"
                )
            else:
                  return possivel_escolha - 1

def cadastrar_usuario(usuario: Usuario):
    try:
        if not usuario.get_nome() or not usuario.get_id_suap() or not usuario.get_senha().get_texto_simples():
            raise ValueError("ID do SUAP, senha ou nome não podem estar vazios")
        
        chave = usuario.get_id_suap() + usuario.get_senha().get_texto_simples()
        if chave in usuarios_cadastrados:
            raise ValueError("Usuário já cadastrado")
        
        usuarios_cadastrados[chave] = usuario
    except ValueError as e:
        print( f"Erro ao cadastrar usuário: {e}" )
    except Exception as e:
        print( f"Erro inesperado: {e}" )
    finally:
        print( "Cadastro concluído" )

while True:
    print("Acesso do mapa de departamentos")
    escolha = escolha_simples(["Login", "Registrar usúario"])

    # login para entrar
    if escolha == 0:
        print("LOGIN")
#o Try está sendo usado de uma forma "fácil" para exibir o erro    
        try:
            id_suap = input("Usuário: ")
            senha = input("Senha: ")

            if (id_suap + senha) in usuarios_cadastrados:
                print( "Você está logado")
        finally:
            print("Processo de login incompleto.")

        
    elif escolha == 1:
        while True:
            print(Fore.GREEN, "Registrar usúario no sistema")
            tipo_cadastro = escolha_simples(["Servidor", "Aluno"])

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
                    print(Fore.YELLOW, f"{nome} você está cadastrado pode ir pro login")
                    break
                else:
                    escrever(Fore.RED, "Senha inválida")

            if tipo_cadastro == 0:
                cadastrar_usuario(Servidor(nome, senha, id_suap))
            elif tipo_cadastro == 1:
                cadastrar_usuario(Aluno(nome, senha, id_suap))
            break





try:
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
except Exception as e:
    print( f"Erro ao cadastrar usuários predefinidos: {e}")
finally:
    print("Cadastro de usuários predefinidos concluído")

# Definindo os blocos
try:
    blocos = [Bloco("A"), Bloco("B"), Bloco("C")]
except Exception as e:
    print( f"Erro ao criar blocos: {e}")
finally:
    print( "Blocos definidos")

# Definindo os departamentos
try:
    departamentos = [
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

    for dep in departamentos:
        if not dep.nome:
            raise ValueError("O nome do departamento não pode ser vazio")
except Exception as e:
    print( f"Erro ao criar departamentos: {e}")
finally:
    print( "Departamentos definidos" )

# Definindo grupos de pesquisa
try:
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

    for grupo in grupos_de_pesquisa:
        if not grupo.nome:
            raise ValueError("O nome do grupo de pesquisa não pode estar vazio")
except Exception as e:
    print(f"Erro ao criar grupos de pesquisa: {e}" )
finally:
    print("Grupos de pesquisa definidos" )

# Definindo andares
try:
    andares = [Andar(0), Andar(1)]
except Exception as e:
    print( f"Erro ao criar andares: {e}" )
finally:
    print( "Andares definidos" )

    





