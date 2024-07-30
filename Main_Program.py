

""" This is the main program for the frame data program by Bradley Williams.
It uses classes in order to make updating/adding new characters easy and simple."""

import pickle
import copy


class CharacterMove:
    """Class that functions as a record of a given character's move.  Records each frame attribute and the name."""
    def __init__(self, name):
        self.name = name
        self.frame_data = {}

    def get_name(self):
        """Returns the name of the move"""
        return self.name

    def get_attribute_data(self, attribute):
        """Returns the attribute data for the move"""
        return self.frame_data[attribute]

    def add_attribute(self, name, data):
        """Adds an attribute and its frame data to the list of attributes
             for the Character move"""
        self.frame_data[name] = data

    def update_attribute(self, name, data):
        """Searches for an attribute in the list of frame data traits and updates if
            it's there."""
        for attribute in self.frame_data:
            if attribute == name:
                self.frame_data[attribute] = data
                return

    def delete_attribute(self, name):
        """Removes an attribute from the list of frame data."""
        for attribute in self.frame_data:
            if attribute == name:
                del self.frame_data[attribute]


class Fighter:
    """Class that functions as the given character.  Has a list of the character's moves and gives the ability
    to add/update any given move."""

    def __init__(self, name):
        self._name = name
        self._character_moves = [['Attacks', []], ['Unique Attacks', []], ['Specials', []]]
        self._filtered_list = None

    def get_name(self):
        """Returns the character's name"""
        return self._name

    # !!! Only for Testing !!! Remove when done.
    def copy_character_moves(self, moves_list):
        self._character_moves = copy.deepcopy(moves_list)
        self._filtered_list = copy.deepcopy(self._character_moves)

    def get_character_moves(self):
        """Returns the list of the character's moves"""
        if self._filtered_list is None:
            self._filtered_list = copy.deepcopy(self._character_moves)
        return self._filtered_list

    def show_character_moves(self, move_type, moves_list):
        """Method that prints the character's moves and their frame data for the specified move type (Attacks,
        Unique Attacks, or Specials)"""
        if self._filtered_list is None:
            self._filtered_list = copy.deepcopy(self._character_moves)

        if move_type == '1':
            move_type = 'Attacks'
        elif move_type == '2':
            move_type = 'Unique Attacks'
        elif move_type == '3':
            move_type = 'Specials'

        print(f"\nHere is a list of {self.get_name()}'s {move_type}:")

        # Convert move_type to integer for indexing in character move list.
        if move_type.lower() == 'attacks':
            move_type = 0

        elif move_type.lower() == 'unique attacks':
            move_type = 1

        elif move_type.lower() == 'specials':
            move_type = 2

        # Loop to print each move and it's frame data.
        for attack in moves_list[move_type][1]:
            print(f'{attack.get_name()}: Start Up - {attack.get_attribute_data('start up')} | Active - '
                  f'{attack.get_attribute_data('active')} | Recovery - '
                  f'{attack.get_attribute_data('recovery')} | On Hit - {attack.get_attribute_data('on hit')} '
                  f'| On Block - {attack.get_attribute_data('on block')}')

    def add_character_move(self, name):
        """Adds a move to the character's list"""

        # Gather frame data for the move from the developer.
        start_up = input(f'What are the start-up frames for {name}? \n')
        active = input(f'What are the active frames for {name}? \n')
        recovery = input(f'What are the recovery frames for {name}? \n')
        on_hit = input(f'What are the frames if {name} hits? \n')
        on_block = input(f'What are the frame if {name} is blocked? \n')

        # Create new move to be added
        new_move = CharacterMove(name)

        # Add specified attributes to the new move
        new_move.add_attribute('start up', start_up)
        new_move.add_attribute('active', active)
        new_move.add_attribute('recovery', recovery)
        new_move.add_attribute('on hit', on_hit)
        new_move.add_attribute('on block', on_block)

        while True:
            try:
                move_type = int(input('Is this move a: \n 1. Attack \n 2. Unique Attack or \n 3. Special? \nPlease '
                                'enter the number associated with the type. \n'))
            except ValueError:
                print('Please enter a number for the type. \n')
                continue

            # Simple form of data validation
            if move_type not in range(1,4):
                print('Sorry, that is not one of the listed types; please try again.')

            # Break loop and add moves to character move list.
            else:
                self._character_moves[move_type - 1][1].append(new_move)
                break

    def filter_character_moves(self, move_type, attribute):
        """Method that handles the filtering interaction for when character frame data is displayed."""

        # If no filter has been applied yet.
        if self._filtered_list is None:
            self._filtered_list = copy.deepcopy(self._character_moves)

        character_move_len = len(self._filtered_list[move_type][1])
        filtered_list = []
        lowest_attribute = None
        knockdown_list = []

        # Loops through moves for loaded character, sorting them by the passed in attribute (descending).
        while len(filtered_list) < character_move_len:
            for move in self._character_moves[move_type][1]:
                if move not in filtered_list:
                    # Special case for moves that don't have a number for the on hit frames.
                    if move.frame_data[attribute] == 'Knockdown':
                        knockdown_list.append(move)
                        character_move_len -= 1

                    elif lowest_attribute is None:
                        lowest_attribute = int(move.frame_data[attribute])
                        lowest_move = move

                    else:
                        if int(move.frame_data[attribute]) <= lowest_attribute:
                            lowest_attribute = int(move.frame_data[attribute])
                            lowest_move = move
            if lowest_attribute is not None:
                filtered_list.append(lowest_move)
                lowest_attribute = None

        if len(knockdown_list) > 0:
            filtered_list += knockdown_list

        self._filtered_list[move_type][1] = filtered_list[:]

    def reset_filter(self):
        """Sets the filtered list to the original list."""
        self._filtered_list = copy.deepcopy(self._character_moves)


# /// START OF MAIN PROGRAM LOGIC /// #
def main():
    app_on = True

    intro = True
    character_list = False
    add_update_character = False

    while app_on:

        while intro:
            print("Welcome to my Frame Data program!  Here you can view the frame data for any available character. \n"
                  "The newest patch is 3.4. Make sure you check out the updates in case it changes the way you play"
                  " your character or against another!  We'll have the details for you to view at a later date.")

            print("\n Please choose an option to proceed! \n 1. Character List - This is where you can view frame data"
                  " for the character of your choice! \n 2. Add or Update a character (developer) - "
                  "This is for developers only!\n 3. Quit - This will exit the program!")

            try:
                user_input = int(input())

            except ValueError:
                print('Please enter a number to proceed!')
                continue

            # Quits out of the app.
            if user_input == 3:
                app_on = False
                break

            # Initializes developer update/add logic
            elif user_input == 2:
                add_update_character = True
                intro = False

            # Initializes character frame data logic
            elif user_input == 1:
                character_list = True
                intro = False

        # Logic for interacting with Character List option from Intro
        while character_list:
            print('\n Welcome to the list of characters for which we have frame data for! \n You can choose a '
                  'character by typing their name or number. This will take you to their entry, where you can view '
                  'the frame data for each of their moves.')

            try:
                user_input = input('\n Please choose a character. \n 1. Ken \n 2. Quit \n')

                if user_input == '1' or user_input.lower() == 'ken':
                    chosen_fighter = 'Ken'

                    try:
                        with open(f'{chosen_fighter}.pickle', 'rb') as file:
                            loaded_fighter = pickle.load(file)

                    except FileNotFoundError:
                        print("Character not found.")

                    except pickle.UnpicklingError:
                        print("There is currently an issue what that character's file.")

                    while True:
                        new_user_input = input('\n Please type the name or number of which type of frame '
                                           'data you would like to see.\n 1. Attacks \n 2. Unique Attacks '
                                           '\n 3. Specials \n')

                        try:
                            if new_user_input in ['1', '2', '3', 'Attacks', 'attacks', 'Unique Attacks', 'unique attacks',
                                          'Specials', 'specials']:
                                loaded_fighter.show_character_moves(new_user_input, loaded_fighter.get_character_moves())

                            elif new_user_input == '4' or new_user_input.lower()[0] == 'q':
                                character_list = False
                                break

                            elif new_user_input.lower().split()[0] == 'filter,':
                                new_user_input = new_user_input.lower().split()

                                try:
                                    if len(new_user_input) == 3:
                                        new_user_input = [new_user_input[0],
                                                          new_user_input[1] + ' ' + new_user_input[2]]

                                    if new_user_input[1] == 'active':
                                        print('To filter, select a category from this list: '
                                              '"start up, recovery, on hit, on block". \n')

                                    elif new_user_input[1] == 'default':
                                        loaded_fighter.reset_filter()

                                    elif (new_user_input[1] in
                                            loaded_fighter.get_character_moves()[0][1][0].frame_data):
                                        loaded_fighter.filter_character_moves(0, new_user_input[1])
                                        loaded_fighter.filter_character_moves(1, new_user_input[1])
                                        loaded_fighter.filter_character_moves(2, new_user_input[1])
                                    else:
                                        print('To filter, select a category from this list: '
                                              '"start up, recovery, on hit, on block". \n')
                                except IndexError:
                                    print('Please add a category to your request.')
                                    continue

                            else:
                                print('Please choose the move type or its associated number. You can also type "4" '
                                      'or "Quit" to go back to the main menu.\n')
                                print('\nYou can filter by each category by typing: Filter, "category" \n'
                                      '(You can reset the filter with: Filter, "default"')
                        except IndexError:
                            print('Please try again!\n')
                            continue

                elif user_input == '2' or user_input.lower().split()[0] == 'q':
                    character_list = False

                else:
                    print('Please choose one of the listed options! \n')
            except IndexError:
                print('Please Try Again!\n')
                continue

        while add_update_character:
            dev_input = input('Would you like to add or update an existing character? \n'
                              'Please enter "add" or "update". \n')

            if dev_input == 'add':
                new_char_input = input("What is this new character's name? \n")
                new_char = Fighter(new_char_input)

                while True:
                    new_move_input = input('Please enter the next move: \n')

                    new_move_confirm = input(f'Is "{new_move_input}" the move you want to add? ("y" or "n") \n')
                    if new_move_confirm.lower() == 'y':
                        new_char.add_character_move(new_move_input)
                    else:
                        continue

                    new_move_done = input('Would you like to add another move? ("y" or "n") \n')

                    if new_move_done == 'y':
                        continue

                    elif new_move_done == 'n':
                        break

                    else:
                        print('Please enter "y" or "n".')

                with open(f'{new_char_input}.pickle', 'wb') as file:
                    pickle.dump(new_char, file)

            elif dev_input == 'update':
                update_input = input('Please choose the character you would like to update. (You can choose '
                                     'their name or number!)\n 1. Ken \n 2. Quit \n')

                if update_input == '1' or update_input.lower() == 'ken':
                    try:
                        with open('Ken.pickle', 'rb') as file:
                            update_fighter = pickle.load(file)

                    except FileNotFoundError:
                        print("Character not found.")

                    except pickle.UnpicklingError:
                        print("There is currently an issue what that character's file.")

                    while True:
                        try:
                            type_input = int(input('Please enter the number of the type of move you would like to '
                                               'update \n 1. Attacks \n 2. Unique Attacks \n 3. Specials \n'))

                            if int(type_input) == 1:
                                update_fighter.show_character_moves('attacks', update_fighter.get_character_moves())

                            elif int(type_input) == 2:
                                update_fighter.show_character_moves('unique attacks',
                                                                    update_fighter.get_character_moves())

                            elif int(type_input) == 3:
                                update_fighter.show_character_moves('specials', update_fighter.get_character_moves())

                        except ValueError:
                            print('Please enter the number associated with the move type.')
                            continue

                        while True:
                            update_move_input = input('Which of the following moves would you like to update?\n')

                            for move in update_fighter.get_character_moves()[type_input - 1][1]:
                                if update_move_input == move.get_name():
                                    print(
                                        f'{move.get_name()}: Start Up - {move.get_attribute_data('start up')} '
                                        f'| Active - '
                                        f'{move.get_attribute_data('active')} | Recovery - '
                                        f'{move.get_attribute_data('recovery')} | On Hit - '
                                        f'{move.get_attribute_data('on hit')} '
                                        f'| On Block - {move.get_attribute_data('on block')}')
                                    change_input = input('Enter what you would like to change as '
                                                         '"attribute" "new value"\n')
                                    move.update_attribute(change_input.split()[0], change_input.split()[1])
                                    print(
                                        f'{move.get_name()}: Start Up - {move.get_attribute_data('start up')} '
                                        f'| Active - '
                                        f'{move.get_attribute_data('active')} | Recovery - '
                                        f'{move.get_attribute_data('recovery')} | On Hit - '
                                        f'{move.get_attribute_data('on hit')} '
                                        f'| On Block - {move.get_attribute_data('on block')}')


            elif dev_input.lower() == 'q':
                intro = True
                add_update_character = False

            else:
                print('Please enter either "add" or "update".  You can also type "q" to return to the previous menu.')


if __name__ == '__main__':
    main()




