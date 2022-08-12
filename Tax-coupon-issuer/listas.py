from modulos import *
from parametros import *


        ##########################################################################

                            ###Listas###
#Lista de Cores                           
cores = [
    "#f9f9f9",
    "#696969",
    "#c7d0d8",
    "#d9d9d9"
]
        ##########################################################################

#Lista de Fontes
fonte1 = tkFont.Font(family="Arial", size=20, weight="bold", slant="italic")    #Definindo padrão de fonte
fonte1_1 = tkFont.Font(family="Arial", size=35, weight="bold")                  #Definindo padrão de fonte
fonte1_2 = tkFont.Font(family="Arial", size=20, weight="bold")                  #Definindo padrão de fonte
fonte1_3 = tkFont.Font(family="Arial", size=15, weight="bold")                  #Definindo padrão de fonte
fonte1_4 = tkFont.Font(family="Arial", size=12, weight="bold")                  #Definindo padrão de fonte
fonte1_5 = tkFont.Font(family="Arial", size=12)                                 #Definindo padrão de fonte

fontes = [
    fonte1,     #fontes[0]
    fonte1_1,   #fontes[1]
    fonte1_2,   #fontes[2]
    fonte1_3,   #fontes[3]
    fonte1_4,   #fontes[4]
    fonte1_5    #fontes[5]
]
        ##########################################################################

#Lista de blocos de fundo
bloco_info = PhotoImage(file= fr"{get_dir}\Blocos\bloco_info.png")
bloco_prod = PhotoImage(file= fr"{get_dir}\Blocos\bloco_prod.png")

bloco = [
    bloco_info, #bloco[0]
    bloco_prod  #bloco[1]
    ]
        ##########################################################################

#lista de Botões
bot_limpar = PhotoImage(file= fr"{get_dir}\Botões\bt_limpar.png")
bot_emitir = PhotoImage(file= fr"{get_dir}\Botões\bt_emitir.png")

bot = [
    bot_limpar, #bot[0]
    bot_emitir  #bot[1]
]
        ##########################################################################

#Lista de Frutas para seção de Hortifruti
frutas = [
    "Banana",
    "Maça",
    "Abacate",
    "Laranja",
    "Kiwi",
    "Uva",
    "Pera",
    "Melancia",
]
        ##########################################################################

#Lista de Produtos de higiene para seção Higiene
higiene = [
    "Papel Higienico",
    "Escova de dentes",
    "Pasta de dente",
    "Fio Dental",
    "Shampoo",
    "Condicionador",
    "Desodorante",
    "Pós barba"
]
        ##########################################################################

#Lista de comidas para seção Mantimentos
mantimentos = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Molho",
    "Ovos",
    "Sal",
    "Açucar",
    "Temperos",
]

