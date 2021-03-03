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
    comunidade precisa ter acesso integral à vacina.
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
    {"="*24} Opção inválida. Tente novamente {"="*23}
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

def decisao_2():
    """vão todas juntas"""
    texto("""
    Vocês chegam na casa do Palhaço, veem vários freezers, e duas enfermeiras do 
    hospital. Vão para o quintal de Jurema e conversam sobre o que fazer, mas ficam 
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
    "pegar as armas do memorial",
    "ir sem armas"
    )
    return decisao

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
    decisao = decisao_2()
    if decisao == 1: f2_1()
    elif decisao == 2: f2_2()
    else:
        invalid()
        f2()

def f2_1():
    decisao = decisao_2_1()
    if decisao == 1: f2_1_1()
    elif decisao == 2: f2_1_2()
    else:
        invalid()
        f2_1()

def f2_2():
    decisao = decisao_2_2()
    if decisao == 1: f2_2_1()
    elif decisao == 2: f2_2_2()
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
    
    if decisao == 1: f1_1_1()
    elif decisao == 2: f1_1_2()
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
    if decisao == 1: f1_2_1()
    elif decisao == 2: f1_2_2()
    else:
        invalid()
        f1_2()

#--------------------------------------------------------------ENREDO DE SANDINO
def s0():
    texto("""
    O que Fátima contou faz você e Jurema começarem a ligar os pontos. Já corria 
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
    if decisao == 1: s1()
    elif decisao == 2: s2()
    else:
        invalid()
        s0()

def s2():
    decisao = decisao_2()
    if decisao == 1: s2_1()
    elif decisao == 2: s2_2()
    else:
        invalid()
        s2()

def s2_1():
    decisao = decisao_2_1()
    if decisao == 1: s2_1_1()
    elif decisao == 2: s_1_2()
    else:
        invalid()
        s2_1()

def s2_2():
    decisao = decisao_2_2()
    if decisao == 1: s2_2_1()
    elif decisao == 2: s2_2_2()
    else:
        invalid()
        s2_2()

def s1():
    texto("""
    
    """)
    decisao1 = escolha(
    "seguir",
    "investigar calada",
    "contar para alguns colegas"
    )
    if decisao1 == 1: s1_1()
    elif decisao1 == 2: s1_2()
    else:
        invalid()
        s1()

def s1_1():
    texto("""
    
    """)
    decisao1_1 = escolha(
    "faz",
    "confrontá-los",
    "ir atrás das suas amigas"
    )
    
    if decisao1_1 == 1: s1_1_1()
    elif decisao1_1 == 2: s1_1_2()
    else:
        invalid()
        s1_1()

def s1_2():
    texto("""
    
    """)
    decisao1_2 = escolha(
    "faz",
    "convocar reunião do hospital",
    "ir atrás das suas amigas"
    )
    
    if decisao1_2 == 1: s1_2_1()
    elif decisao1_2 == 2: s1_2_2()
    else:
        invalid()
        s1_2()

# INÍCIO DO JOGO
inicio()




