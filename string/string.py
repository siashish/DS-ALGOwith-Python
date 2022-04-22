# https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html

# defining string in python
string = 'hello world!\
    sdhf'
print (string)

string = "Hello \"India!\
svdfdvhds\""
print(string)

string = '10'
print([ord(c) for c in string])


string = '''Hello UP!
hello yogi ji!'''
print(string)

string = """Hello Varanasi!
            hello Modi ji!"""
print(string)

# Accessing string in python
name = 'Ashish'
print('name = ',name)

print('name[0] = ',name[0])
print('name[-6] = ',name[-6])

print('name[5] = ',name[5])
print('name[-1] = ',name[-1])

print(name[1:5])
print(name[-6:6])
print(name[-6:5])
print(name[::2])
print(name[1:5:-1])


# print(name[13])
# print(name[1.5])
print(name[:13])


# updating string
# it's give error
# new = 'hello KGF'
# new[3]= 'L'
# print(new)

# Concatenation in string
str1 = 'hello'
str2 = 'KGF '
print(str1 +' '+ str2)
print(str2+str2+str2)
print(str2*3)

# iterate over string
count = 0
for l in 'Hello World':
    if (l=='l'):
        count+=1
print(count,'letters found')

print('a' in 'program')
print('d' in 'program')

str = "Shital"
print(len(str))

str = "Heena \n Pooja"
print(str)

str = "Neha"
print(list(enumerate(str)))
for id, ch in enumerate(str):
    print(id,ch)

print("He say \"what's there?\"")
print("This is \x61 \n good one")
print(R"This is \x61 \n good one")




