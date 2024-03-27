def isbalanced(s):
  c= 0
  ans=False
  for i in s:
    if i == "(" or i == "{" or i == "[": 
     c += 1
    elif i == ")" or i=="}" or i=="]":
     c-= 1
  if c < 0:
     return ans
  if c==0:
     return not ans
  return ans

t="[})({]"
f="{[)]}"
print("Given string is balanced :",isbalanced(t))
print("Given string is balanced :",isbalanced(f))