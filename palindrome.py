# This code is a better, more pythonic way to find the whether a given number or string is palindrome or not

s = input('Enter your input: ')
l = len(s)

if l%2!=0:
  if s[:l//2] == s[:l//2:-1]:
    print(f'String {s} is palindrome')
  else:
    print(f'String {s} is not a palindrome')
else:
  if s[:l//2] == s[:l//2-1:-1]:
    print(f'String {s} is palindrome')
  else:
    print(f'String {s} is not a palindrome')
    
# why I used slicing over other methods?
# Other methods that can be used to find whether a number/string is palindrome include reversing string
# or comparing first elemennt of string with last element, second element with second last element and so on.
# All above operations would require a for loop, in which we still have to use comparison operation.
# Using this way, the complexity is O(len(s)), which is linear and requires less operations than needed
