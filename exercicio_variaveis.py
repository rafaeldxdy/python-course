from datetime import date

current_date = date.today()
current_year = current_date.year

nome = 'Rafael'
sobrenome = 'Ribeiro'
ano_nascimento = 1991
idade = current_year - ano_nascimento
maior_de_idade = idade >= 18
altura_metros = 1.68

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)