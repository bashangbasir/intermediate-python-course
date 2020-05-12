import random

def main():
  #first argument in randint() method is start value, 2nd arg is end value
  dice_rolls = 2
  dice_sum = 0
  
  for i in range(dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_sum += roll
  
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()