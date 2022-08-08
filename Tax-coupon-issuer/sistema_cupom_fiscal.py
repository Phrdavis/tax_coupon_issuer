from multiprocessing.connection import answer_challenge
from modulos import *                               #Importe da pasta Modulos

root = tk.Tk()                                      #Definindo variavel para a janela root
get_dir = os.path.dirname(__file__)                 #Definindo variavel para diretorio do arquivo
data = datetime.now().strftime('%d/%m/%Y %H:%M')    #Definindo variavel para data e hora atuais


                            ###Listas###
#Lista de Cores                           
cores = [
    "#f9f9f9",
    "#696969",
    "#c7d0d8",
    "#d9d9d9"
]

#Lista de Fontes
fonte1 = tkFont.Font(family="Arial", size=20, weight="bold", slant="italic")    #Definindo padrão de fonte
fonte1_1 = tkFont.Font(family="Arial", size=35, weight="bold")                  #Definindo padrão de fonte
fonte1_2 = tkFont.Font(family="Arial", size=20, weight="bold")                  #Definindo padrão de fonte
fonte1_3 = tkFont.Font(family="Arial", size=15, weight="bold")                  #Definindo padrão de fonte

fontes = [
    fonte1,     #fontes[0]
    fonte1_1,   #fontes[1]
    fonte1_2,    #fontes[2]
    fonte1_3    #fontes[3]
]

#Lista de blocos de fundo
bloco_info = PhotoImage(file= fr"{get_dir}\Blocos\bloco_info.png")
bloco_prod = PhotoImage(file= fr"{get_dir}\Blocos\bloco_prod.png")

bloco = [
    bloco_info, #bloco[0]
    bloco_prod  #bloco[1]
    ]

#lista de Botões
bot_limpar = PhotoImage(file= fr"{get_dir}\Botões\bt_limpar.png")
bot_emitir = PhotoImage(file= fr"{get_dir}\Botões\bt_emitir.png")

bot = [
    bot_limpar, #bot[0]
    bot_emitir  #bot[1]
]

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

        ##Label para o bloco de Hortifruti
        self.bloco_hort = Label(self.frame1, image= bloco[1], background= cores[0])
        self.bloco_hort.place(anchor="center", relx= 0.2, rely= 0.52)

        #Label para descrição: HORTIFRUTI
        self.hort = Label(self.frame1, text= "Hortifruti", background= cores[0])
        self.hort.configure(font= fontes[3])
        self.hort.place(anchor="center", relx= 0.2, rely=0.23)

        ##Label para o bloco de Higiene 
        self.bloco_hig = Label(self.frame1, image= bloco[1], background= cores[0])
        self.bloco_hig.place(anchor="center", relx= 0.5, rely= 0.52)

        #Label para descrição: HIGIENE
        self.hig = Label(self.frame1, text= "Higiene", background= cores[0])
        self.hig.configure(font= fontes[3])
        self.hig.place(anchor="center", relx= 0.5, rely=0.23)
        
        #Label para o bloco de Mantimentos 
        self.bloco_mant = Label(self.frame1, image= bloco[1], background= cores[0])
        self.bloco_mant.place(anchor="center", relx= 0.8, rely= 0.52)   

        #Label para descrição: MANTIMENTOS
        self.mant = Label(self.frame1, text= "Mantimentos", background= cores[0])
        self.mant.configure(font= fontes[3])
        self.mant.place(anchor="center", relx= 0.8, rely=0.23)

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
Application()