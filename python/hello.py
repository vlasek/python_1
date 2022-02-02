print ('hello world')
a=1
print(a)
list = [1,4,6,8]

print (list)

# a r w+ r+ - ключи для 
colors = ['red', 'green', 'blue']
data = open ('file.txt', 'w')
data.writelines(colors)
data.write('\nLINE\n')
data.write('LINE646\n')

data.close()
