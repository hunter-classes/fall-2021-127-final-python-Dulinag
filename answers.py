
#This functions takes a list of numbers and if its increasing it returns True else it returns False. The first value  is the starting point that determines everything if it decreases or increases.

def isIncreasing(list2):
  c = list2[0]
  for num in list2[1:-1]:
    if c > num:
      return False 
  return True

#This function takes numbers from list and converts it to an integer. For this function to work I added a empty string to the string of that number and returned it.
 
def NumConvert(list_3):
  result = ""
  for num in list_3:
    result = result + str(num)
  return result

##This is binary conversion. For This I made result = 0 and added it to val which is 1 so it would start at 1 and times that by 2 if the character = "1".

def BinConvert(bin_1):
  result = 0
  val = 1
  for i in bin_1[::-1]:
    if i == "1":
      result += val
    val = val * 2
  return result



def main():

  print("------------------- Question 1 ----------------")
  print("This is the increasing Function which returns True if a value is increasing in a list, if not it returns False")
  print()
  print("Test for isIncreasing function:")
  list3 = [4,5,8,9,10]
  print(list3, "is")
  print(isIncreasing(list3))
  print()
  print("This test shows the use negative numbers in the middle which returns False as it is a decrease:")
  print()
  list3_12 = [40, -50, -60, 90]
  print(list3_12,"is")
  print(isIncreasing(list3_12))
  print()



  print("------------------- Question 2 ----------------")
  print("This is Number Conversion which take a list of single digit numbers and converts it to an integer")
  print()
  list4 = [3,5,1]
  print("These are the digits:",list4)
  print("This is the conversion:")
  print(NumConvert(list4))
  print()
  print("This is a another example:")
  print()
  list41 = [4,5,6,7,8,9]
  print("These are the digits:",list41)
  print(NumConvert(list41))
  print()

  print("------------------- Question 3 ----------------")
  print("This is Binary Conversion which takes a string representing a binary number and returns an integer with that number converted to decimal.")
  print()
  print("Converts 11101 to:")
  print(BinConvert("11101"))
  print()
  print("This is another example of Binary Conversion:")
  print("Converts 101 to:")
  print(BinConvert("101"))


main()