import random
eyes = [':', ';', '=']
noses = ['^', '.', '-']
mouth = [')', '(', 'p']
eyes_1 = random.choice(eyes)
noses_1 = random.choice(noses)
mouth_1 = random.choice(mouth)
emotion = eyes_1 + noses_1 + mouth_1
print(emotion)
