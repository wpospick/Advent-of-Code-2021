
#Notes
# Changing from a pair of variables to a single tuple with 3 values. this should help with the sliding range required for this problem.
# 




#Imports
import sys


# class DepthFinder:
# 	depth_trio = [None, None, None] # Order will be Newest, Middle, Oldest
# 	prev_sum = None
# 	cur_sum = None
# 	deeper_count = 0 
# 	shallower_count = 0
# 	flat_count = 0

# 	def __init__(self):
# 		self.depth 	= 0
# 		self.h_pos 	= 0
# 		self.aim 	= 0

# 	def __str__(self):
# 		return 'Depth:\t{self.depth} \nHorizontal Pos:\t{self.h_pos} \nAim:\t{self.aim}'.format(self=self)










#Functions
def depth_finder(depth_file):
	depth_trio = [None, None, None] # Order will be Newest, Middle, Oldest
	prev_sum = None
	cur_sum = None
	deeper_count = 0 
	shallower_count = 0
	flat_count = 0


	

	with open(depth_file) as f:
		for line in f:
			slope = "tesseract"
			
			if depth_trio[0] is None:
				depth_trio[0] = int(line.strip())
				continue
			elif depth_trio[1] is None:
				depth_trio[1] = depth_trio[0]
				depth_trio[0] = int(line.strip())
				continue
			elif depth_trio[2] is None:
				depth_trio[2] = depth_trio[1]
				depth_trio[1] = depth_trio[0]
				depth_trio[0] = int(line.strip())
				cur_sum = depth_trio[0] + depth_trio[1] + depth_trio[2]
				continue
			else:
				depth_trio[2] = depth_trio[1]
				depth_trio[1] = depth_trio[0]
				depth_trio[0] = int(line.strip())
				cur_sum = depth_trio[0] + depth_trio[1] + depth_trio[2]

			if prev_sum is None: # Replacing first_flag with using prev_sum being None.
				# Nothing to do because no comparison can be made
				slope = 'N'
			elif cur_sum > prev_sum: # New measurement window is greater than previous, thus slope is is deeper
				deeper_count += 1
				slope = 'G'
			elif cur_sum < prev_sum: # New measurement window is less than previous, thus slope is shallower
				shallower_count += 1
				slope = 'L'
			elif cur_sum == prev_sum: # New measurement window is the same as the previous, thus slope is flat
				flat_count += 1
				slope = 'E'

			# print( 		  str(prev_sum)
			# 	+ '|' 	+ str(cur_sum)
			# 	+ '| ' 	+ slope 
			# 	+ ' |(' + str(depth_trio[0]) 
			# 	+ ','	+ str(depth_trio[1])
			# 	+ ','	+ str(depth_trio[2]) + ')')

			prev_sum = cur_sum
		#END for
	#END with

	print('Shallower: ' + 	str(shallower_count))
	print('Flat: ' 		+ 	str(flat_count))
	print('Deeper: ' 	+ 	str(deeper_count))
#END depth_finder(depth_file)






#Main Function
def main():
	#Welcome to the deep... we are rolling in it #Adele
	#
	##########
	depth_finder(sys.argv[1]) #First arg is input file of depths

#END main()
main()


























