import random


# Obtener opción del usuario y la computadora
def choose_options():
  # Tupla de opciones
  options = ('piedra', 'papel', 'tijera')

  # Opción del usuario
  user_option = input("Piedra, Papel o Tijera: ")
  user_option = user_option.lower()

  if user_option not in options:
    print("Opción no válida")
    return None, None

  # Opción de la computadora
  computer_option = random.choice(options)

  return user_option, computer_option


# Verificar opciones introducidas
def check_rules(user_option, computer_option, user_wins, computer_wins):
  uo = user_option
  co = computer_option

  if uo == co:
    print("Empate")
  elif uo == 'piedra':

    if co == 'tijera':
      print('piedra gana tijera. Gana user')
      user_wins += 1
    elif co == 'papel':
      print('papel gana piedra. Gana computer')
      computer_wins += 1

  elif uo == 'papel':

    if co == 'piedra':
      print('papel gana piedra. Gana user')
      user_wins += 1
    elif co == 'tijera':
      print('papel gana tijera. Gana computer')
      computer_wins += 1

  elif uo == 'tijera':

    if co == 'papel':
      print('tijera gana papel. Gana user')
      user_wins += 1
    elif co == 'piedra':
      print('piedra gana tijera. Gana computer')
      computer_wins += 1

  return user_wins, computer_wins


# Veficar ganador
def check_wins(user_wins, computer_wins):
  if user_wins == 2:
    print("gano user")
    return 'break'
  if computer_wins == 2:
    print("gano computer")
    return 'break'


# Main
def run_game():
  user_wins = 0
  computer_wins = 0
  rounds = 1

  while True:
    print('*' * 10)
    print(f'ROUND {rounds}')
    print('*' * 10)

    print('')
    print(f'Victorias user: {user_wins}')
    print(f'Victorias computer: {computer_wins}')
    print('')

    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option,
                                           user_wins, computer_wins)
    result = check_wins(user_wins, computer_wins)

    if result == 'break':
      break


run_game()
