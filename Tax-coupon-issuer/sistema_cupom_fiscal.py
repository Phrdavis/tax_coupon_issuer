from cgi import test
from modulos import *                               #Importe da pasta Modulos

root = tk.Tk()                                      #Definindo variavel para a janela root
get_dir = os.path.dirname(__file__)                 #Definindo variavel para diretorio do arquivo
data = datetime.now().strftime('%d/%m/%Y %H:%M')    #Definindo variavel para data e hora atuais


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
        ##########################################################################
                            ###Função para geração da tela no meio###
def center(win):
    win.update_idletasks()

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    win.deiconify()
        ##########################################################################

                            ###Função para geração de PFD###
def gerar_pdf(args):
    cnv = canvas.Canvas("Nota Fiscal.pdf")
    cnv.drawString(150,450,"uepa")
    cnv.save()
    return 0
 

                            ###Classe principal para formação e configuração da tela###
class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.label()
        self.widgets()
        root.mainloop()
    def tela(self):
        root.title("Gerador de Nota Fiscal")
        root.geometry("1366x743")
        root.configure(background= cores[1])
        root.resizable(False, False)

        center(self.root)

    def frame(self):
        self.frame1 = Frame(self.root, background= cores[0])
        self.frame1.place(anchor= "center", relx=0.5, rely=0.5, relheight=0.95, relwidth=0.95)
    def label(self):

        ##Label para o titulo da Frame##
        self.titulo = Label(self.frame1, text="Emissor de Cupom Fiscal", bg= cores[0])
        self.titulo.configure(font= fontes[0])
        self.titulo.place(anchor="center", relx= 0.5, rely=0.05)
        ##########################################################################

        ##Label para o bloco cinza para informações
        self.bloco_cinza_sup = Label(self.frame1, image= bloco[0], background= cores[0])
        self.bloco_cinza_sup.place(anchor="center", relx= 0.5, rely= 0.13, relheight= 0.1)

        #Label para NOME
        self.nome = Label(self.frame1, text= "Nome:_______________________", bg= cores[2])
        self.nome.configure(font= fontes[3])
        self.nome.place(anchor="center", relx= 0.2, rely=0.13)
        
        #Label para CPF
        self.cpf = Label(self.frame1, text= "CPF:_______________________", bg= cores[2])
        self.cpf.configure(font= fontes[3])
        self.cpf.place(anchor="center", relx= 0.5, rely=0.13)

        #Label para TELEFONE
        self.telefone = Label(self.frame1, text= "Telefone:_______________________", bg= cores[2])
        self.telefone.configure(font= fontes[3])
        self.telefone.place(anchor="center", relx= 0.8, rely=0.13)
        ##########################################################################

                            ###Área de HORTIFRUTI        
        ##Label para o bloco de Hortifruti
        self.bloco_hort = Label(self.frame1, image= bloco[1], background= cores[0])
        self.bloco_hort.place(anchor="center", relx= 0.2, rely= 0.52)

        #Label para descrição: HORTIFRUTI
        self.hort = Label(self.frame1, text= "Hortifruti", background= cores[0])
        self.hort.configure(font= fontes[3])
        self.hort.place(anchor="center", relx= 0.2, rely=0.23)

        #Label para frutas
        self.produto1_hort = Label(self.frame1, text=frutas[0], background= cores[3])
        self.produto1_hort.configure(font= fontes[5])
        self.produto1_hort.place(anchor="center", relx= 0.14, rely= 0.3)
        
        self.produto2_hort = Label(self.frame1, text=frutas[1], background= cores[3])
        self.produto2_hort.configure(font= fontes[5])
        self.produto2_hort.place(anchor="center", relx= 0.14, rely= 0.362)
        
        self.produto3_hort = Label(self.frame1, text=frutas[2], background= cores[3])
        self.produto3_hort.configure(font= fontes[5])
        self.produto3_hort.place(anchor="center", relx= 0.14, rely= 0.424)
        
        self.produto4_hort = Label(self.frame1, text=frutas[3], background= cores[3])
        self.produto4_hort.configure(font= fontes[5])
        self.produto4_hort.place(anchor="center", relx= 0.14, rely= 0.486)
        
        self.produto5_hort = Label(self.frame1, text=frutas[4], background= cores[3])
        self.produto5_hort.configure(font= fontes[5])
        self.produto5_hort.place(anchor="center", relx= 0.14, rely= 0.548)
        
        self.produto6_hort = Label(self.frame1, text=frutas[5], background= cores[3])
        self.produto6_hort.configure(font= fontes[5])
        self.produto6_hort.place(anchor="center", relx= 0.14, rely= 0.61)
        
        self.produto7_hort = Label(self.frame1, text=frutas[6], background= cores[3])
        self.produto7_hort.configure(font= fontes[5])
        self.produto7_hort.place(anchor="center", relx= 0.14, rely= 0.672)
        
        self.produto8_hort = Label(self.frame1, text=frutas[7], background= cores[3])
        self.produto8_hort.configure(font= fontes[5])
        self.produto8_hort.place(anchor="center", relx= 0.14, rely= 0.734)

        #Label para valor do HORTIFRUTI
        self.valor_hort = Label(self.frame1, text= "Valor: R$00,00", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805)
        ##########################################################################

                            ###Área de HIGIENE
        ##Label para o bloco de Higiene 
        self.bloco_hig = Label(self.frame1, image= bloco[1], background= cores[0])
        self.bloco_hig.place(anchor="center", relx= 0.5, rely= 0.52)

        #Label para descrição: HIGIENE
        self.hig = Label(self.frame1, text= "Higiene", background= cores[0])
        self.hig.configure(font= fontes[3])
        self.hig.place(anchor="center", relx= 0.5, rely=0.23)

        #Label para produtos higiene 
        self.produto1_hig = Label(self.frame1, text=higiene[0], background= cores[3])
        self.produto1_hig.configure(font= fontes[5])
        self.produto1_hig.place(anchor="center", relx= 0.45, rely= 0.3)
        
        self.produto2_hig = Label(self.frame1, text=higiene[1], background= cores[3])
        self.produto2_hig.configure(font= fontes[5])
        self.produto2_hig.place(anchor="center", relx= 0.45, rely= 0.362)
        
        self.produto3_hig = Label(self.frame1, text=higiene[2], background= cores[3])
        self.produto3_hig.configure(font= fontes[5])
        self.produto3_hig.place(anchor="center", relx= 0.45, rely= 0.424)
        
        self.produto4_hig = Label(self.frame1, text=higiene[3], background= cores[3])
        self.produto4_hig.configure(font= fontes[5])
        self.produto4_hig.place(anchor="center", relx= 0.45, rely= 0.486)
        
        self.produto5_hig = Label(self.frame1, text=higiene[4], background= cores[3])
        self.produto5_hig.configure(font= fontes[5])
        self.produto5_hig.place(anchor="center", relx= 0.45, rely= 0.548)
        
        self.produto6_hig = Label(self.frame1, text=higiene[5], background= cores[3])
        self.produto6_hig.configure(font= fontes[5])
        self.produto6_hig.place(anchor="center", relx= 0.45, rely= 0.61)
        
        self.produto7_hig = Label(self.frame1, text=higiene[6], background= cores[3])
        self.produto7_hig.configure(font= fontes[5])
        self.produto7_hig.place(anchor="center", relx= 0.45, rely= 0.672)
        
        self.produto8_hig = Label(self.frame1, text=higiene[7], background= cores[3])
        self.produto8_hig.configure(font= fontes[5])
        self.produto8_hig.place(anchor="center", relx= 0.45, rely= 0.734)

        #Label para valor do HIGIENE
        self.valor_hig = Label(self.frame1, text= "Valor: R$00,00", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805)
        ##########################################################################
        
                            ###Área de MANTIMENTOS
        #Label para o bloco de Mantimentos 
        self.bloco_mant = Label(self.frame1, image= bloco[1], background= cores[0])
        self.bloco_mant.place(anchor="center", relx= 0.8, rely= 0.52)   

        #Label para descrição: MANTIMENTOS
        self.mant = Label(self.frame1, text= "Mantimentos", background= cores[0])
        self.mant.configure(font= fontes[3])
        self.mant.place(anchor="center", relx= 0.8, rely=0.23)

        #Label para produtos higiene 
        self.produto1_mant = Label(self.frame1, text=mantimentos[0], background= cores[3])
        self.produto1_mant.configure(font= fontes[5])
        self.produto1_mant.place(anchor="center", relx= 0.74, rely= 0.3)
        
        self.produto2_mant = Label(self.frame1, text=mantimentos[1], background= cores[3])
        self.produto2_mant.configure(font= fontes[5])
        self.produto2_mant.place(anchor="center", relx= 0.74, rely= 0.362)
        
        self.produto3_mant = Label(self.frame1, text=mantimentos[2], background= cores[3])
        self.produto3_mant.configure(font= fontes[5])
        self.produto3_mant.place(anchor="center", relx= 0.74, rely= 0.424)
        
        self.produto4_mant = Label(self.frame1, text=mantimentos[3], background= cores[3])
        self.produto4_mant.configure(font= fontes[5])
        self.produto4_mant.place(anchor="center", relx= 0.74, rely= 0.486)
        
        self.produto5_mant = Label(self.frame1, text=mantimentos[4], background= cores[3])
        self.produto5_mant.configure(font= fontes[5])
        self.produto5_mant.place(anchor="center", relx= 0.74, rely= 0.548)
        
        self.produto6_mant = Label(self.frame1, text=mantimentos[5], background= cores[3])
        self.produto6_mant.configure(font= fontes[5])
        self.produto6_mant.place(anchor="center", relx= 0.74, rely= 0.61)
        
        self.produto7_mant = Label(self.frame1, text=mantimentos[6], background= cores[3])
        self.produto7_mant.configure(font= fontes[5])
        self.produto7_mant.place(anchor="center", relx= 0.74, rely= 0.672)
        
        self.produto8_mant = Label(self.frame1, text=mantimentos[7], background= cores[3])
        self.produto8_mant.configure(font= fontes[5])
        self.produto8_mant.place(anchor="center", relx= 0.74, rely= 0.734)
      

        #Label para valor do MANTIMENTOS
        self.valor_mant = Label(self.frame1, text= "Valor: R$00,00", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805)
        ##########################################################################


        #Label para valor TOTAL
        self.total = Label(self.frame1, text="Total: R$00,00", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88)

        #Label para valro NOTA
        self.nota = Label(self.frame1, text="Nota: 00000", background= cores[0])
        self.nota.configure(font= fontes[4])
        self.nota.place(anchor="center", relx= 0.5, rely=0.92)
        ##########################################################################


        #Label para data e hora atual
        self.datetime = Label(self.frame1, text= data, bg= cores[0])
        self.datetime.place(anchor='center', relx=0.8, rely=0.05)
        self.datetime.configure(font= fontes[3])

    def widgets(self):
        ##Botão para limpar seleção
        self.limpar = Button(self.frame1, image= bot[0], bg= cores[0], bd= 0, relief= FLAT)
        self.limpar.place(anchor= "center", relx= 0.2, rely= 0.88, relheight= 0.1, relwidth= 0.125)

        ##Botão para emitir Nota Fiscal
        self.emitir = Button(self.frame1, image= bot[1], bg= cores[0], bd= 0, relief= FLAT)
        self.emitir.place(anchor= "center", relx= 0.8, rely= 0.88, relheight= 0.1, relwidth= 0.125)
        
        ##########################################################################

        #Botões de Mais (+)
        self.mais1 = Button(self.frame1, text="+", background=cores[1])
        self.mais1.place(anchor="center", relx= 0.24, rely= 0.3, relheight=0.03, relwidth=0.016)
        
        self.mais2 = Button(self.frame1, text="+", background=cores[1])
        self.mais2.place(anchor="center", relx= 0.24, rely= 0.362, relheight=0.03, relwidth=0.016)
        
        self.mais3 = Button(self.frame1, text="+", background=cores[1])
        self.mais3.place(anchor="center", relx= 0.24, rely= 0.424, relheight=0.03, relwidth=0.016)
        
        self.mais4 = Button(self.frame1, text="+", background=cores[1])
        self.mais4.place(anchor="center", relx= 0.24, rely= 0.486, relheight=0.03, relwidth=0.016)
        
        self.mais5 = Button(self.frame1, text="+", background=cores[1])
        self.mais5.place(anchor="center", relx= 0.24, rely= 0.548, relheight=0.03, relwidth=0.016)
        
        self.mais6 = Button(self.frame1, text="+", background=cores[1])
        self.mais6.place(anchor="center", relx= 0.24, rely= 0.61, relheight=0.03, relwidth=0.016)
        
        self.mais7 = Button(self.frame1, text="+", background=cores[1])
        self.mais7.place(anchor="center", relx= 0.24, rely= 0.672, relheight=0.03, relwidth=0.016)
        
        self.mais8 = Button(self.frame1, text="+", background=cores[1])
        self.mais8.place(anchor="center", relx= 0.24, rely= 0.734, relheight=0.03, relwidth=0.016)


        
        self.mais9 = Button(self.frame1, text="+", background=cores[1])
        self.mais9.place(anchor="center", relx= 0.55, rely= 0.3, relheight=0.03, relwidth=0.016)
    
        self.mais10 = Button(self.frame1, text="+", background=cores[1])
        self.mais10.place(anchor="center", relx= 0.55, rely= 0.362, relheight=0.03, relwidth=0.016)
        
        self.mais11 = Button(self.frame1, text="+", background=cores[1])
        self.mais11.place(anchor="center", relx= 0.55, rely= 0.424, relheight=0.03, relwidth=0.016)
        
        self.mais12 = Button(self.frame1, text="+", background=cores[1])
        self.mais12.place(anchor="center", relx= 0.55, rely= 0.486, relheight=0.03, relwidth=0.016)
        
        self.mais13 = Button(self.frame1, text="+", background=cores[1])
        self.mais13.place(anchor="center", relx= 0.55, rely= 0.548, relheight=0.03, relwidth=0.016)
        
        self.mais14 = Button(self.frame1, text="+", background=cores[1])
        self.mais14.place(anchor="center", relx= 0.55, rely= 0.61, relheight=0.03, relwidth=0.016)
        
        self.mais15 = Button(self.frame1, text="+", background=cores[1])
        self.mais15.place(anchor="center", relx= 0.55, rely= 0.672, relheight=0.03, relwidth=0.016)
        
        self.mais16 = Button(self.frame1, text="+", background=cores[1])
        self.mais16.place(anchor="center", relx= 0.55, rely= 0.734, relheight=0.03, relwidth=0.016)


        
        self.mais17 = Button(self.frame1, text="+", background=cores[1])
        self.mais17.place(anchor="center", relx= 0.84, rely= 0.3, relheight=0.03, relwidth=0.016)
        
        self.mais18 = Button(self.frame1, text="+", background=cores[1])
        self.mais18.place(anchor="center", relx= 0.84, rely= 0.362, relheight=0.03, relwidth=0.016)
        
        self.mais19 = Button(self.frame1, text="+", background=cores[1])
        self.mais19.place(anchor="center", relx= 0.84, rely= 0.424, relheight=0.03, relwidth=0.016)
        
        self.mais20 = Button(self.frame1, text="+", background=cores[1])
        self.mais20.place(anchor="center", relx= 0.84, rely= 0.486, relheight=0.03, relwidth=0.016)
        
        self.mais21 = Button(self.frame1, text="+", background=cores[1])
        self.mais21.place(anchor="center", relx= 0.84, rely= 0.548, relheight=0.03, relwidth=0.016)
        
        self.mais22 = Button(self.frame1, text="+", background=cores[1])
        self.mais22.place(anchor="center", relx= 0.84, rely= 0.61, relheight=0.03, relwidth=0.016)
        
        self.mais23 = Button(self.frame1, text="+", background=cores[1])
        self.mais23.place(anchor="center", relx= 0.84, rely= 0.672, relheight=0.03, relwidth=0.016)
        
        self.mais24 = Button(self.frame1, text="+", background=cores[1])
        self.mais24.place(anchor="center", relx= 0.84, rely= 0.734, relheight=0.03, relwidth=0.016)

Application()