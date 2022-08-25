import random
import string

# .randint(A, B) -> Gera um número inteiro entre A e B
integer_number = random.randint(10, 20)
print(f'Random integer number: {integer_number}')

# .uniform(A, B) -> Gera um número flutuante entre A e B
float_number = random.uniform(10, 20)
print(f'Random floating number: {float_number}')

# .random() -> Gera um número flutuante entre 0 e 1
float_number = random.random()
print(f'Random floating number between 0 and 1: {float_number}')

# .randrange() -> Gera um número aleatório usando a função range()
integer_number = random.randrange(900, 999, 10)
print(f'Integer number in range(900, 999, 10): {integer_number}')

print()

# .choice() -> Seleciona aleatoriamente um item da lista
raffle = ['Maria', 'Nicolas', 'Arthur', 'Leandro', 'José', 'Gabriel']
winner_raffle = random.choice(raffle)
print(f'Raffle participants: {raffle}')
print(f'Winner: {winner_raffle}')

print()

# .choice() -> Seleciona aleatoriamente uma qtd de elementos da lista, 
# pode haver (duplicatas)
winners_raffle = random.choices(raffle, k=3)
print('New raffle with the same participants')
print(f'Winners: {winners_raffle}')

print()

# .sample() -> Seleciona aleatoriamente uma qtd de elementos da lista,
# não há duplicatas
winners_raffle_k = random.sample(raffle, k=3)
print('New raffle with the same participants')
print(f'Winners: {winners_raffle_k}')

print()

# .shuffle() -> Embaralha aleatoriamente a lista
print(f'Original raffle participants: {raffle}')
random.shuffle(raffle)
print(f'Shuffled raffle participants: {raffle}')

print()

# Gerar uma senha aleatória com random e string
letters = string.ascii_letters
digits = string.digits
characters = '!@#$%&*?'
sample = letters + digits + characters
password = ''.join(random.choices(sample, k=8)) # Senha com no mínimo 8 caracteres
print(f'Generated password: {password}')