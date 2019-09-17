import pickle
import pandas as pd
import numpy as np

# read in the model
my_model = pickle.load(open("finalpickle.p","rb"))

# create a function to take in user-entered amounts and apply the model
def active_inactive(amounts_float, model=my_model):
    
    # put everything in terms of tablespoons
    # flour, milk, sugar, butter, eggs, baking powder, vanilla, salt
    # multipliers = [16, 16, 16, 16, 3, .33, .33, .33]
    
    # sum up the total values to get the total number of tablespoons in the batter
    # total = np.dot(multipliers, amounts_float)

    # note the proportion of flour and sugar
    #codon_order = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'w', 'y']
    amounts_float = [int(i) for i in amounts_float]

    positions = [59, 68, 171, 1, 151, 128, 39, 135, 21, 160]

    pred = np.zeros(195)

    for i,p in enumerate(positions):
        if amounts_float[i] == 1:
            pred[p] = 1

    # make a prediction
    prediction = my_model.predict(np.asarray(pred).reshape(1,-1))[0]

    message_array = ["Active",
                     "Inactive"]
    # return a message
    return message_array[prediction]
