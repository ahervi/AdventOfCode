file = open(r'C:\Users\I00380\Documents\Advent_of_Code\1\input.txt', "r")
lines = file.read().splitlines()
input = [int(numeric_string) for numeric_string in lines]
counter = 0
for i in range(1, len(input)-2):
    if input[i+2] > input[i-1]:
        counter+=1  
counter