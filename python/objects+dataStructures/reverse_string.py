#python script to reverse a string
# class Solution:
#      def reverseString(self, s):
#        """
#         :type s: str
#          :rtype: str
#          """

#         s1 = list(s)
#         s1.reverse()
#         return ''.join(s1)


## Python code to reverse a string
# using extended slice syntax
'''Extended slice offers to put a “step” field as
[start,stop,step], and giving no field as start and stop
indicates default to 0 and string length respectively and “-1”
denotes starting from end and stop at the start, hence reversing string.'''
# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string

#-------------------------

# Python code to reverse a string
# using loop
'''we call a function to reverse a string,
which iterates to every element and intelligently
join each character in the beginning so as to obtain the reversed string.'''
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

s = "Geeksforgeeks"

print ("The original string  is : ",end="")
print (s)

print ("The reversed string(using loops) is : ",end="")
print (reverse(s))

#----------------------------------------------
# Python code to reverse a string
# using recursion
'''string is passed as an argument to a recursive
function to reverse the string.
-In the function, the base condition is that if the length of the string
is equal to 0, the string is returned.
-If not equal to 0, the reverse function is recursively called to slice the
part of the string except the first character and concatenate
the first character to the end of the sliced string.'''

def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]

s = "Halleluya"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))


# Python code to reverse a string
# using reversed()
 '''The reversed() returns the reversed iterator of the given string
 and then its elements are joined empty string separated using join().
 And reversed order string is formed.
 '''
# Function to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string

s = "Geeksforgeeks"

print ("The original string  is : ",end="")
print (s)

print ("The reversed string(using reversed) is : ",end="")
print (reverse(s))
