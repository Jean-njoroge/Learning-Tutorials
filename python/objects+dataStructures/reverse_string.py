class Solution:
     def reverseString(self, s):
       """
        :type s: str
         :rtype: str
         """

#         s1 = list(s)
#         s1.reverse()
#         return ''.join(s1)

###2 option
s = 'Hello'
class Solution:
     def reverseString(self, s):
         return s[::-1]
reverseString(s)     
