#modulo random
#A função random retorna um número float entre 0.0 e 1.0 (incluindo 0.0, mas não
#1.0). Todas as vezes que você chamar a função random, você receberá o próximo
#número de uma série longa. Para ver uma amostra, rode esse loop:

import random
for i in range(1000):
    x = random.random()
    print(x)

#Este programa produz a seguinte lista de 1000 números aleatórios entre 0.0 e até,
#mas não incluindo, 1.0.0.0
