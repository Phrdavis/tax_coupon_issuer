from modulos import *

root = tk.Tk()                                      #Definindo variavel para a janela root
get_dir = os.path.dirname(__file__)                 #Definindo variavel para diretorio do arquivo
data = datetime.now().strftime('%d/%m/%Y %H:%M')    #Definindo variavel para data e hora atuais
nota = ''



        ##########################################################################
            ###Variaveis auxiliares para quantidade e preço de produtos###

#primeira seção HORTIFRUTI quantidade
valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0
valor5 = 0
valor6 = 0
valor7 = 0
valor8 = 0

#primeira seção HOTIFRUTI preço
pre1 = [
    1.56,
    2.80,
    3.60,
    1.9,
    4.7,
    3.58,
    2.76,
    0.5
    ]

soma1 = 0

#segunda seção HIGIENE quantidade
valor9 = 0
valor10 = 0
valor11 = 0
valor12 = 0
valor13 = 0
valor14 = 0
valor15 = 0
valor16 = 0

#primeira seção HIGIENE preço
pre2 = [
    1.56,
    1.9,
    4.7,
    3.60,
    0.5,
    2.76,
    3.58,
    2.80
    ]

soma2 = 0

#terceira seção MANTIMENTOS quantidade
valor17 = 0
valor18 = 0
valor19 = 0
valor20 = 0
valor21 = 0
valor22 = 0
valor23 = 0
valor24 = 0

#primeira seção MANTIMENTOS preço
pre3 = [
    0.5,
    1.56,
    2.76,
    4.7,
    3.60,
    1.9,
    2.80,
    3.58
    ]

soma3 = 0

        ##########################################################################

#Soma total dos valores

soma_total = 0

