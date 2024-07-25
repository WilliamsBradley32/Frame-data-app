

""" This is the main program for the frame data program by Bradley Williams.
It uses classes in order to make updating/adding new characters easy and simple."""


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
            it's there, otherwise, it will print "not found"."""
        for attribute in self.frame_data:
            if attribute == name:
                self.frame_data[attribute] = data

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

    def get_name(self):
        """Returns the character's name"""
        return self._name

    def get_character_moves(self):
        """Returns the list of the character's moves"""
        return self._character_moves

    def show_character_moves(self, move_type):
        """Method that prints the character's moves and their frame data for the specified move type (Attacks,
        Unique Attacks, or Specials)"""

        print(f"Here is a list of {self.get_name()}'s {move_type}:")

        # Convert move_type to integer for indexing in character move list.
        if move_type.lower() == 'attacks':
            move_type = 0

        elif move_type.lower() == 'unique attacks':
            move_type = 1

        elif move_type.lower() == 'specials':
            move_type = 2

        # Loop to print each move and it's frame data.
        for attack in self._character_moves[move_type][1]:
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


# /// START OF MAIN PROGRAM LOGIC /// #
app_on = True

while app_on:

    intro = True
    character_list = False
    add_update_character = False

    while intro:
        print("Welcome to my Frame Data program!  Here you can view the frame data for any available character. \n"
              "The newest patch is 3.4. Make sure you check out the updates in case it changes the way you play your "
              "character or against another!  We'll have the details for you to view at a later date.")

        print("\n Please choose an option to proceed! \n 1. Character List - This is where you can view frame data"
              "for the character of your choice! \n 2. Add or Update a character (developer) - "
              "This is for developers only! 3. Quit - This will exit the program!")

        try:
            user_input = int(input())

        except ValueError:
            print('Please enter a number to proceed!')
            continue

        if user_input == 3:
            app_on = False

        elif user_input == 2:
            add_update_character = True
            intro = False

        elif user_input == 1:
            character_list = True
            intro = False

    while character_list:
        user_input = input('\n Welcome to the list of characters for which we have frame data for! \n'
                           'You can choose a character by typing their name or number. This will take you their entry,'
                           ' where you can view the frame data for each of their moves.')

        if user_input == 1 or user_input.lower() == 'ken':
            chosen_fighter = Ken







    while add_update_character:
        break






