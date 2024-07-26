

"""This creates a default copy of the character Ken."""

import pickle

from Main_Program import CharacterMove, Fighter

# Ken = Fighter('Ken')
#
# Ken.add_character_move('Light Punch')
# Ken.add_character_move('Light Kick')
# Ken.add_character_move('Medium Punch')
# Ken.add_character_move('Medium Kick')
# Ken.add_character_move('Heavy Punch')
# Ken.add_character_move('Heavy Kick')
#
# Ken.add_character_move('Chin Buster')
# Ken.add_character_move('Triple Flash Kicks')
#
# Ken.add_character_move('Light Hadoken')
# Ken.add_character_move('Medium Hadoken')
# Ken.add_character_move('Heavy Hadoken')
# Ken.add_character_move('Light Shoryuken')
# Ken.add_character_move('Medium Shoryuken')
# Ken.add_character_move('Heavy Shoryuken')
# Ken.add_character_move('Light Tatsumaki Senpu-kyaku')
# Ken.add_character_move('Medium Tatsumaki Senpu-kyaku')
# Ken.add_character_move('Heavy Tatsumaki Senpu-kyaku')


# with open('Ken.pickle', 'wb') as file:
#     pickle.dump(Ken, file)


with open('Ken.pickle', 'rb') as file:
    loaded_Ken = pickle.load(file)

Ken = Fighter('Ken')
Ken.copy_character_moves(loaded_Ken.get_character_moves())


with open('Ken.pickle', 'wb') as file:
    pickle.dump(Ken, file)