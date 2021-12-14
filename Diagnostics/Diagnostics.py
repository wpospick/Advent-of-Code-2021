"""A Diagnostics class and example use.

This is for Advent of Code 2021. Based on Day 3 challenge. Represents 
the Sub diagnostics concept from the role-play. First commandline argument is the 
depth readings, the second argument is the Submarines movements, third is the 
diagnostics reading.

Input is a list of binary numbers.

  Typical usage example:

  sub = Submarine()
  with open(movement_file) as movement_instructions:
      for line in movement_instructions:
          sub.move(line)
  print(sub.silly_multiply())

"""

#Imports
import sys


class DiagnosticReport:
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


    pwr_consum = None
    epsilon_rate = None
    gamma_rate = None
    e_string = None
    g_string = None
    positional_frequency = []
    row_count = 0

    life_support_rating = None
    o2_generator_rating = None
    co2_scrubber_rating = None
    o2_list = []
    co2_list = []

    def __init__(self, diagnostic_file=''):
        """Inits a new DianosticReport object."""
        self.pwr_consum = 0
        self.epsilon_rate = 0
        self.gamma_rate = 0
        self.e_string = ''
        self.g_string = ''
        self.positional_frequency = []

        self.life_support_rating = 0
        self.o2_generator_rating = 0
        self.co2_scrubber_rating = 0
        self.o2_list = []
        self.co2_list = []

        if diagnostic_file != '':
            self.diagnostic_refresh(diagnostic_file)
        #END __init__

    def __str__(self):
        """String representation of the DiagnosticsReport object."""
        output  = '********DIAGNOSTIC REPORT********\n'
        output += '{:<25}: {:>12}\n'.format('Epsilon Rate',self.epsilon_rate)
        output += '{:<25}: {:>12}\n'.format('Gamma Rate', self.gamma_rate)
        output += '{:>25}: {:>12}\n'.format('Power Consumption', self.pwr_consum)
        output += '{:<25}: {:>12}\n'.format('O2 Generator Rating', self.o2_generator_rating)
        output += '{:<25}: {:>12}\n'.format('CO2 Scrubber Rating', self.co2_scrubber_rating)
        output += '{:>25}: {:>12}\n'.format('Life Support Rating', self.life_support_rating)
        output += '********DIAGNOSTIC REPORT********'
        return output

    def diagnostic_refresh(self, diagnostic_file):
        with open(diagnostic_file) as diagnostic_log:
            self.read_diag_log(diagnostic_log)
            #END diagnostic_log parser
        self.calc_ge()
        self.calc_life_support()

    def stream_size(self, line):
        """Calculates the length of row of the data in the log file."""
        for bit in line:
            self.positional_frequency.append(0)

    def read_ge(self, line):
        """Reads a row of data and interprets it for the GE calcs."""
        self.row_count += 1
        # This section fills the positional_frequency for calculating Gamma and Epsilon calculations
        for index, bit in enumerate(line):
            if bit == '1':
                self.positional_frequency[index] += 1
            elif bit == '0':
                pass

    def calc_ge(self):
        """Calculate the Gamma, Epsilon, and Power Consumption values."""
        for i, value in enumerate(self.positional_frequency):
            ratio = self.positional_frequency[i] / self.row_count 
            if ratio >= 0.5: # 1 is most common or tied
                self.e_string += '0'
                self.g_string += '1'
            else: # 0 is most common
                self.e_string += '1'
                self.g_string += '0'
            #END for
        self.gamma_rate = int(self.g_string, 2)
        self.epsilon_rate = int(self.e_string, 2)
        self.pwr_consum = self.gamma_rate * self.epsilon_rate
        #END def 

    def read_diag_log(self, diagnostic_log):
        """Reads a list of binary numbers from the diagnostic log."""
        for line in diagnostic_log:
            line = line.strip()
            # print(line)

            #Add the line to the o2_list and co2_list
            self.o2_list.append(line)
            self.co2_list.append(line)

            # Add another element for calculating
            if len(self.positional_frequency) != len(line):
                self.stream_size(line)
            self.read_ge(line)
            #END for
        #END def

    def calc_gep(self, log, position):
        """Reads a list of binary numbers and calculates Gamma, Epsilon, and Power Consumption values."""
        pass

        #END def

    def calc_o2(self, temp_list, position):
        """Reads a list of binary numbers and calculates the O^2 Generator Rating."""
        culled_list = []
        freq = 0
        num_rows = 0
        for i, line in enumerate(temp_list): # go though every row
            num_rows += 1
            if line[position] == '1':
                freq += 1
            else:
                pass

        # Exit if only one item in temp_list
        if num_rows == 1:
            self.o2_generator_rating = int(temp_list[0], 2)
            return temp_list

        rolling_ratio = freq / num_rows
        if rolling_ratio >= 0.5: # 1 is most common or tied
            most_common_val = '1'
            # cull the list
            for line in temp_list:
                line_bit_pos_val = line[position]
                if line_bit_pos_val == most_common_val:
                    # most common, so add line to temp_o2_list
                    culled_list.append(line)
            #END Culling
        else: # 1 is most common
            most_common_val = '0'
            # cull the list
            for line in temp_list:
                line_bit_pos_val = line[position]
                if line_bit_pos_val == most_common_val:
                    # most common, so add line to temp_o2_list
                    culled_list.append(line)
            #END Culling

        # Exit if only one item in temp_list
        if len(culled_list) == 1:
            self.o2_generator_rating = int(culled_list[0], 2)
            return culled_list

        return culled_list

    def calc_co2(self, temp_list, position):
        """Reads a list of binary numbers and calculates the CO^2 Generator Rating."""
        culled_list = []
        freq = 0
        num_rows = 0
        for i, line in enumerate(temp_list): # go though every row 
            num_rows += 1
            if line[position] == '1':
                freq += 1
            else:
                pass
        # Exit if only one item in temp_list
        if num_rows == 1:
            self.co2_scrubber_rating = int(temp_list[0], 2)
            return temp_list

        rolling_ratio = freq / num_rows
        if rolling_ratio >= 0.5: # 1 is most common or tied
            least_common_val = '0'
            # cull the list
            for line in temp_list:
                line_bit_pos_val = line[position]
                if line_bit_pos_val == least_common_val:
                    # most common, so add line to temp_o2_list
                    culled_list.append(line)
            #END Culling
        else: # 1 is least common
            least_common_val = '1'
            # cull the list
            for line in temp_list:
                line_bit_pos_val = line[position]
                if line_bit_pos_val == least_common_val:
                    # most common, so add line to temp_o2_list
                    culled_list.append(line)
            #END Culling

        # Exit if only one item remains in culled_list
        if len(culled_list) == 1:
            self.co2_scrubber_rating = int(culled_list[0], 2)
            return culled_list
        return culled_list
    
    def calc_life_support(self):
        index = 0
        while index < len(self.positional_frequency): #go through every bit in a line
            self.o2_list = self.calc_o2(self.o2_list, index)
            self.co2_list = self.calc_co2(self.co2_list, index)
            index += 1
        self.life_support_rating = self.o2_generator_rating * self.co2_scrubber_rating
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

    # Initiate Submarine...
    print('Initiating Diagnostic...')
    diag = DiagnosticReport(diagnostic_file)
    print(diag)
    print('...Diagnostic initiated.')
    print('------------------------')


#END main()

if __name__ == '__main__':
    main()
