def inicio():

    laco = True
    while laco == True:

        print(f"""
    _____   _____       _   _   _    ____   _   _   ____       _      ____     ___  
   |_   _| | ____|     | | | | | |  / ___| | | | | |  _ \     / \    |  _ \   / _ \ 
     | |   |  _|    _  | | | | | | | |     | | | | | |_) |   / _ \   | |_) | | | | |
     | |   | |___  | |_| | | |_| | | |___  | |_| | |  __/   / ___ \  |  __/  | |_| |
     |_|   |_____|  \___/   \___/   \____|  \___/  |_|     /_/   \_\ |_|      \___/ 
                                                                                    
    {"="*80}
    Estamos na comunidade de Tejucupapo, a comunidade já perdeu 2 anciãs 
    para o novo vírus que circula pelo mundo. E nessa semana chegaram as vacinas 
    suficientes para imunizar 70% da população do local. Mas os coronéis 
    roubaram todas as doses, e a população está recebendo placebo. Fátima, 
    enfermeira no Hospital Elizabete Altino Teixeira vem desconfiando 
    disso há um tempo, e resolveu compartilhar sua teoria com suas amigas 
    Sandino, a ativista; e Jurema, a encantada. Para você ganhar o jogo a 
    comunidade precisa ter acesso integral à vacina. Incluencie o grupo para
    tomar as melhores decisões, que lhe levarão à vitória.
    """)

        menu_iniciar = int(input(f"""
    {"="*80}
    Digite:
    [1] para INICIAR o jogo
    [2] para SAIR do jogo
    {"="*80}
    > """))

        if menu_iniciar == 1:
            entrada_0()
        if menu_iniciar == 2:
            laco = False
        else:
            invalid()
            inicio()
#----------------------------------------------------------------FUNÇÕES BÁSICAS
def escolha(verbo, opcao1, opcao2):
    decisao = int(input(f"""
    {"="*80}
    O que você {verbo}? Digite:
    [1] para {opcao1} 
    [2] para {opcao2}
    {"="*80}  
    > """))
    return decisao

def invalid():
    print(f"""
    {"="*80} 
    {"="*25} Opção inválida. Tente novamente {"="*24}
    {"="*80} 
    """)

def game_over():
    print(f"""
    {"="*80} 
    {"="*35} GAME OVER {"="*36}
    {"="*80} 
    """)

def win():
    print(f"""
    {"="*80} 
    {"="*35} VITÓRIA!!! {"="*35}
    {"="*80} 
    """)

def texto(str):
    print(f"""
    {"="*80}
    {str}""")

def entrada_0():
    entrada = int(
        input(f"""
    {"="*80}
    Quem você quer ser nessa história? Digite:
    [0] para Fátima
    [1] para Sandino
    [2] para Jurema
    {"="*80}
    > """)
    )
    if entrada == 0:
        f0()
    elif entrada == 1:
        s0()
    elif entrada == 2:
        j0()
    else:
        invalid()
        entrada_0() 

def decisao_0(companheira):
    texto(f"""
    O que Fátima contou faz você e {companheira} começarem a ligar os pontos. Já corria 
    algumas histórias pela comunidade, e agora tudo faz sentido. Vocês decidem 
    investigar no latifúndio do Palhaço Junior, líder dos coroneis. Mas Fátima 
    fica em dúvida se ela fica no hospital para não levantar suspeita, ou se vai 
    com vocês.
    """)
    decisao = escolha(
        "sugere",
        "que Fátima fique no hospital", 
        "que Fátima vá com vocês"
    )
    return decisao

def decisao_1(quintal):
    texto("""
    Fátima fica no hospital e vocês vão à casa do Palhaço, veem vários freezers, e 
    duas enfermeiras do hospital. Vão para o quintal {quintal} e conversam sobre o
    que fazer, e ficam em dúvida se devem contar para alguém agora. Ou se devem
    pensar mais um pouco, tomar um chá.
    """)
    decisao = escolha(
    "sugere",
    "tomar um chá",
    "contar para algumas pessoas"
    )
    return decisao

def decisao_1_2():
    texto("""
    Vocês concordam em contar para algumas pessoas. Mas será que é melhor contar
    só para algumas pesssoas que irão ajudar a pensar no que fazer ou divulgar 
    para geral?
    """)
    decisao = escolha(
    "sugere",
    "contar só para algumas pessoas",
    "divulgar para a comunidade interia"
    )

def decisao_2(quintal):
    """vão todas juntas"""
    texto(f"""
    Vocês chegam na casa do Palhaço, veem vários freezers, e duas enfermeiras do 
    hospital. Vão para o quintal {quintal} e conversam sobre o que fazer, mas ficam 
    em dúvida sobre dois caminhos a seguir. 
    """)
    decisao = escolha(
    "sugere",
    "mandar as fotos nos grupos do zap",
    "pegar as vacinas de volta"
    )
    return decisao

def decisao_2_1():
    """ contar no zap """
    texto("""
    As fotos se espalham rapidamente e os grupos viram um caos. Tem muita gente 
    calada, algumas tentando desmentir, e poucas acreditando.
    """)
    decisao = escolha(
    "sugere",
    "convocar assembleia da comunidade",
    "confrontar aliados dos coronéis"
    )
    return decisao

def decisao_2_2():
    """ pegar as vacinas """
    texto("""
    Vocês decidem pegar as vacinas de volta, mas como? 
    """)
    decisao = escolha(
    "sugere",
    "buscar sabedoria no memorial das Heróinas de Tejucupapo",
    "pegar durante a madrugada"
    )
    return decisao

def trabalhadoras():
    """ vacinas só para trabalhadoras(es) """
    win()
    pass
def todos():
    """ vacinas para todo mundo """
    win()
    pass
def perde_apoio():
    """ perder o apoio popular """
    game_over()
    pass
def alianca():
    """ aliança com os coroneis """
    game_over()
    pass
def morre():
    """ o grupo morrer """
    game_over()
    pass
def ignorancia():
    """ ignorância """
    game_over()

    pass
#---------------------------------------------------------------ENREDO DE FÁTIMA
def f0():
    texto("""
    Sandino e Jurema juntaram as peças com outras histórias que corriam pela 
    comunidade e concordaram com a sua teoria. Elas lhe chamaram para ir investigar 
    no latifúndio do coronel Palhaço Júnior, líder dos coronéis.
    """)
    decisao = escolha(
    "decide",
    "permanecer no hospital",
    "ir com elas"
    )
    if decisao == 1: f1()
    elif decisao == 2: f2()
    else:
        invalid()
        f0()

def f2():
    decisao = decisao_2("de Jurema")
    if decisao == 1: f2_1()
    elif decisao == 2: f2_2()
    else:
        invalid()
        f2()

def f2_1():
    decisao = decisao_2_1()
    if decisao == 1: alianca()
    elif decisao == 2: perde_apoio()
    else:
        invalid()
        f2_1()

def f2_2():
    decisao = decisao_2_2()
    if decisao == 1: trabalhadoras()
    elif decisao == 2: morre()
    else:
        invalid()
        f2_2()

def f1():
    """ficar no hospital"""
    texto("""
    Você fica no hospital
    """)
    decisao = escolha(
    "faz a seguir",
    "investigar calada",
    "contar para alguns colegas"
    )
    if decisao == 1: f1_1()
    elif decisao == 2: f1_2()
    else:
        invalid()
        f1()

def f1_1():
    texto("""
    Você fica no hospital para investigar mais e escuta dois médicos conversando 
    sobre os placebos, e eles parecem compactuar com isso. 
    """)
    decisao = escolha(
    "faz",
    "confrontá-los",
    "ir atrás das suas amigas"
    )
    
    if decisao == 1: perde_apoio()
    elif decisao == 2: todos()
    else:
        invalid()
        f1_1()

def f1_2():
    texto("""
    Você resolve contar para alguns colegas de trabalho. A fofoca sai do controle e 
    quase todo mundo fica sabendo. O clima começa a pesar no hospital, há pessoas 
    dizendo que é mentira e outras botando fé.
    """)
    decisao = escolha(
    "faz",
    "convocar reunião do hospital",
    "ir atrás das suas amigas"
    )
    if decisao == 1: perde_apoio()
    elif decisao == 2: todos()
    else:
        invalid()
        f1_2()

# #--------------------------------------------------------------ENREDO DE SANDINO
def s0():
    decisao = decisao_0("Jurema")
    if decisao == 1: s1()
    elif decisao == 2: s2()
    else:
        invalid()
        s0()

def s2():
    decisao = decisao_2("de Jurema")
    if decisao == 1: s2_1()
    elif decisao == 2: s2_2()
    else:
        invalid()
        s2()

def s2_1():
    decisao = decisao_2_1()
    if decisao == 1: alianca()
    elif decisao == 2: perde_apoio()
    else:
        invalid()
        s2_1()

def s2_2():
    decisao = decisao_2_2()
    if decisao == 1: trabalhadoras()
    elif decisao == 2: morre()
    else:
        invalid()
        s2_2()

def s1():
    decisao = decisao_1("de Jurema")
    if decisao == 1: s1_1()
    elif decisao == 2: s1_2()
    else:
        invalid()
        s1()

def s1_1():
    texto("""
    Jurema concorda e vocês vão tomar um chá. Jurema ganhou dois chás novos da
    Cabocla de pena, um é para abraçar a verdade, e o outro é para ignorância 
    abençoada.
    """)
    decisao = escolha(
    "deseja tomar",
    "abraçar a verdade",
    "ignorância abençoada"
    )
    
    if decisao == 1: todos()
    elif decisao == 2: ignorancia()
    else:
        invalid()
        s1_1()

def s1_2():
    decisao = decisao_1_2
    
    if decisao == 1: trabalhadoras()
    elif decisao == 2: perde_apoio()
    else:
        invalid()
        s1_2()

#--------------------------------------------------------------ENREDO DE JUREMA

def j0():
    decisao = decisao_0("Sandino")
    if decisao == 1: j1()
    elif decisao == 2: j2()
    else:
        invalid()
        j0()

def j2():
    decisao = decisao_2("da sua casa")
    if decisao == 1: j2_1()
    elif decisao == 2: j2_2()
    else:
        invalid()
        j2()

def j2_1():
    decisao = decisao_2_1()
    if decisao == 1: alianca()
    elif decisao == 2: perde_apoio()
    else:
        invalid()
        j2_1()

def j2_2():
    decisao = decisao_2_2()
    if decisao == 1: trabalhadoras()
    elif decisao == 2: morre()
    else:
        invalid()
        j2_2()

def j1():
    decisao = decisao_1("da sua casa")
    if decisao == 1: j1_1()
    elif decisao == 2: j1_2()
    else:
        invalid()
        j1()

def j1_1():
    texto("""
    Sandino concorda e vocês vão tomar um chá. Você ganhou dois chás novos da
    Cabocla de pena, um é para abraçar a verdade, e o outro é para ignorância 
    abençoada.
    """)
    decisao = escolha(
    "deseja tomar",
    "abraçar a verdade",
    "ignorância abençoada"
    )
    if decisao == 1: todos()
    elif decisao == 2: ignorancia()
    else:
        invalid()
        j1_1()

def j1_2():
    decisao = decisao_1_2()
    if decisao == 1: trabalhadoras()
    elif decisao == 2: perde_apoio()
    else:
        invalid()
        j1_2()

# INÍCIO DO JOGO
inicio()




