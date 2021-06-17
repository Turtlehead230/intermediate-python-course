import random


def main():
    dice_rolls = int(input('How many dice you wanna roll??'))
    dice_sides = int(input('how many sides does you dice have??'))
    dice_sum = 0
    for i in range(0, dice_rolls):
      roll = random.randint(1, dice_sides)
      dice_sum += roll

    if roll == 1:
      print(f'You rolled a {roll}, EPIC FAIL')
    elif roll == dice_sides:
      print(f'You rolled a {roll}, EPIC GAMER MOMENT')
    else:
      print(f'you rolled a {roll}')

    print(f'You rolled a total of {dice_sum} !')

if __name__== "__main__":
  main()