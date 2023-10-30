idade = int (input("digite sua idade"))
total = float(input('digite o valor total do produto'))

if(idade >= 18 ):
    print('Pode ter o desconto')
    desconto = total  * 0.1
    valorFinal = total - desconto
    print(f"""
    o valor do desconto foi de {desconto}, 
    e o total é de {valorFinal}
    """)