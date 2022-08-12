from modulos import *
from listas import *

class funcs(): 
        ##########################################################################
                            ###Função para geração da tela no meio###
    def center(self, win):
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
            ##########################################################################

                                ###Função para aumentar contador###

                                        ###Área de HORTIFRUTI

    def aumentar1(self):
        global valor1, pre1, soma1, soma_total
        valor1 += 1
        self.valor1_hortifruti = Label(self.frame1, text= valor1, background= cores[3])
        self.valor1_hortifruti.configure(font= fontes[5])
        self.valor1_hortifruti.place(anchor="center", relx= 0.26, rely=0.3)
        soma1 += pre1[0]
        
        self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

        soma_total += pre1[0]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar2(self):
        global valor2, pre1, soma1, soma_total
        valor2 += 1
        self.valor2_hortifruti = Label(self.frame1, text= valor2, background= cores[3])
        self.valor2_hortifruti.configure(font= fontes[5])
        self.valor2_hortifruti.place(anchor="center", relx= 0.26, rely=0.362)
        soma1 += pre1[1]
        
        self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

        soma_total += pre1[1]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar3(self):
        global valor3, pre1, soma1, soma_total
        valor3 += 1
        self.valor3_hortifruti = Label(self.frame1, text= valor3, background= cores[3])
        self.valor3_hortifruti.configure(font= fontes[5])
        self.valor3_hortifruti.place(anchor="center", relx= 0.26, rely=0.424)
        soma1 += pre1[2]   
        
        self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

        soma_total += pre1[2]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar4(self):
        global valor4, pre1, soma1, soma_total
        valor4 += 1
        self.valor4_hortifruti = Label(self.frame1, text= valor4, background= cores[3])
        self.valor4_hortifruti.configure(font= fontes[5])
        self.valor4_hortifruti.place(anchor="center", relx= 0.26, rely=0.486)
        soma1 += pre1[3]
        
        self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

        soma_total += pre1[3]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar5(self):
        global valor5, pre1, soma1, soma_total
        valor5 += 1
        self.valor5_hortifruti = Label(self.frame1, text= valor5, background= cores[3])
        self.valor5_hortifruti.configure(font= fontes[5])
        self.valor5_hortifruti.place(anchor="center", relx= 0.26, rely=0.548)
        soma1 += pre1[4]
        
        self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

        soma_total += pre1[4]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar6(self):
        global valor6, pre1, soma1, soma_total
        valor6 += 1
        self.valor6_hortifruti = Label(self.frame1, text= valor6, background= cores[3])
        self.valor6_hortifruti.configure(font= fontes[5])
        self.valor6_hortifruti.place(anchor="center", relx= 0.26, rely=0.61)
        soma1 += pre1[5]
        
        self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

        soma_total += pre1[5]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar7(self):
        global valor7, pre1, soma1, soma_total
        valor7 += 1
        self.valor7_hortifruti = Label(self.frame1, text= valor7, background= cores[3])
        self.valor7_hortifruti.configure(font= fontes[5])
        self.valor7_hortifruti.place(anchor="center", relx= 0.26, rely=0.672)
        soma1 += pre1[6]
        
        self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

        soma_total += pre1[6]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar8(self):
        global valor8, pre1, soma1, soma_total
        valor8 += 1
        self.valor8_hortifruti = Label(self.frame1, text= valor8, background= cores[3])
        self.valor8_hortifruti.configure(font= fontes[5])
        self.valor8_hortifruti.place(anchor="center", relx= 0.26, rely=0.734)
        soma1 += pre1[7]
        
        self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

        soma_total += pre1[7]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)
        ##########################################################################

                                    ###Área de HIGIENE
    def aumentar9(self):
        global valor9, pre2, soma2, soma_total
        valor9 += 1
        self.valor1_higiene = Label(self.frame1, text= valor9, background= cores[3])
        self.valor1_higiene.configure(font= fontes[5])
        self.valor1_higiene.place(anchor="center", relx= 0.57, rely=0.3)
        soma2 += pre2[0]

        self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

        soma_total += pre2[0]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar10(self):
        global valor10, pre2, soma2, soma_total
        valor10 += 1
        self.valor2_higiene = Label(self.frame1, text= valor10, background= cores[3])
        self.valor2_higiene.configure(font= fontes[5])
        self.valor2_higiene.place(anchor="center", relx= 0.57, rely=0.362)
        soma2 += pre2[1]

        self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

        soma_total += pre2[1]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar11(self):
        global valor11, pre2, soma2, soma_total
        valor11 += 1
        self.valor3_higiene = Label(self.frame1, text= valor11, background= cores[3])
        self.valor3_higiene.configure(font= fontes[5])
        self.valor3_higiene.place(anchor="center", relx= 0.57, rely=0.424)
        soma2 += pre2[2]

        self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

        soma_total += pre2[2]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar12(self):
        global valor12, pre2, soma2, soma_total
        valor12 += 1
        self.valor4_higiene = Label(self.frame1, text= valor12, background= cores[3])
        self.valor4_higiene.configure(font= fontes[5])
        self.valor4_higiene.place(anchor="center", relx= 0.57, rely=0.486)
        soma2 += pre2[3]

        self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

        soma_total += pre2[3]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar13(self):
        global valor13, pre2, soma2, soma_total
        valor13 += 1
        self.valor5_higiene = Label(self.frame1, text= valor13, background= cores[3])
        self.valor5_higiene.configure(font= fontes[5])
        self.valor5_higiene.place(anchor="center", relx= 0.57, rely=0.548)
        soma2 += pre2[4]

        self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

        soma_total += pre2[4]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar14(self):
        global valor14, pre2, soma2, soma_total
        valor14 += 1
        self.valor6_higiene = Label(self.frame1, text= valor14, background= cores[3])
        self.valor6_higiene.configure(font= fontes[5])
        self.valor6_higiene.place(anchor="center", relx= 0.57, rely=0.61)
        soma2 += pre2[5]

        self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

        soma_total += pre2[5]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar15(self):
        global valor15, pre2, soma2, soma_total
        valor15 += 1
        self.valor7_higiene = Label(self.frame1, text= valor15, background= cores[3])
        self.valor7_higiene.configure(font= fontes[5])
        self.valor7_higiene.place(anchor="center", relx= 0.57, rely=0.672)
        soma2 += pre2[6]

        self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

        soma_total += pre2[6]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar16(self):
        global valor16, pre2, soma2, soma_total
        valor16 += 1
        self.valor8_higiene = Label(self.frame1, text= valor16, background= cores[3])
        self.valor8_higiene.configure(font= fontes[5])
        self.valor8_higiene.place(anchor="center", relx= 0.57, rely=0.734)
        soma2 += pre2[7]

        self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

        soma_total += pre2[7]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

        ##########################################################################
        
                                    ###Área de MANTIMENTOS

    def aumentar17(self):
        global valor17, pre3, soma3, soma_total
        valor17 += 1
        self.valor1_mantimentos = Label(self.frame1, text= valor17, background= cores[3])
        self.valor1_mantimentos.configure(font= fontes[5])
        self.valor1_mantimentos.place(anchor="center", relx= 0.86, rely=0.3)
        soma3 += pre3[0]
        
        self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

        soma_total += pre3[0]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar18(self):
        global valor18, pre3, soma3, soma_total
        valor18 += 1
        self.valor2_mantimentos = Label(self.frame1, text= valor18, background= cores[3])
        self.valor2_mantimentos.configure(font= fontes[5])
        self.valor2_mantimentos.place(anchor="center", relx= 0.86, rely=0.362)
        soma3 += pre3[1]
        
        self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

        soma_total += pre3[1]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar19(self):
        global valor19, pre3, soma3, soma_total
        valor19 += 1
        self.valor3_mantimentos = Label(self.frame1, text= valor19, background= cores[3])
        self.valor3_mantimentos.configure(font= fontes[5])
        self.valor3_mantimentos.place(anchor="center", relx= 0.86, rely=0.424)
        soma3 += pre3[2]
        
        self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

        soma_total += pre3[2]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar20(self):
        global valor20, pre3, soma3, soma_total
        valor20 += 1
        self.valor4_mantimentos = Label(self.frame1, text= valor20, background= cores[3])
        self.valor4_mantimentos.configure(font= fontes[5])
        self.valor4_mantimentos.place(anchor="center", relx= 0.86, rely=0.486)
        soma3 += pre3[3]
        
        self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

        soma_total += pre3[3]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar21(self):
        global valor21, pre3, soma3, soma_total
        valor21 += 1
        self.valor5_mantimentos = Label(self.frame1, text= valor21, background= cores[3])
        self.valor5_mantimentos.configure(font= fontes[5])
        self.valor5_mantimentos.place(anchor="center", relx= 0.86, rely=0.548)
        soma3 += pre3[4]
        
        self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

        soma_total += pre3[4]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar22(self):
        global valor22, pre3, soma3, soma_total
        valor22 += 1
        self.valor6_mantimentos = Label(self.frame1, text= valor22, background= cores[3])
        self.valor6_mantimentos.configure(font= fontes[5])
        self.valor6_mantimentos.place(anchor="center", relx= 0.86, rely=0.61)
        soma3 += pre3[5]
        
        self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

        soma_total += pre3[5]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar23(self):
        global valor23, pre3, soma3, soma_total
        valor23 += 1
        self.valor7_mantimentos = Label(self.frame1, text= valor23, background= cores[3])
        self.valor7_mantimentos.configure(font= fontes[5])
        self.valor7_mantimentos.place(anchor="center", relx= 0.86, rely=0.672)
        soma3 += pre3[6]
        
        self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

        soma_total += pre3[6]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def aumentar24(self):
        global valor24, pre3, soma3, soma_total
        valor24 += 1
        self.valor8_mantimentos = Label(self.frame1, text= valor24, background= cores[3])
        self.valor8_mantimentos.place(anchor="center", relx= 0.86, rely=0.734)
        self.valor8_mantimentos.configure(font= fontes[5])
        soma3 += pre3[7]
        
        self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

        soma_total += pre3[7]

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)
            ##########################################################################

                                ###Função para diminuir contador###

                                        ###Área de HORTIFRUTI

    def diminuir1(self):
        global valor1, pre1, soma1, soma_total
        if valor1 > 0:
            valor1 -= 1
            self.valor1_hortifruti = Label(self.frame1, text= valor1, background= cores[3])
            self.valor1_hortifruti.configure(font= fontes[5])
            self.valor1_hortifruti.place(anchor="center", relx= 0.26, rely=0.3)
            soma1 -= pre1[0]
        
            self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
            self.valor_hort.configure(font= fontes[4])
            self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

            soma_total -= pre1[0]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir2(self):
        global valor2, pre1, soma1, soma_total
        if valor2 > 0:
            valor2 -= 1
            self.valor2_hortifruti = Label(self.frame1, text= valor2, background= cores[3])
            self.valor2_hortifruti.configure(font= fontes[5])
            self.valor2_hortifruti.place(anchor="center", relx= 0.26, rely=0.362)
            soma1 -= pre1[1]
        
            self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
            self.valor_hort.configure(font= fontes[4])
            self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

            soma_total -= pre1[1]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir3(self):
        global valor3, pre1, soma1, soma_total
        if valor3 > 0:
            valor3 -= 1
            self.valor3_hortifruti = Label(self.frame1, text= valor3, background= cores[3])
            self.valor3_hortifruti.configure(font= fontes[5])
            self.valor3_hortifruti.place(anchor="center", relx= 0.26, rely=0.424)
            soma1 -= pre1[2]
        
            self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
            self.valor_hort.configure(font= fontes[4])
            self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

            soma_total -= pre1[2]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir4(self):
        global valor4, pre1, soma1, soma_total
        if valor4 > 0:
            valor4 -= 1
            self.valor4_hortifruti = Label(self.frame1, text= valor4, background= cores[3])
            self.valor4_hortifruti.configure(font= fontes[5])
            self.valor4_hortifruti.place(anchor="center", relx= 0.26, rely=0.486)
            soma1 -= pre1[3]
        
            self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
            self.valor_hort.configure(font= fontes[4])
            self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

            soma_total -= pre1[3]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir5(self):
        global valor5, pre1, soma1, soma_total
        if valor5 > 0:
            valor5 -= 1
            self.valor5_hortifruti = Label(self.frame1, text= valor5, background= cores[3])
            self.valor5_hortifruti.configure(font= fontes[5])
            self.valor5_hortifruti.place(anchor="center", relx= 0.26, rely=0.548)
            soma1 -= pre1[4]
        
            self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
            self.valor_hort.configure(font= fontes[4])
            self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

            soma_total -= pre1[4]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir6(self):
        global valor6, pre1, soma1, soma_total
        if valor6 > 0:
            valor6 -= 1
            self.valor6_hortifruti = Label(self.frame1, text= valor6, background= cores[3])
            self.valor6_hortifruti.configure(font= fontes[5])
            self.valor6_hortifruti.place(anchor="center", relx= 0.26, rely=0.61)
            soma1 -= pre1[5]
        
            self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
            self.valor_hort.configure(font= fontes[4])
            self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

            soma_total -= pre1[5]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir7(self):
        global valor7, pre1, soma1, soma_total
        if valor7> 0:
            valor7-= 1
            self.valor7_hortifruti = Label(self.frame1, text= valor7, background= cores[3])
            self.valor7_hortifruti.configure(font= fontes[5])
            self.valor7_hortifruti.place(anchor="center", relx= 0.26, rely=0.672)
            soma1 -= pre1[6]
        
            self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
            self.valor_hort.configure(font= fontes[4])
            self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

            soma_total -= pre1[6]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir8(self):
        global valor8, pre1, soma1, soma_total
        if valor8> 0:
            valor8-= 1
            self.valor8_hortifruti = Label(self.frame1, text= valor8, background= cores[3])
            self.valor8_hortifruti.configure(font= fontes[5])
            self.valor8_hortifruti.place(anchor="center", relx= 0.26, rely=0.734)
            soma1 -= pre1[7]
        
            self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
            self.valor_hort.configure(font= fontes[4])
            self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)

            soma_total -= pre1[7]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)
        ##########################################################################

                            ###Área de HIGIENE
    def diminuir9(self):
        global valor9, pre2, soma2, soma_total
        if valor9> 0:
            valor9-= 1
            self.valor1_higiene = Label(self.frame1, text= valor9, background= cores[3])
            self.valor1_higiene.configure(font= fontes[5])
            self.valor1_higiene.place(anchor="center", relx= 0.57, rely=0.3)
            soma2 -= pre2[0]

            self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
            self.valor_hig.configure(font= fontes[4])
            self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

            soma_total -= pre2[0]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir10(self):
        global valor10, pre2, soma2, soma_total
        if valor10> 0:
            valor10-= 1
            self.valor2_higiene = Label(self.frame1, text= valor10, background= cores[3])
            self.valor2_higiene.configure(font= fontes[5])
            self.valor2_higiene.place(anchor="center", relx= 0.57, rely=0.362)
            soma2 -= pre2[1]

            self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
            self.valor_hig.configure(font= fontes[4])
            self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

            soma_total -= pre2[1]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir11(self):
        global valor11, pre2, soma2, soma_total
        if valor11> 0:
            valor11-= 1
            self.valor3_higiene = Label(self.frame1, text= valor11, background= cores[3])
            self.valor3_higiene.configure(font= fontes[5])
            self.valor3_higiene.place(anchor="center", relx= 0.57, rely=0.424)
            soma2 -= pre2[2]

            self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
            self.valor_hig.configure(font= fontes[4])
            self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

            soma_total -= pre2[2]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir12(self):
        global valor12, pre2, soma2, soma_total
        if valor12> 0:
            valor12-= 1
            self.valor4_higiene = Label(self.frame1, text= valor12, background= cores[3])
            self.valor4_higiene.configure(font= fontes[5])
            self.valor4_higiene.place(anchor="center", relx= 0.57, rely=0.486)
            soma2 -= pre2[3]

            self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
            self.valor_hig.configure(font= fontes[4])
            self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

            soma_total -= pre2[3]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir13(self):
        global valor13, pre2, soma2, soma_total
        if valor13> 0:
            valor13-= 1
            self.valor5_higiene = Label(self.frame1, text= valor13, background= cores[3])
            self.valor5_higiene.configure(font= fontes[5])
            self.valor5_higiene.place(anchor="center", relx= 0.57, rely=0.548)
            soma2 -= pre2[4]

            self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
            self.valor_hig.configure(font= fontes[4])
            self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

            soma_total -= pre2[4]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir14(self):
        global valor14, pre2, soma2, soma_total
        if valor14> 0:
            valor14-= 1
            self.valor6_higiene = Label(self.frame1, text= valor14, background= cores[3])
            self.valor6_higiene.configure(font= fontes[5])
            self.valor6_higiene.place(anchor="center", relx= 0.57, rely=0.61)
            soma2 -= pre2[5]

            self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
            self.valor_hig.configure(font= fontes[4])
            self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

            soma_total -= pre2[5]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir15(self):
        global valor15, pre2, soma2, soma_total
        if valor15> 0:
            valor15-= 1
            self.valor7_higiene = Label(self.frame1, text= valor15, background= cores[3])
            self.valor7_higiene.configure(font= fontes[5])
            self.valor7_higiene.place(anchor="center", relx= 0.57, rely=0.672)
            soma2 -= pre2[6]

            self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
            self.valor_hig.configure(font= fontes[4])
            self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

            soma_total -= pre2[6]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir16(self):
        global valor16, pre2, soma2, soma_total
        if valor16> 0:
            valor16-= 1
            self.valor8_higiene = Label(self.frame1, text= valor16, background= cores[3])
            self.valor8_higiene.configure(font= fontes[5])
            self.valor8_higiene.place(anchor="center", relx= 0.57, rely=0.734)
            soma2 -= pre2[7]

            self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
            self.valor_hig.configure(font= fontes[4])
            self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)

            soma_total -= pre2[7]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

        ##########################################################################
        
                            ###Área de MANTIMENTOS

    def diminuir17(self):
        global valor17, pre3, soma3, soma_total
        if valor17> 0:
            valor17-= 1
            self.valor1_mantimentos = Label(self.frame1, text= valor17, background= cores[3])
            self.valor1_mantimentos.configure(font= fontes[5])
            self.valor1_mantimentos.place(anchor="center", relx= 0.86, rely=0.3)
            soma3 -= pre3[0]
        
            self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
            self.valor_mant.configure(font= fontes[4])
            self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

            soma_total -= pre3[0]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir18(self):
        global valor18, pre3, soma3, soma_total
        if valor18> 0:
            valor18-= 1
            self.valor2_mantimentos = Label(self.frame1, text= valor18, background= cores[3])
            self.valor2_mantimentos.configure(font= fontes[5])
            self.valor2_mantimentos.place(anchor="center", relx= 0.86, rely=0.362)
            soma3 -= pre3[1]
        
            self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
            self.valor_mant.configure(font= fontes[4])
            self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

            soma_total -= pre3[1]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir19(self):
        global valor19, pre3, soma3, soma_total
        if valor19> 0:
            valor19-= 1
            self.valor3_mantimentos = Label(self.frame1, text= valor19, background= cores[3])
            self.valor3_mantimentos.configure(font= fontes[5])
            self.valor3_mantimentos.place(anchor="center", relx= 0.86, rely=0.424)
            soma3 -= pre3[2]
        
            self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
            self.valor_mant.configure(font= fontes[4])
            self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

            soma_total -= pre3[2]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir20(self):
        global valor20, pre3, soma3, soma_total
        if valor20> 0:
            valor20-= 1
            self.valor4_mantimentos = Label(self.frame1, text= valor20, background= cores[3])
            self.valor4_mantimentos.configure(font= fontes[5])
            self.valor4_mantimentos.place(anchor="center", relx= 0.86, rely=0.486)
            soma3 -= pre3[3]
        
            self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
            self.valor_mant.configure(font= fontes[4])
            self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

            soma_total -= pre3[3]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir21(self):
        global valor21, pre3, soma3, soma_total
        if valor21> 0:
            valor21-= 1
            self.valor5_mantimentos = Label(self.frame1, text= valor21, background= cores[3])
            self.valor5_mantimentos.configure(font= fontes[5])
            self.valor5_mantimentos.place(anchor="center", relx= 0.86, rely=0.548)
            soma3 -= pre3[4]
        
            self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
            self.valor_mant.configure(font= fontes[4])
            self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

            soma_total -= pre3[4]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir22(self):
        global valor22, pre3, soma3, soma_total
        if valor22> 0:
            valor22-= 1
            self.valor6_mantimentos = Label(self.frame1, text= valor22, background= cores[3])
            self.valor6_mantimentos.configure(font= fontes[5])
            self.valor6_mantimentos.place(anchor="center", relx= 0.86, rely=0.61)
            soma3 -= pre3[5]
        
            self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
            self.valor_mant.configure(font= fontes[4])
            self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

            soma_total -= pre3[5]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir23(self):
        global valor23, pre3, soma3, soma_total
        if valor23> 0:
            valor23-= 1
            self.valor7_mantimentos = Label(self.frame1, text= valor23, background= cores[3])
            self.valor7_mantimentos.configure(font= fontes[5])
            self.valor7_mantimentos.place(anchor="center", relx= 0.86, rely=0.672)
            soma3 -= pre3[6]
        
            self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
            self.valor_mant.configure(font= fontes[4])
            self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

            soma_total -= pre3[6]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def diminuir24(self):
        global valor24, pre3, soma3, soma_total
        if valor24> 0:
            valor24-= 1
            self.valor8_mantimentos = Label(self.frame1, text= valor24, background= cores[3])
            self.valor8_mantimentos.configure(font= fontes[5])
            self.valor8_mantimentos.place(anchor="center", relx= 0.86, rely=0.734)
            soma3 -= pre3[7]
        
            self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
            self.valor_mant.configure(font= fontes[4])
            self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

            soma_total -= pre3[7]

            #Label para valor TOTAL
            self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
            self.total.configure(font= fontes[2])
            self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)

    def limpar(self):
        global soma1, soma2, soma3, soma_total, valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8, valor9, valor10, valor11, valor12, valor13, valor14, valor15, valor16, valor17, valor18, valor19, valor20, valor21, valor22, valor23, valor24
        
        valor1 = 0
        valor2 = 0
        valor3 = 0
        valor4 = 0
        valor5 = 0
        valor6 = 0
        valor7 = 0
        valor8 = 0

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
        

        valor9 = 0
        valor10 = 0
        valor11 = 0
        valor12 = 0
        valor13 = 0
        valor14 = 0
        valor15 = 0
        valor16 = 0

        self.valor1_higiene = Label(self.frame1, text= valor9, background= cores[3])
        self.valor1_higiene.configure(font= fontes[5])
        self.valor1_higiene.place(anchor="center", relx= 0.57, rely=0.3)
        
        self.valor2_higiene = Label(self.frame1, text= valor10, background= cores[3])
        self.valor2_higiene.configure(font= fontes[5])
        self.valor2_higiene.place(anchor="center", relx= 0.57, rely=0.362)
        
        self.valor3_higiene = Label(self.frame1, text= valor11, background= cores[3])
        self.valor3_higiene.configure(font= fontes[5])
        self.valor3_higiene.place(anchor="center", relx= 0.57, rely=0.424)
        
        self.valor4_higiene = Label(self.frame1, text= valor12, background= cores[3])
        self.valor4_higiene.configure(font= fontes[5])
        self.valor4_higiene.place(anchor="center", relx= 0.57, rely=0.486)
        
        self.valor5_higiene = Label(self.frame1, text= valor13, background= cores[3])
        self.valor5_higiene.configure(font= fontes[5])
        self.valor5_higiene.place(anchor="center", relx= 0.57, rely=0.548)
        
        self.valor6_higiene = Label(self.frame1, text= valor14, background= cores[3])
        self.valor6_higiene.configure(font= fontes[5])
        self.valor6_higiene.place(anchor="center", relx= 0.57, rely=0.61)
        
        self.valor7_higiene = Label(self.frame1, text= valor15, background= cores[3])
        self.valor7_higiene.configure(font= fontes[5])
        self.valor7_higiene.place(anchor="center", relx= 0.57, rely=0.672)
        
        self.valor8_higiene = Label(self.frame1, text= valor16, background= cores[3])
        self.valor8_higiene.configure(font= fontes[5])
        self.valor8_higiene.place(anchor="center", relx= 0.57, rely=0.734)
    

        valor17 = 0
        valor18 = 0
        valor19 = 0
        valor20 = 0
        valor21 = 0
        valor22 = 0
        valor23 = 0
        valor24 = 0

        self.valor1_mantimentos = Label(self.frame1, text= valor17, background= cores[3])
        self.valor1_mantimentos.configure(font= fontes[5])
        self.valor1_mantimentos.place(anchor="center", relx= 0.86, rely=0.3)
        
        self.valor2_mantimentos = Label(self.frame1, text= valor18, background= cores[3])
        self.valor2_mantimentos.configure(font= fontes[5])
        self.valor2_mantimentos.place(anchor="center", relx= 0.86, rely=0.362)
        
        self.valor3_mantimentos = Label(self.frame1, text= valor19, background= cores[3])
        self.valor3_mantimentos.configure(font= fontes[5])
        self.valor3_mantimentos.place(anchor="center", relx= 0.86, rely=0.424)
        
        self.valor4_mantimentos = Label(self.frame1, text= valor20, background= cores[3])
        self.valor4_mantimentos.configure(font= fontes[5])
        self.valor4_mantimentos.place(anchor="center", relx= 0.86, rely=0.486)
        
        self.valor5_mantimentos = Label(self.frame1, text= valor21, background= cores[3])
        self.valor5_mantimentos.configure(font= fontes[5])
        self.valor5_mantimentos.place(anchor="center", relx= 0.86, rely=0.548)
        
        self.valor6_mantimentos = Label(self.frame1, text= valor22, background= cores[3])
        self.valor6_mantimentos.configure(font= fontes[5])
        self.valor6_mantimentos.place(anchor="center", relx= 0.86, rely=0.61)
        
        self.valor7_mantimentos = Label(self.frame1, text= valor23, background= cores[3])
        self.valor7_mantimentos.configure(font= fontes[5])
        self.valor7_mantimentos.place(anchor="center", relx= 0.86, rely=0.672)
        
        self.valor8_mantimentos = Label(self.frame1, text= valor24, background= cores[3])
        self.valor8_mantimentos.place(anchor="center", relx= 0.86, rely=0.734)
        self.valor8_mantimentos.configure(font= fontes[5])
        
        
            
        soma1 = 0
        soma2 = 0
        soma3 = 0
        soma_total = 0
        
        self.valor_hort = Label(self.frame1, text= f"Valor: R${soma1:.2f}", background= cores[0])
        self.valor_hort.configure(font= fontes[4])
        self.valor_hort.place(anchor="center", relx= 0.2, rely=0.805, relwidth=0.1)
        
        self.valor_hig = Label(self.frame1, text= f"Valor: R${soma2:.2f}", background= cores[0])
        self.valor_hig.configure(font= fontes[4])
        self.valor_hig.place(anchor="center", relx= 0.5, rely=0.805, relwidth= 0.1)
    
        self.valor_mant = Label(self.frame1, text= f"Valor: R${soma3:.2f}", background= cores[0])
        self.valor_mant.configure(font= fontes[4])
        self.valor_mant.place(anchor="center", relx= 0.8, rely=0.805, relwidth= 0.1)

        #Label para valor TOTAL
        self.total = Label(self.frame1, text=f"Total: R${soma_total:.2f}", background= cores[0])
        self.total.configure(font= fontes[2])
        self.total.place(anchor="center", relx= 0.5, rely=0.88, relwidth=0.2)