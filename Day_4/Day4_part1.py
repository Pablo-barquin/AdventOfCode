
def fullyContain(text):
    
    with open(text, 'r') as file:
        for lines in file:
            for splitter in ['\n', ',', '-']:
                lines = lines.split(splitter, ' ')
            
            print(lines)
            
    pass

if '__main__' == __name__:
    print(fullyContain('Day_4/Day4.txt'))
