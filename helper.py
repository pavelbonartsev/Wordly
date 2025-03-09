import math
with open('russian.dict', encoding='utf-8') as wordsR:
    wordR = [i for i in wordsR.read().split()]
for i in wordR:
    if "-" in i:
        wordR.pop(wordR.index(i))
with open('english.dict', encoding="utf-8") as wordsE:
    wordE = [i for i in wordsE.read().split()]
for i in wordE:
    if "-" in i:
        wordE.pop(wordE.index(i))
ans, common = "", [wordR, wordE]
while ans != "Exit":
    st = input("Введите ту строку, которая у вас есть на данный момент: ").lower()
    lng = ""
    while lng != "1" and lng != "2":
        print('Выберите язык цифрой 1 или 2: 1 - Русский, 2 - Английский.')
        lng = input()
    meaningValues, indexes = [], []
    for i in range(len(st)):
        if st[i] != "_":
            meaningValues.append(st[i])
            indexes.append(i)
    d = []
    for i in common[int(lng) - 1]:
        a = 0
        if len(i) == len(st):
            for j in range(len(meaningValues)):
                if i[indexes[j]] == meaningValues[j]:
                    a += 1
            percento = float(a) / len(indexes)
            if percento != 0:
                d.append([i, math.trunc(percento * 100)])
    d = sorted(d, key=lambda x: x[1], reverse=True)
    print("Совпадения символов с учетом их положения:")
    for i in d:
        print(i[0] + ": совпадение данных символов на " + str(i[1]) + "%")
    print("Если вы хотите выйти из игры, введите Exit (именно так), если хотите продолжить - все, кроме Exit.")
    ans = input()
        
                
            
