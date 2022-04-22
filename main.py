"""Word Guessing Game with three choices of games, have fun!"""

import random as rd, time as t
choice_games = 'Game Choice Titles: \n\t 1. Car Names \n\t 2. Sport Names \n\t 3. Animal Names \n\t 4. Exit'
games = {
  'car_names': ['Chevrolet', 'BMW', 'Honda', 'Ford', 'Audi', 'Nissan', 'Mercedes'],
  'sport_names': ['Soccer', 'Basketball', 'Tennis', 'Golf', 'Volleyball', 'Football'],
  'animal_names': ['Lion', 'Tiger', 'Dog', 'Bear', 'Panda', 'Zebra', 'Monkey', 'Snake', 'Elephant']
}

# welcoming players and getting their name.
player_name = input('Welcome to WORD GUESSING GAME, What is your name: ').upper()
t.sleep(2)
print(f"Nice to meet you {player_name}, I hope you enjoy the game.", '\v'), t.sleep(2)

# car choice
def cars():
  points = 0
  
  while True:
    rand_car = rd.choice(games['car_names'])
    print(f"The car name starts with {rand_car[:2]}")
    rand_car = rand_car.upper()
    guess_car = input("Guess the car or Exit: ").upper()
    
    if guess_car == rand_car:
      print('CORRECT', '\v')
      points +=1
    elif guess_car == 'EXIT':
        break
        print('\v')
    else:
      if guess_car != rand_car:
        t.sleep(3.5)
        print('That is not correct!')
        points -=1
        hint = input('Would you like a hint?: ').upper()
        if hint == 'YES':
          t.sleep(2)
          print('\v')
          print('Look through the list and guess the car, you will only get 1/2 point if you get it right', '\v')
          t.sleep(2)

          # returns cars list
          for i in games['car_names']:
            print(i.upper())
          t.sleep(3.5)
          guess_car = input("Guess the car: ").upper()
          if guess_car == rand_car:
            points += 0.5
            print('CORRECT!', '\v')
          else:
            print('WRONG!', '\v')
        elif hint != 'YES':
          print('OK', '\v')
          continue
  # after the player choose to exit   
  print('\v')
  t.sleep(3.5)
  print(f'Your final score is {points}')
  print('\v')
  t.sleep(2)

  
# sport choice
def sports():
  points = 0
  
  while True:
    rand_sport = rd.choice(games['sport_names'])
    print(f"The sport name starts with {rand_sport[:2]}")
    rand_sport = rand_sport.upper()
    guess_sport = input("Guess the sport or Exit: ").upper()

    if guess_sport == rand_sport:
      print('CORRECT', '\v')
      points +=1
    elif guess_sport == 'EXIT':
        break
        print('\v')
    else:
      if guess_sport != rand_sport:
        t.sleep(3.5)
        print('That is not correct!')
        points -=1
        hint = input('Would you like a hint?: ').upper()
        if hint == 'YES':
          t.sleep(2)
          print('\v')
          print('Look through the list and guess the sport, you will only get 1/2 point if you get it right', '\v')
          t.sleep(2)

          # returns sports list
          for i in games['sport_names']:
            print(i.upper())
            
          t.sleep(3.5)
          guess_sport = input("Guess the sport: ").upper()
          if guess_sport == rand_sport:
            points += 0.5
            print('CORRECT!', '\v')
          else:
            print('WRONG!', '\v')
        else:
          if hint != 'YES':
            print('OK', '\v')
            continue
  print('\v')
  t.sleep(3.5)
  print(f'Your final score is {points}')
  print('\v')
  t.sleep(2)

  
# animal choice
def animals():
  points = 0
  
  while True:
    rand_animal = rd.choice(games['animal_names'])
    print(f"The animal name starts with {rand_animal[:2]}")
    rand_animal = rand_animal.upper()
    guess_animal = input("Guess the animal or Exit: ").upper()

    if guess_animal == rand_animal:
      print('CORRECT', '\v')
      points +=1
    elif guess_animal == 'EXIT':
        break
        print('\v')
    else:
      if guess_animal != rand_animal:
        t.sleep(3.5)
        print('That is not correct!')
        points -=1
        hint = input('Would you like a hint?: ').upper()
        if hint == 'YES':
          t.sleep(2)
          print('\v')
          print('Look through the list and guess the animal, you will only get 1/2 point if you get it right', '\v')
          t.sleep(2)

          # returns animals list
          for i in games['animal_names']:
            print(i.upper())
            
          t.sleep(3.5)
          guess_animal = input("Guess the animal: ").upper()
          if guess_animal == rand_animal:
            points += 0.5
            print('CORRECT!', '\v')
          else:
            print('WRONG!', '\v')
        else:
          if hint != 'YES':
            print('OK', '\v')
            continue
  print('\v')
  t.sleep(3.5)
  print(f'Your final score is {points}')
  print('\v')
  t.sleep(2)


# game choice
while True:
  print(choice_games, '\v')
  try:
    game_choice = int(input('Choose game (Enter a number): '))
    
    if game_choice == 1:
      print('\t')
      t.sleep(2)
      cars()
    elif game_choice == 2:
      print('\t')
      t.sleep(2)
      sports()
    elif game_choice == 3:
      print('\t')
      t.sleep(2)
      animals()
    elif game_choice == 4:
      t.sleep(1.5)
      print('\v', 'Thank you for playing!')
      break
    else:
      if game_choice != 1 or 2 or 3 or 4:
        t.sleep(1.5)
        print('That is not one of the options, TRY AGAIN!', '\v')
  except ValueError:
    t.sleep(3)
    print('That is not a number, TRY AGAI!', '\v')