import pickle
from Main_Program import CharacterMove, Fighter

with open('Ken.pickle', 'rb') as file:
    loaded_Ken = pickle.load(file)

move_type = 0

print(loaded_Ken.get_character_moves()[move_type][1][0].get_name())


