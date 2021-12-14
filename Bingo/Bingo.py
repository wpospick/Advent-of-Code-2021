"""A Bingo class and example use.

This is for Advent of Code 2021. Based on Day 3 challenge. Represents 
the Sub diagnostics concept from the role-play. First commandline argument is the 
depth readings, the second argument is the Submarines movements, third is the 
diagnostics reading.

Input is a list of binary numbers.

  Typical usage example:

    #TODO#
  sub = Submarine()
  with open(movement_file) as movement_instructions:
      for line in movement_instructions:
          sub.move(line)
  print(sub.silly_multiply())

"""

#Imports
import sys

class BingoCard:
    card = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]
    called_matrix = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]

    def __init__(self):
        self.card = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
            ]
        self.called_matrix = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
            ]

    def __str__(self):
        return str(self.card)

    def __repr__(self):
        # output = '------------------\n'
        output = ''
        for idx, row in enumerate(self.card):
            for column in self.card[idx]:
                output += ' {val:>3}'.format(val=column)
            output += '\n'
        # print(str(output))
        return output


    def populate_card(self, buffer):
        # print(buffer)
        items = (str(buffer).split(' '))
        for idx, val in enumerate(items):
            # print(val)
            if val == '':
                items.pop(idx)
        # print(items)
        if len(items) == 25:
            # print(len(items))
            for idx, val in enumerate(items):
                # print('idx: ' + str(idx) + '\tval: ' + val)
                row = int(idx/5)
                col = idx%5
                self.card[row][col] =  val
                # print('idx: ' + str(idx) + '\trow: ' + str(row) + '\tcol: ' + str(col) + '\tval: ' + str(self.card[row][col]))

        row_count = len(self.card)
        # print('card: \n' + str(self.card))

    def check_card(self, called_num):
        """."""
        pass
        # go through the elements of the bingo card and check if they match called num
        # if they do, then mark that same bit on the called_matrix
        #END def




class Bingo:
    """Reads and processes ship diagnostic inputs. 

    A three-measurement sliding window to smooth out surface noise. 
    Readings are integer values followed by a new line. Higher numbers 
    indicate longer distances from the device.
 
    Attributes:
      pwr_consum: 
        Determined by multiplying the gamma rate by the epsilon rate.
      epsilon_rate: 
        Determined by finding the LEAST common bit in the corresponding 
        position of all numbers in the diagnostic report.
      gamma_rate: 
        Determined by finding the MOST common bit in the corresponding 
        position of all numbers in the diagnostic report.
    """



    def __init__(self, game_file=''):
        """Inits a new Bingo object."""
        self.call_order = []
        self.card_list = [] #type BingoCard

        if game_file != '':
            self.refresh_game(game_file)
        #END __init__

    def __str__(self):
        """String representation of a BingoCard object."""
        output  = '******** Bingo Card ********\n'
        for bingo_card in enumerate(self.card_list):
            output += '--------- Card {:>2} ------------\n'.format(bingo_card[0])
            output += repr(bingo_card[1])
        output += '------------------------------\n'
        output += '****************************'
        return output

    def __repr__(self):
        """String representation of the DiagnosticsReport object."""
        output  = ''
        for bingo_card in enumerate(self.card_list):
            output += '--------- Card {:>2} ------------\n'.format(bingo_card[0])
            output += repr(bingo_card[1])
        output += '------------------------------\n'
        return output

    def refresh_game(self, game_file):
        with open(game_file) as game_log:
            # print('In refresh_game()...')
            self.read_game_log(game_log)
            #END diagnostic_log parser


    def read_game_log(self, game_log):
        """Reads a list of binary numbers from the diagnostic log."""
        buffer = ''

        for index, line in enumerate(game_log):
            line = line.strip()
            # print('line: {:>10}'.format(line))
            if line == '': # skip the empty lines
                # print('SKIPPER')
                buffer = '' # Reset buffer on empty lines between cards
                continue
            if index == 0: # first line is the "calling order"
                # print('Call Order... GME 2 DA MOON')
                self.call_order = line.split(',')
                continue
            else:
                # print('I is a bingo card')
                buffer += line
                buffer_split = str(buffer).split()
                for val in buffer_split:
                    # print(val)
                    if val == '':
                        buffer_split.pop(val)
                # print(str(buffer).split())
                # This means I am a row of values for a bingo card
                if len(str(buffer).split()) == 25:
                    # I have a full card worth of numbers
                    temp_card = BingoCard()
                    temp_card.populate_card(buffer)
                    # print(temp_card)
                    self.card_list.append(temp_card)
                    # print(self.card_list)
                else:
                    buffer += ' '
                    pass
            #END for
        #END def


###############
#Main Function
###############
def main():
    #Welcome to the deep... we are rolling in it #Adele
    #
    ##########
    depth_file = sys.argv[1] # First arg is input file of depths
    movement_file = sys.argv[2] # Second arg is input file for Submarine movement
    diagnostic_file = sys.argv[3] # Third arg is input file for Submarine Diagnostic log
    bingo_file = sys.argv[4] # Fourth arg is input file for Bingo Game file

    # Initiate B-I-N-G-O...
    # print('Initiating BINGO...')
    # game = Bingo(bingo_file)
    # print(game)
    # print('...BINGO initiated.')
    # print('------------------------')
    bing = Bingo(bingo_file)
    print(bing)
    print(bing.call_order)
    # bing = Bingo(bingo_file)
    # b = BingoCard()
    # print(b)
    # b.populate_card('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25')
    # print(b)




#END main()

if __name__ == '__main__':
    main()
