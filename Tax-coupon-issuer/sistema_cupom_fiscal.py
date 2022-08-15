from modulos import *                               #Importe da pasta Modulos
from funcs import *
from listas import *
from parametros import *

                            ###Classe principal para formação e configuração da tela###
class Application(funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.label()
        self.entrys()
        self.widgets()
        root.mainloop()
    def tela(self):
        root.title("Gerador de Nota Fiscal")
        root.geometry("1366x743")
        root.configure(background= cores[1])
        root.resizable(False, False)

        
        self.center(self.root)

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



        #Labels de numeros para primeira seção
        self.valor1_hortifruti = Label(self.frame1, text= valor1, background= cores[3])
        self.valor1_hortifruti.configure(font= fontes[5])
        self.valor1_hortifruti.place(anchor="center", relx= 0.26, rely=0.3)

        self.valor2_hortifruti = Label(self.frame1, text= valor2, background= cores[3])
        self.valor2_hortifruti.configure(font= fontes[5])
        self.valor2_hortifruti.place(anchor="center", relx= 0.26, rely=0.362)

        self.valor3_hortifruti = Label(self.frame1, text= valor3, background= cores[3])
        self.valor3_hortifruti.configure(font= fontes[5])
        self.valor3_hortifruti.place(anchor="center", relx= 0.26, rely=0.424)

        self.valor4_hortifruti = Label(self.frame1, text= valor4, background= cores[3])
        self.valor4_hortifruti.configure(font= fontes[5])
        self.valor4_hortifruti.place(anchor="center", relx= 0.26, rely=0.486)

        self.valor5_hortifruti = Label(self.frame1, text= valor5, background= cores[3])
        self.valor5_hortifruti.configure(font= fontes[5])
        self.valor5_hortifruti.place(anchor="center", relx= 0.26, rely=0.548)

        self.valor6_hortifruti = Label(self.frame1, text= valor6, background= cores[3])
        self.valor6_hortifruti.configure(font= fontes[5])
        self.valor6_hortifruti.place(anchor="center", relx= 0.26, rely=0.61)

        self.valor7_hortifruti = Label(self.frame1, text= valor7, background= cores[3])
        self.valor7_hortifruti.configure(font= fontes[5])
        self.valor7_hortifruti.place(anchor="center", relx= 0.26, rely=0.672)

        self.valor8_hortifruti = Label(self.frame1, text= valor8, background= cores[3])
        self.valor8_hortifruti.configure(font= fontes[5])
        self.valor8_hortifruti.place(anchor="center", relx= 0.26, rely=0.734)
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


        #Labels de numeros para segunda seção
        self.valor1_higiene = Label(self.frame1, text= valor1, background= cores[3])
        self.valor1_higiene.configure(font= fontes[5])
        self.valor1_higiene.place(anchor="center", relx= 0.57, rely=0.3)

        self.valor2_higiene = Label(self.frame1, text= valor2, background= cores[3])
        self.valor2_higiene.configure(font= fontes[5])
        self.valor2_higiene.place(anchor="center", relx= 0.57, rely=0.362)

        self.valor3_higiene = Label(self.frame1, text= valor3, background= cores[3])
        self.valor3_higiene.configure(font= fontes[5])
        self.valor3_higiene.place(anchor="center", relx= 0.57, rely=0.424)

        self.valor4_higiene = Label(self.frame1, text= valor4, background= cores[3])
        self.valor4_higiene.configure(font= fontes[5])
        self.valor4_higiene.place(anchor="center", relx= 0.57, rely=0.486)

        self.valor5_higiene = Label(self.frame1, text= valor5, background= cores[3])
        self.valor5_higiene.configure(font= fontes[5])
        self.valor5_higiene.place(anchor="center", relx= 0.57, rely=0.548)

        self.valor6_higiene = Label(self.frame1, text= valor6, background= cores[3])
        self.valor6_higiene.configure(font= fontes[5])
        self.valor6_higiene.place(anchor="center", relx= 0.57, rely=0.61)

        self.valor7_higiene = Label(self.frame1, text= valor7, background= cores[3])
        self.valor7_higiene.configure(font= fontes[5])
        self.valor7_higiene.place(anchor="center", relx= 0.57, rely=0.672)

        self.valor8_higiene = Label(self.frame1, text= valor8, background= cores[3])
        self.valor8_higiene.configure(font= fontes[5])
        self.valor8_higiene.place(anchor="center", relx= 0.57, rely=0.734)
        ##########################################################################
        
                            ###Área de MANTIMENTOS
        #Label para o bloco de Mantimentos 
        self.bloco_mant = Label(self.frame1, image= bloco[1], background= cores[0])
        self.bloco_mant.place(anchor="center", relx= 0.8, rely= 0.52)   

        #Label para descrição: MANTIMENTOS
        self.mant = Label(self.frame1, text= "Mantimentos", background= cores[0])
        self.mant.configure(font= fontes[3])
        self.mant.place(anchor="center", relx= 0.8, rely=0.23)

        #Label para produtos mantimentos 
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
        
    
         #Labels de numeros para terceira seção
        self.valor1_mantimentos = Label(self.frame1, text= 0, background= cores[3])
        self.valor1_mantimentos.configure(font= fontes[5])
        self.valor1_mantimentos.place(anchor="center", relx=0.86, rely=0.3)

        self.valor2_mantimentos = Label(self.frame1, text= 0, background= cores[3])
        self.valor2_mantimentos.configure(font= fontes[5])
        self.valor2_mantimentos.place(anchor="center", relx= 0.86, rely=0.362)

        self.valor3_mantimentos = Label(self.frame1, text= 0, background= cores[3])
        self.valor3_mantimentos.configure(font= fontes[5])
        self.valor3_mantimentos.place(anchor="center", relx= 0.86, rely=0.424)

        self.valor4_mantimentos = Label(self.frame1, text= 0, background= cores[3])
        self.valor4_mantimentos.configure(font= fontes[5])
        self.valor4_mantimentos.place(anchor="center", relx= 0.86, rely=0.486)

        self.valor5_mantimentos = Label(self.frame1, text= 0, background= cores[3])
        self.valor5_mantimentos.configure(font= fontes[5])
        self.valor5_mantimentos.place(anchor="center", relx= 0.86, rely=0.548)

        self.valor6_mantimentos = Label(self.frame1, text= 0, background= cores[3])
        self.valor6_mantimentos.configure(font= fontes[5])
        self.valor6_mantimentos.place(anchor="center", relx= 0.86, rely=0.61)

        self.valor7_mantimentos = Label(self.frame1, text= 0, background= cores[3])
        self.valor7_mantimentos.configure(font= fontes[5])
        self.valor7_mantimentos.place(anchor="center", relx= 0.86, rely=0.672)

        self.valor8_mantimentos = Label(self.frame1, text= 0, background= cores[3])
        self.valor8_mantimentos.configure(font= fontes[5])
        self.valor8_mantimentos.place(anchor="center", relx= 0.86, rely=0.734)

        ##########################################################################

        #Label para valor TOTAL
        self.total = Label(self.frame1, text="Total: R$00,00", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.90)

        ##########################################################################

        #Label para data e hora atual
        self.datetime = Label(self.frame1, text= data, bg= cores[0])
        self.datetime.place(anchor='center', relx=0.8, rely=0.05)
        self.datetime.configure(font= fontes[3])
    
    def entrys(self):
        #Entry para cadastro de nome
        self.nome_entry = Entry(self.frame1, bd= 0, bg= cores[2])
        self.nome_entry.configure(font= fontes[5])
        self.nome_entry.place(anchor='center', relx = 0.22, rely= 0.129, relwidth= 0.18)

        ##########################################################################
        #Entry para cadastro de CPF
        self.cpf_entry = Entry(self.frame1, bd= 0, bg= cores[2])
        self.cpf_entry.configure(font= fontes[5])
        self.cpf_entry.place(anchor='center', relx = 0.52, rely= 0.129, relwidth= 0.18)

        ##########################################################################'
        #Entry para cadastro de Telefone
        self.telefone_entry = Entry(self.frame1, bd= 0, bg= cores[2])
        self.telefone_entry.configure(font= fontes[5])
        self.telefone_entry.place(anchor='center', relx = 0.84, rely= 0.129, relwidth= 0.18)


    def widgets(self):
        ##Botão para limpar seleção
        self.bt_limpar = Button(self.frame1, image= bot[0], bg= cores[0], bd= 0, relief= FLAT, command= self.limpar)
        self.bt_limpar.place(anchor= "center", relx= 0.2, rely= 0.88, relheight= 0.1, relwidth= 0.125)

        ##Botão para emitir Nota Fiscal
        self.bt_emitir = Button(self.frame1, image= bot[1], bg= cores[0], bd= 0, relief= FLAT, command= self.gerar_pdf)
        self.bt_emitir.place(anchor= "center", relx= 0.8, rely= 0.88, relheight= 0.1, relwidth= 0.125)
        
        ##########################################################################

                                    #Botões de Mais (+)
        #Botões da primeira seção
        self.mais1 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar1)
        self.mais1.place(anchor="center", relx= 0.24, rely= 0.3, relheight=0.03, relwidth=0.016)
        
        self.mais2 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar2)
        self.mais2.place(anchor="center", relx= 0.24, rely= 0.362, relheight=0.03, relwidth=0.016)
        
        self.mais3 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar3)
        self.mais3.place(anchor="center", relx= 0.24, rely= 0.424, relheight=0.03, relwidth=0.016)
        
        self.mais4 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar4)
        self.mais4.place(anchor="center", relx= 0.24, rely= 0.486, relheight=0.03, relwidth=0.016)
        
        self.mais5 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar5)
        self.mais5.place(anchor="center", relx= 0.24, rely= 0.548, relheight=0.03, relwidth=0.016)
        
        self.mais6 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar6)
        self.mais6.place(anchor="center", relx= 0.24, rely= 0.61, relheight=0.03, relwidth=0.016)
        
        self.mais7 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar7)
        self.mais7.place(anchor="center", relx= 0.24, rely= 0.672, relheight=0.03, relwidth=0.016)
        
        self.mais8 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar8)
        self.mais8.place(anchor="center", relx= 0.24, rely= 0.734, relheight=0.03, relwidth=0.016)


        #Botões da segunda seção
        self.mais9 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar9)
        self.mais9.place(anchor="center", relx= 0.55, rely= 0.3, relheight=0.03, relwidth=0.016)
    
        self.mais10 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar10)
        self.mais10.place(anchor="center", relx= 0.55, rely= 0.362, relheight=0.03, relwidth=0.016)
        
        self.mais11 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar11)
        self.mais11.place(anchor="center", relx= 0.55, rely= 0.424, relheight=0.03, relwidth=0.016)
        
        self.mais12 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar12)
        self.mais12.place(anchor="center", relx= 0.55, rely= 0.486, relheight=0.03, relwidth=0.016)
        
        self.mais13 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar13)
        self.mais13.place(anchor="center", relx= 0.55, rely= 0.548, relheight=0.03, relwidth=0.016)
        
        self.mais14 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar14)
        self.mais14.place(anchor="center", relx= 0.55, rely= 0.61, relheight=0.03, relwidth=0.016)
        
        self.mais15 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar15)
        self.mais15.place(anchor="center", relx= 0.55, rely= 0.672, relheight=0.03, relwidth=0.016)
        
        self.mais16 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar16)
        self.mais16.place(anchor="center", relx= 0.55, rely= 0.734, relheight=0.03, relwidth=0.016)


        #Botões da terceira seção
        self.mais17 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar17)
        self.mais17.place(anchor="center", relx= 0.84, rely= 0.3, relheight=0.03, relwidth=0.016)
        
        self.mais18 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar18)
        self.mais18.place(anchor="center", relx= 0.84, rely= 0.362, relheight=0.03, relwidth=0.016)
        
        self.mais19 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar19)
        self.mais19.place(anchor="center", relx= 0.84, rely= 0.424, relheight=0.03, relwidth=0.016)
        
        self.mais20 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar20)
        self.mais20.place(anchor="center", relx= 0.84, rely= 0.486, relheight=0.03, relwidth=0.016)
        
        self.mais21 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar21)
        self.mais21.place(anchor="center", relx= 0.84, rely= 0.548, relheight=0.03, relwidth=0.016)
        
        self.mais22 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar22)
        self.mais22.place(anchor="center", relx= 0.84, rely= 0.61, relheight=0.03, relwidth=0.016)
        
        self.mais23 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar23)
        self.mais23.place(anchor="center", relx= 0.84, rely= 0.672, relheight=0.03, relwidth=0.016)
        
        self.mais24 = Button(self.frame1, text="+", background=cores[1], command= self.aumentar24)
        self.mais24.place(anchor="center", relx= 0.84, rely= 0.734, relheight=0.03, relwidth=0.016)
        
        ##########################################################################

                                    #Botões de Mais (-)
        #Botões da primeira seção
        self.menos1 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir1)
        self.menos1.place(anchor="center", relx= 0.28, rely= 0.3, relheight=0.03, relwidth=0.016)
        
        self.menos2 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir2)
        self.menos2.place(anchor="center", relx= 0.28, rely= 0.362, relheight=0.03, relwidth=0.016)
        
        self.menos3 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir3)
        self.menos3.place(anchor="center", relx= 0.28, rely= 0.424, relheight=0.03, relwidth=0.016)
        
        self.menos4 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir4)
        self.menos4.place(anchor="center", relx= 0.28, rely= 0.486, relheight=0.03, relwidth=0.016)
        
        self.menos5 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir5)
        self.menos5.place(anchor="center", relx= 0.28, rely= 0.548, relheight=0.03, relwidth=0.016)
        
        self.menos6 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir6)
        self.menos6.place(anchor="center", relx= 0.28, rely= 0.61, relheight=0.03, relwidth=0.016)
        
        self.menos7 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir7)
        self.menos7.place(anchor="center", relx= 0.28, rely= 0.672, relheight=0.03, relwidth=0.016)
        
        self.menos8 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir8)
        self.menos8.place(anchor="center", relx= 0.28, rely= 0.734, relheight=0.03, relwidth=0.016)


        #Botões da segunda seção
        self.menos9 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir9)
        self.menos9.place(anchor="center", relx= 0.59, rely= 0.3, relheight=0.03, relwidth=0.016)
    
        self.menos10 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir10)
        self.menos10.place(anchor="center", relx= 0.59, rely= 0.362, relheight=0.03, relwidth=0.016)
        
        self.menos11 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir11)
        self.menos11.place(anchor="center", relx= 0.59, rely= 0.424, relheight=0.03, relwidth=0.016)
        
        self.menos12 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir12)
        self.menos12.place(anchor="center", relx= 0.59, rely= 0.486, relheight=0.03, relwidth=0.016)
        
        self.menos13 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir13)
        self.menos13.place(anchor="center", relx= 0.59, rely= 0.548, relheight=0.03, relwidth=0.016)
        
        self.menos14 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir14)
        self.menos14.place(anchor="center", relx= 0.59, rely= 0.61, relheight=0.03, relwidth=0.016)
        
        self.menos15 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir15)
        self.menos15.place(anchor="center", relx= 0.59, rely= 0.672, relheight=0.03, relwidth=0.016)
        
        self.menos16 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir16)
        self.menos16.place(anchor="center", relx= 0.59, rely= 0.734, relheight=0.03, relwidth=0.016)


        #Botões da terceira seção
        self.menos17 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir17)
        self.menos17.place(anchor="center", relx= 0.88, rely= 0.3, relheight=0.03, relwidth=0.016)
        
        self.menos18 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir18)
        self.menos18.place(anchor="center", relx= 0.88, rely= 0.362, relheight=0.03, relwidth=0.016)
        
        self.menos19 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir19)
        self.menos19.place(anchor="center", relx= 0.88, rely= 0.424, relheight=0.03, relwidth=0.016)
        
        self.menos20 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir20)
        self.menos20.place(anchor="center", relx= 0.88, rely= 0.486, relheight=0.03, relwidth=0.016)
        
        self.menos21 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir21)
        self.menos21.place(anchor="center", relx= 0.88, rely= 0.548, relheight=0.03, relwidth=0.016)
        
        self.menos22 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir22)
        self.menos22.place(anchor="center", relx= 0.88, rely= 0.61, relheight=0.03, relwidth=0.016)
        
        self.menos23 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir23)
        self.menos23.place(anchor="center", relx= 0.88, rely= 0.672, relheight=0.03, relwidth=0.016)
        
        self.menos24 = Button(self.frame1, text="-", background=cores[1], command= self.diminuir24)
        self.menos24.place(anchor="center", relx= 0.88, rely= 0.734, relheight=0.03, relwidth=0.016)


Application()