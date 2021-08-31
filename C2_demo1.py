#Brandon Skaggs
#8/31/2021
#Filename: C2_demo1
#Purpose: Calculate the size of a tract of land in acres, given the square feet.

#declare variables
tractSize = 0.0 #floating decimal type of data
acres = 0.0

#declare a constant
SQ_FT_PER_ACRE = 43560

#get the square feet in the tract
tractSize = float(input('Enter the number of square feet in the tract:  '))

#calculate the acreage
acres = tractSize / SQ_FT_PER_ACRE

#give the answer
print(f'The size of the tract in acres is {acres:,.1f}')

            
