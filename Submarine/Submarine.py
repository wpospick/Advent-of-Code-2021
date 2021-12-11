"""A Submarine class and example use.

This is for Advent of Code 2021. Based on Day 2 challenge. Represents 
the DepthFinder concept from the role-play. First commandline argument is the 
depth readings, the second argument is the Submarines movements.

  Typical usage example:

  sub = Submarine()
  with open(movement_file) as movement_instructions:
      for line in movement_instructions:
          sub.move(line)
  print(sub.silly_multiply())

"""

#Imports
import sys


class Submarine:
	"""Reads and processes depth readings. 

	A three-measurement sliding window to smooth out surface noise. 
	Readings are integer values	followed by a new line. Higher numbers 
	indicate longer distances from the device.
 
    Attributes:
      name: 
        EVERY SHIP MUST HAVE A NAME!
      depth: 
        An integer indicating the depth the submarine is at.
      h_pos: 
        An integer representation of the Submarines horizontal position.
        might need to rename this better as AoC progresses.
      aim: 
        An integer count of the aim.
        This might be pitch of the submarine. Will rename as needed.
    """


	name 	= 'Steve' # EVERY SHIP MUST HAVE A NAME
	depth 	= None
	h_pos 	= None
	aim 	= None
	

	def __init__(self):
		"""Inits a new Submarine at the origin point."""
		self.depth 	= 0
		self.h_pos 	= 0
		self.aim 	= 0

	def __str__(self):
		"""String representation of a Submarine object."""
		return 'Depth:\t{self.depth} \nHorizontal Pos:\t{self.h_pos} \nAim:\t{self.aim}'.format(self=self)


	def move(self, direction, magnitude=None):
		"""Parses instruction then moves the Submarine to calculated location."""

		# Check if one or both arguments were provided.
		if magnitude is None: 
			# Since no magnitude was provided, we will assume the 
			#  direction is a instruction. (e.g. - "up 3")
			# Splitting instruction into a magnitude and direction.

			# Stack Trace: direction in next line is the instruction.
			instruction = direction.split(' ') 
			magnitude = (int) (instruction[1])
			direction = instruction[0]

		# Match-case converts word direction ("up") to mathematical 
		#  calculations (this might be pitch up and down)
		match direction:
			case 'forward':
				# increases horizontal position by <magnitude>.
				# increases depth by aim multiplied by <magnitude>.
				self.h_pos += magnitude
				self.depth += self.aim * magnitude
			case 'down':
				# increases aim by <magnitude> units.
				self.aim += magnitude
			case 'up':
				# decreases aim by <magnitude> units.
				self.aim -= magnitude
			case _:
				print("you done fucked up a-a-ron...")
				print('  Direction: {dir}\n  Magnitude: {mag}').format(
						dir=direction, mag=magnitude)
		#END match
	#END move

	# IDK what this is doing in the realm of the story/physics but... 
	#  its part of the challenge...
	def silly_multiply(self):
		"""This is only for Advent of Code AFAIK."""
		return self.depth * self.h_pos


###############
#Main Function
###############
def main():
	#Welcome to the deep... we are rolling in it #Adele
	#
	##########
	depth_file = sys.argv[1] # First arg is input file of depths
	movement_file = sys.argv[2] # Second arg is input file for Submarine movement

	# Initiate Submarine...
	print('Initiating Submarine...')
	sub = Submarine()
	print(sub)
	print('...Submarine initiated.')
	print('------------------------')

	with open(movement_file) as movement_instructions:
		for line in movement_instructions:
			sub.move(line)
		#END for
	#END movement_file parser

	answer = sub.silly_multiply()
	print('{s} \nMultiply: {answer}').format(s=sub, answer=sub.silly_multiply())

#END main()

main()
