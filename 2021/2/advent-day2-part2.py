file = open(r'C:\Users\I00380\Documents\Advent_of_Code\2\input.txt', "r")
lines = file.read().splitlines()
input = [(string.split(' ')[0], int(string.split(' ')[1])) for string in lines]

aim = 0
depth = 0
horizontal = 0
for i in range(len(input)):
    if input[i][0] == 'forward':
        horizontal += input[i][1]  
        depth += aim*input[i][1]  
    elif input[i][0] == 'down':
        #depth += input[i][1] 
        aim += input[i][1] 
    elif input[i][0] == 'up':
         #depth -= input[i][1] 
         aim -= input[i][1] 
depth*horizontal