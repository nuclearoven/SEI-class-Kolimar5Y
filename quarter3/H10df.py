from operator import index

import pandas as pd
import numpy as np

def roll_dice(size=20):
    """returns a list of random integers between 1 and 6 with the size 20"""
    return np.random.randint(1,7,  size=size)

#creates a dictionary of three returns of the "roll_dice" function
my_dict= {'dice1' : roll_dice(), 'dice2' : roll_dice(), 'dice3' : roll_dice()}

#turns "my_dict" into a dataframe and creates two new collums:
#"sum" is the sum of collum 1-3
#"multi" is the multiple of collum 1-3
df_dice = pd.DataFrame(my_dict)
df_dice['sum'] = df_dice.sum(axis=1)
df_dice['multi'] = my_dict['dice1'] * my_dict['dice2'] * my_dict['dice3']

#prints the row if the first dice throw returns a 6
value = 6
print(df_dice[df_dice['dice1'] == value])