#integrar a funcionalidade de encontrar delta e x1 e x2 de uma bhaskara no programa
quest =0
import math
e = 0
maior = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
while True:
    print('=' * 15, '[MENU INICIAL]', '=' * 15)
    print('[1] Análise de Dados\n'
          '[2] Cálculo da Área\n'
          '[3] Bhaskara\n'
          '[4] Sair do programa')
    quest = int(input('Digite o número da funcionalidade que desejar: '))
    if quest == 1:
        print('=' * 15, '[MENU DE ANÁLISE DE DADOS]', '=' * 15)
        print('[1] Somar\n'
                  '[2] Multiplicar\n'
                  '[3] Subtração (Maior pelo Menor)\n'
                  '[4] Média\n'
                  '[5] Maior número e menor número\n'
                  '[6] Divisão (Maior/Menor)\n'
                  '[7] Fatorial\n'
                  '[8] Raiz Quadrada\n'
                  '[9] Elevado ao Quadrado/Cubo\n'
                  '[10] Tabuada\n'
                f'[11] Converter para Radiano\n'
                  '[12] Seno/Cosseno/Tangente\n'
                  '[13] Calcular Hipotenusa\n'
                  '[14] Fibonacci\n'
                f'[15] Converter Celsius para Fahrenheit\n' 
                  '[16] Mais informações\n'
                  '[17] Sair do programa')
        print()
        e = int(input('Qual operação matemática deseja fazer? '))
        print()
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print(f'Sua escolha: {e}\n-----------RESULTADO-----------')
        if e == 1:
            print(f'A soma entre {n1} e {n2} é igual a: {n1 + n2}')
            print()
        elif e == 2:
            print(f'A multiplicação entre {n1} e {n2} é igual a: {n1 * n2}')
            print()
        elif e == 3:
            if n1 > n2:
                print(f'{n1} subtraído por {n2} é igual a: {n1 - n2}')
            elif n2 > n1:
                print(f'{n2} subtraído por {n1} é igual a: {n2 - n1}')
            elif n1 == n2:
                print(f'O resultado é igual a 0.')
            print()
        elif e == 4:
            print(f'A média entre {n1} e {n2} é igual a: {(n1 + n2) / 2}')
            print()
        elif e == 5:
            if n1 > n2:
                maior = n1
                menor = n2
            elif n2 > n1:
                maior = n2
                menor = n1
            print(f'O maior número: {maior}\nO menor número: {menor}')
            print()
        elif e == 6:
            if n1 > n2:
                print(f'{n1} dividido por {n2} é igual a: {n1 / n2}')
                print()
            elif n2 > n1:
                print(f'{n2} dividido por {n1} é igual a: {n2 / n1}')
                print()
        elif e == 7:
            print(f'Fatorial de {n1} -> {math.factorial(n1)}')
            print(f'Fatorial de {n2} -> {math.factorial(n2)}')
            print()
        elif e == 8:
            print(f'Raiz Quadrada de {n1} -> {math.sqrt(n1)}')
            print(f'Raiz Quadrada de {n2} -> {math.sqrt(n2)}')
            print()
        elif e == 9:
            print(f'{n1}² -> {n1 * n1} // {n1}³ -> {n1 * n1 * n1}')
            print(f'{n2}² -> {n2 * n2} // {n2}³ -> {n2 * n2 * n2}')
            print()
        elif e == 10:
            for c in range(11):
                print(f'{n1} x {c} = {n1 * c}')
            print('=' * 25)
            for c in range(11):
                print(f'{n2} x {c} = {n2 * c}')
            print()
        elif e == 11:
            print(f'{n1}° para radianos -> {math.radians(n1):.6f}')
            print(f'{n2}° para radianos -> {math.radians(n2):.6f}')
            print()
        elif e == 12:
            print(
                f'Cosseno de {n1}: {math.cos(n1):.10f}\nSeno de {n1}: {math.sin(n1):.10f}\nTangente de {n1}: {math.tan(n1):.10f}')
            print('=' * 25)
            print(
                f'Cosseno de {n2}: {math.cos(n1):.10f}\nSeno de {n2}: {math.sin(n2):.10f}\nTangente de {n2}: {math.tan(n2):.10f}')
            print()
        elif e == 13:
            print(
                f'Considerando {n1} como cateto oposto e {n2} como cateto adjacente, a hipotenusa é igual a: {math.sqrt(n1 ** 2 + n2 ** 2):.10f}')
            print()
        elif e == 14:
            a = 0
            b = 1
            print(f'Os {n1} primeiros termos da sequência de Fibonacci: {a}, {b}', end=' ')
            contador = 1
            while contador <= n1 - 2:
                c = a + b
                a = b
                b = c
                print(f', {c}', end=' ')
                contador += 1
            print()
            a = 0
            b = 1
            print(f'Os {n2} primeiros termos da sequência de Fibonacci: {a}, {b}', end=' ')
            contador = 1
            while contador <= n2 - 2:
                c = a + b
                a = b
                b = c
                print(f', {c}', end=' ')
                contador += 1
            print()
            print()
        elif e == 15:
            print(f'{n1}°C para Fahrenheit é igual a: {n1 * 1.8 + 32}°F')
            print(f'{n2}°C para Fahrenheit é igual a: {n2 * 1.8 + 32}°F')
            print()
        elif e == 16:
            contador = 0
            for c in range(1, n1 + 1):
                if n1 % c == 0:
                    contador += 1
                else:
                    continue
            if contador == 2:
                print(f'{n1} é Número Primo? ✅')
            else:
                print(f'{n1} é Número Primo? ❌')
            contador = 0
            for c in range(1, n2 + 1):
                if n2 % c == 0:
                    contador += 1
                else:
                    continue
            if contador == 2:
                print(f'{n2} é Número Primo? ✅')
            else:
                print(f'{n2} é Número Primo? ❌')
            print()

            if n1 % 2 == 0:
                print(f'{n1} é Par? ✅ / {n1} é Ímpar? ❌')
            else:
                print(f'{n1} é Par? ❌ / {n1} é Ímpar? ✅')

            if n1 % 2 == 0:
                print(f'{n2} é Par? ✅ / {n2} é Ímpar? ❌')
            else:
                print(f'{n2} é Par? ❌ / {n2} é Ímpar? ✅')
            print()
        elif e == 17:
            break
            print(f'Programa encerrado.')
        elif e > 17 or e <= 0:
            print('Por favor, escolha entre as opções 1 a 17 somente.')
            print('Programa reiniciado.')
            print()
    elif quest == 2:
        print('=' * 15, '[MENU DO CÁLCULO DA ÁREA]', '=' * 15)
        print('[1] Triângulo\n'
              '[2] Quadrado\n'
              '[3] Retângulo\n'
              '[4] Trapézio\n'
              '[5] Círculo\n'
              '[6] Losango\n'
              '[7] Sair do Programa'
              )
        print()
        quest = int(input('Escolha a figura plana que deseja calcular a área: '))
        print(f'Sua escolha: {quest}')
        print()
        if quest == 1:
            n1 = int(input('Digite o valor da base: '))
            n2 = int(input('Digite o valor da altura: '))
            n3 = int(input('Digite o valor do primeiro lado do Triângulo (m): '))
            n4 = int(input('Digite o valor do segundo lado do Triângulo (m): '))
            n5 = int(input('Digite o valor do terceiro lado do Triângulo (m): '))
            val = [n3, n4, n5]
            val.sort()
            soma = val[0] + val[1]
            if n1 in val:
                if soma > n5:
                    print()
                    print('Triângulo válido')
                    if n3 == n4 and n4 == n5:
                        print('Triângulo Equilátero.')
                    elif n3 == n4 or n3 == n5 or n4 == n5:
                        print('Triângulo Isósceles.')
                    else:
                        print('Triângulo Escaleno.')
                    print()
                    print(f'A área do Triângulo, é igual a: Base X Altura/2')
                    print(f'Desta forma, a área do Triângulo é igual a: {(n1 * n2) / 2}')
                    print()
                else:
                    print('Triângulo inválido.')
            else:
                print()
                print('Triângulo inválido.')
                print()
        elif quest == 2:
            n1 = int(input('Digite o lado do quadrado (m): '))
            print()
            print('A área do Quadrado é igual a: Lado²')
            print(f'Desta forma, a área do Quadrado é igual a: {n1 ** 2}')
            print()
        elif quest == 3:
            n1 = int(input('Digite o valor da base do Retângulo (m): '))
            n2 = int(input('Digite o valor da altura do Retângulo (m): '))
            print()
            print('A área do Retângulo é igual a: Base X Altura')
            print(f'Desta forma, a área do Retângulo é igual a: {n1 * n2}')
            print()
        elif quest == 4:
            n1 = int(input('Digite o valor da base maior do Trapézio (m): '))
            n2 = int(input('Digite o valor da base menor do Trapézio (m): '))
            n3 = int(input('Digite o valor da altura do Trapézio (m): '))
            print()
            if n1 < n2:
                print('A base menor, não pode ser maior que a base maior. Insira os valores corretamente.')
                n1 = int(input('Digite o valor da base maior do Trapézio (m): '))
                n2 = int(input('Digite o valor da base menor do Trapézio (m): '))
                n3 = int(input('Digite o valor da altura do Trapézio (m): '))
            print()
            print('A área do Trapézio, é igual a: Base maior + Base menor/2')
            print(f'Desta forma, a área do Trapézio é igual a: {(n1 + n2) * n3 / 2}')
            print()
        elif quest == 5:
            n1 = int(input('Digite o valor do raio da circunferência (m): '))
            print()
            print(
                'A área do Círculo é igual a: π.raio²\nO perímetro do Círculo é igual a: 2π.raio\nO diâmetro do Círculo é igual a: r.2')
            print(f'Considerando π = 3,1415')
            print()
            print(
                f'Desta forma, a área do Círculo é igual a: {(n1 ** 2) * 3.1415:.2f}\nO perímetro do Círculo é igual a: {3.1415 * 2 * n1:.2f}\nO diâmetro do Círculo é igual a: {n1 * 2}')
            print()
        elif quest == 6:
            n1 = int(input('Digite o valor da diagonal maior do Losango (m): '))
            n2 = int(input('Digite o valor da diagonal menor do Losango (m): '))
            n3 = int(input('Digite o valor do lado do Losango (m): '))
            print()
            print(
                'A área do Losango é igual a: Diagonal maior X Diagonal menor/2\nO perímetro do Losango é igual a: Lado X 4')
            print()
            print(
                f'Desta forma, a área do Losango é igual a: {(n1 + n2) / 2}\nO perímetro do Losango é igual a: {n3 * 4}')
            print()
        elif quest == 7:
            print(f'Programa encerrado.')
            break
    elif quest == 3:
        print()
        print('='*15,'CALCULAR BHASKARA','='*15)
        n1 = int(input('Informe o valor de A: '))
        n2 = int(input('Informe o valor de B: '))
        n3 = int(input('Informe o valor de C: '))
        delta = n2 ** 2 - 4 * n1 * n3
        xm = (math.sqrt(delta) + (-n2)) / (n1 * 2)
        xn = - (math.sqrt(delta) - (-n2)) / (n1 * 2)
        print()
        print(f'O valor de Delta 🔺: {delta}')
        print(f"O valor de x': {xn:.2f}")
        print(f'O valor de x": {xm:.2f}')
        print()
        print('Programa reiniciado.')
        print()
    elif quest == 4:
        break
    elif quest <= 0 or quest > 4:
        print()
        print(f'Por favor, indique apenas números presentes no Menu inicial. 1 a 4 somente.')
        print('Programa reiniciado.')
        print()
