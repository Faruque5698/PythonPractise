import random
# import my_module

# a = 10
# b = 20
# print(random.randint(a,b))
# print("my fvrt number:", my_module.my_fv_num)

# friends = ["Shifat", "Reza", "Nahid", "Fuyad", "Rifat"]
# radom_data = random.randint(0,4)
# print(friends[radom_data])
# print(random.choice(friends))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


my_input = input('Select rock, paper or scissors\n')
if my_input == 'rock':
    my_val = 0
    print("rock:",rock)
elif my_input == 'paper':
    my_val = 1
    print('paper:',paper)
else:
    my_val = 2
    print('scissors:',scissors)


random_data = random.randint(0,2);
if random_data == 0:
    print("rock:",rock)
elif random_data == 1:
    print('paper:',paper)
else:
    print('scissors:',scissors)

if random_data == 0 and my_val == 1:
    print('You win')
elif random_data > my_val:
    print('You lose')
else:
    print('Tie')
