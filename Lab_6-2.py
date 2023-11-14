# Author: Caleb Moura

# Variable my_row set equal to list that contains the names of 2 people in my row
my_row = ["Dylan", "Liam"]

# Using slices, my name added to the end of the list
my_row += ["Caleb"]

# Aanother variable: my_row2 set equal to my_row
my_row2 = my_row

# Statement that prints my_row2
print("my_row2:", my_row2)

# Statement that removes the value at index 1 from my_row
del my_row[1]

# Statement that prints my_row
print("my_row:", my_row)

# After running: my name replaces Liam's in the order of the list
# ex: ['Dylan','Caleb']