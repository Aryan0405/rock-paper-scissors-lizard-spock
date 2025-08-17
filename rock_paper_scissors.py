#!/usr/bin/env python
# coding: utf-8

# ROCK PAPER SCISSORS LIZARD SPOCK

# RULES OF THE GAME
# 
# Scissors cut Paper.
# Paper covers Rock.
# Rock crushes Lizard.
# Lizard poisons Spock.
# Spock smashes Scissors.
# Scissors beat Lizard.
# Lizard eats Paper.
# Paper disproves Spock.
# Spock vaporizes Rock.
# Rock breaks Scissors
# 
# Rules which were not there in the usual game:
# Rock crushes Lizard.
# Lizard poisons Spock.
# Spock smashes Scissors.
# Scissors beat Lizard.
# Lizard eats Paper.
# Paper disproves Spock.
# Spock vaporizes Rock.
# 
# Spock, being a character of pure logic, is "disproven" by the simplicity of paper. It's a playful twist on his intellectual nature, as if a logical argument (Spock) can be refuted or rendered invalid by a simple document (paper).
# 
# In essence, it's just one of the ten unique winning/losing relationships in the expanded game, adding more complexity and reducing the chance of ties compared to the original Rock-Paper-Scissors.

# 1) ✊
# 2) ✋
# 3) ✌️
# 4) 🦎
# 5) 🖖

# In[1]:


import random 
computer = random.randint(1,5)
player = int(input("Enter a number between 1 and 5: " ))
    
if player == 1:
    print("You chose = ✊")
elif player==2:
    print("You chose = ✋")
elif player==3:
    print("You chose = ✌️")
elif player==4:
    print("You chose = 🦎")
else:
    print("You chose = 🖖")

if computer == 1:
    print("Computer chose = ✊")
elif computer ==2:
    print("Computer chose = ✋")
elif computer==3:
    print("Computer chose = ✌️")
elif computer==4:
    print("Computer chose = 🦎")
else:
    print("Computer chose = 🖖")

if player == computer:
    print("It's a tie!")
else:
  if (player == 1 and (computer == 3 or computer == 4)) or \
       (player == 2 and (computer == 1 or computer == 5)) or \
       (player == 3 and (computer == 2 or computer == 4)) or \
       (player == 4 and (computer == 2 or computer == 5)) or \
       (player == 5 and (computer == 1 or computer == 3)):
        print("You won!")
  else:
        print("You lost!")


# In[ ]:




