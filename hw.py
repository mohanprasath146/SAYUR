print("-----------PROBLEM 1----------")
print("------------------------------")
sen = "hellllllllllo"
new = ""
for word in sen: 
    if word not in new :
        new += word

print (new)

print("------------------------------")
print("-----------PROBLEM 2----------")
print("------------------------------")
str="SAYUR"
for i in range(0, len(str)):  #  0 1 2 3 4 
    for j in range(0, i + 1): #  0 | 0 1 | 0 1 2 | 0 1 2 3 | 0 1 2 3 4
        print(str[j], end=" ")
    print("")

print("------------------------------")
print("-----------PROBLEM 3----------")
print("------------------------------")
text = "abcdefg"
newtext = ""

for i in range(0, len(text), 2):  # 0 2 4 6 
    newtext += text[i:i+2]  
    if i + 2 < len(text):  # 2 < 7 | 4 < 7 | 6 < 7 
        newtext += " "

print(newtext)

print("------------------------------")