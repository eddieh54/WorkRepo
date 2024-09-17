import random 
import re

password = []
ranpass = []

def ran(x):

  with open(x, 'r') as file:
    alphls = []
    for line in file:
      file1line = line.strip()
      alphls.append(file1line)
    password = random.sample(alphls,5)
    return password

ranpass = ranpass + ran('alphabet.txt')
ranpass = ranpass + ran('1-9.txt')
ranpass = ranpass + ran('specialchar.txt')
random.shuffle(ranpass)
ranpass = ''.join(map(str, ranpass))
print(ranpass.title())
