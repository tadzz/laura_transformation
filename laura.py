from csv import reader, writer

# This is the function with the logic (input array, output array of arrays with the leading item)

def transpose_add(arr):
	# Output Matrix Array (array of arrays)
	matrarr = []
	
	# For every item in the Input Array, add all the items in the rest of the Array (unless they're empty) 
	for i in arr:
		if i != '':
			temparr = [i,]
			for n in arr:
				if n != i:
					if n != '':
						temparr.append(n)
			matrarr.append(temparr)
	return matrarr



# This is the read/write part. It just reads the file, and for every line it calls the function above and writes a line for each item.

with open('csv_input.csv') as csvinput:
	csvdata = reader(csvinput)
	with open('csv_output.csv', 'w') as file:
		csv_writer = writer(file)
		for row in csvdata:
			parsed_items = transpose_add(row)
			for n in parsed_items:
				csv_writer.writerow(n)
			