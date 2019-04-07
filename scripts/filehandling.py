f = open("scripts/text.txt", "r")
print(f.read()) 
f.close()

x = 0
for x in range(25): 
    f = open("scripts/text.txt", "a")
    f.write("   hahahahahahahahaha   ")
    f.close()
    x += 1

f = open("scripts/text.txt", "r")
print(f.read()) 
f.close() 