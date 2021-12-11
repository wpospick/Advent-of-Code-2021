#Imports
import sys


#Main Function
def main():
	depth_file = 'input.txt'
	prev_val = -666
	cur_val = -666
	deeper_count = 0 
	shallower_count = 0
	flat_count = 0


	depth_file = sys.argv[1] #First arg is input file of depths

	with open(depth_file) as f:
		first_line = True # First line flag. Don't want the first row to count as an increase in depth
		for line in f:
			cur_val = int(line.strip())
			slope = "tesseract"
			
			if first_line:
				first_line = False # Kill first line flag
				slope = 'N'
			elif cur_val > prev_val: 						# New depth reading is greater than previous, thus slope is is deeper
				deeper_count  = deeper_count + 1
				slope = 'G'
			elif cur_val < prev_val: 						# New depth reading is less than previous, thus slope is shallower
				shallower_count = shallower_count + 1
				slope = 'L'
			elif cur_val == prev_val: 						# New depth reading is the same as the previous, thus slope is flat
				flat_count = flat_count + 1
				slope = 'E'

			dif = cur_val - prev_val
			# print(str(prev_val) + ' | ' + str(cur_val) + ' | ' + slope + ' | ' + str(dif))
			# print(str(prev_val) + ' | ' + str(cur_val) + ' | ' + slope)

			prev_val = cur_val
		#END for
	#END with

	print('Shallower: ' + 	str(shallower_count))
	print('Flat: ' 		+ 	str(flat_count))
	print('Deeper: ' 	+ 	str(deeper_count))

#END main
main()


























