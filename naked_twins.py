def naked_twins(values):

   all_digits = '123456789'

    for unit in unitlist:
        d = dict()
        for digit in all_digits:
       	    boxes_with_digit = ''.join([box for box in unit if digit in values[box]])

       	    if len(boxes_with_digit) == 4:

       	   	    if (boxes_with_digit not in d.keys()):
       	   	   	    d[boxes_with_digit] = digit
       	   	   	else:
       	   	   	    digits = d[boxes_with_digit] + digit

       	   	   	    for box in unit:
       	   	   	    	if (box in boxes_with_digit):
       	   	   	    		assign_value(values, box, digits)

       	   	   	    	else:
       	   	   	    		assign_value(values, box, values[box].replace(digits[0], ""))
       	   	   	    		assign_value(values, box, values[box].replace(digits[1], ""))
    return values
    











