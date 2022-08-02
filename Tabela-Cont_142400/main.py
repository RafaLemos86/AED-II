from student import *
from tabela import *

# TESTES DOS METODOS, PERCEBA QUE HÁ FUNCOES EM QUE CHAMA A BUSCA LINEAR E BINARIA (CONSULT), SEM
# CONFILTIO DE RETORNOS

tabela = Table(5)

student1 = Student(1234, "Rafael", 20, "Sistemas de Informação")
student2 = Student(1574, "Joao", 24, "Engenharia de Alimentos")
student3 = Student(7869, "Andressa", 19, "Administracao")
student4 = Student(2536, "Maria", 29, "Historia")
student5 = Student(5847, "Fabio", 34, "Matematica")
student6 = Student(8969, "Bruna", 22, "Sistemas de Informação")

# INSERCAO ORDENADA
tabela.order_insert(student1.get_id(), student1)
tabela.order_insert(student2.get_id(), student2)
tabela.order_insert(student3.get_id(), student3)
tabela.order_insert(student4.get_id(), student4)
tabela.order_insert(student5.get_id(), student5)
tabela.order_insert(student6.get_id(), student6)
print(tabela)

# # REMOÇOES E TROCAS DE VALORES NAS CHAVES
tabela.remove(1574)
tabela.remove(5847)
tabela.order_insert(student6.get_id(), student6)
tabela.order_insert(7869, "name: Andressa age: 20 course: Marketing")
print(tabela)

# # # CONSULTAS DO VALOR A PARTIR DA CHAVE
print(tabela.consult(2536))
print(tabela.consult(1234))

# DESTRUIR VETOR
tabela.clean_vector()
print(tabela.size())
