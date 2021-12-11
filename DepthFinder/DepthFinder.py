"""A DepthFinder class and example use.

This is for Advent of Code 2021. Based on Day 1 challenge. Represents 
the DepthFinder concept from the role-play.

  Typical usage example:

  df = DepthFinder()
  with open(depth_file) as f_movement:
      for line in f_movement:
          df.parse_reading(line)
          df.calculate_metrics()
  print(df)

"""

#Imports
import sys


class DepthFinder:
	"""Reads and processes depth readings. 

	A three-measurement sliding window to smooth out surface noise. 
	Readings are integer values	followed by a new line. Higher numbers 
	indicate longer distances from the device.
 
    Attributes:
      depth_trio: 
        A triple representing the three-measurement window.
      prev_sum: 
        An integer summation the previous windows.
      cur_sum: 
        An integer summation of the current window.
      deeper_count: 
        An integer count of the readings that got deeper.
      shallower_count:
        An integer count of the readings that got shallower.
      flat_count:
        An integer count of the reading that remained the same.
    """

	depth_trio = [None, None, None] # Order will be Newest, Middle, Oldest
	prev_sum = None
	cur_sum = None
	deeper_count = 0 
	shallower_count = 0
	flat_count = 0

	def __init__(self):
		"""Inits a new DepthFinder."""
		pass

	def __str__(self):
		"""String representation of a DepthFinder object."""
		output = '----------------\n'
		output += 'Current reading: \n({a},{b},{c})\n'.format(a=str(self.depth_trio[0]), b=str(self.depth_trio[1]), c=str(self.depth_trio[2]))
		output += 'Metrics: \n  Deep: {deep}\n  Shallower: {shall}\n  Flat: {flat}'.format(deep=self.deeper_count, shall=self.shallower_count, flat=self.flat_count)
		return output
	#END def __str__

	def parse_reading(self, reading):
		"""Parses a single depth reading into window and sumates."""

		# Parses through the first 3 lines to get a full window.
		if self.depth_trio[0] is None:
			self.depth_trio[0] = int(reading.strip())
		elif self.depth_trio[1] is None:
			self.depth_trio[1] = self.depth_trio[0]
			self.depth_trio[0] = int(reading.strip())
		elif self.depth_trio[2] is None:
			self.depth_trio[2] = self.depth_trio[1]
			self.depth_trio[1] = self.depth_trio[0]
			self.depth_trio[0] = int(reading.strip())
			self.cur_sum = self.depth_trio[0] + self.depth_trio[1] + self.depth_trio[2]
		else:
			self.prev_sum = self.cur_sum
			self.depth_trio[2] = self.depth_trio[1]
			self.depth_trio[1] = self.depth_trio[0]
			self.depth_trio[0] = int(reading.strip())
			self.cur_sum = self.depth_trio[0] + self.depth_trio[1] + self.depth_trio[2]
	#END def parse_reading

	def calculate_metrics(self):
		"""Incriments the counter based on Slope."""
		if self.prev_sum is None:
			# Nothing to do because no comparison can be made.
			pass
		elif self.cur_sum > self.prev_sum: # Slope is is deeper
			self.deeper_count += 1
		elif self.cur_sum < self.prev_sum: # Slope is shallower
			self.shallower_count += 1
		elif self.cur_sum == self.prev_sum: # Slope is flat
			self.flat_count += 1
	#END def calculate_metrics 
#END class DepthFinder




#Functions




#Main Function
def main():
	#Welcome to the deep... we are rolling in it #Adele
	#
	##########
	depth_file = sys.argv[1] # First arg is input file of depths

	# Initiate Depth Finder...
	print('--------------------------------')
	print('--------------------------------')
	print('Initiating Depth Finder...')
	df = DepthFinder()
	print(df)
	print('...Depth Finder initiated.')
	print('--------------------------------')
	print('--------------------------------')

	with open(depth_file) as f_movement:
		for line in f_movement:
			df.parse_reading(line)
			df.calculate_metrics()

	print(df)
#END main()

main()


























