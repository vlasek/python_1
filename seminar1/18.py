# Проверить истинность утверждения ¬(X ⋁ Y v Z) = 
# ¬X ⋀ ¬Y ⋀ ¬Z
def uslovie (x, y,z):
    return not(x or y or z) == (not x and not y and not z)

# print (uslovie (0,1,0))
for x in range (0,2):
    for y in range (0,2):
        for z in range (0,2):
            print (uslovie (x,y,z))





