from random import *


ans, word = '', ''
with open('russian.dict', encoding='utf-8') as wordsR:
    wordR = [i for i in wordsR.read().split()]
for i in wordR:
    if "-" in i:
        wordR.pop(wordR.index(i))
with open('english.dict', encoding="utf-8") as wordsE:
    wordE = [i for i in wordsE.read().split()]
for i in wordE :
    if "-" in i:
        wordE.pop(wordE.index(i))
while ans != 'Exit':
    lng = ""
    while lng != "1" and lng != "2":
        print('Выберите язык цифрой 1 или 2: 1 - Русский, 2 - Английский.')
        lng = input()
    if str(lng) == '1':
        word = wordR.pop(randint(0, len(wordR) - 1)).lower()
    elif str(lng) == '2':
        word = wordE.pop(randint(0, len(wordE) - 1)).lower()
    notInWord, wrongPos, inWord = [], [], []
    emit, ok = list('_' * len(word)), False
    print("".join(emit))
    guess = ""
    while len(guess) != len(word):
        print('Введите сюда свою догадку, она должна состоять из такого же количества символов, что и угадываемое слово, в данном случае - ' + str(len(word)) + ".")
        guess = input()
    for _ in range(6):
        for i in range(len(word)):
            if guess == word:
                ok = True
                break
            else:
                if guess[i] in word and word.rfind(guess[i]) != guess[i] and guess[i] not in inWord:
                    wrongPos.append(guess[i])
                if guess[i] == word[i]:
                    emit[i] = word[i]
                    wrongPos = list(set(wrongPos))
                if guess[i] in word and list(word).count(guess[i]) == emit.count(guess[i]):
                    wrongPos.remove(guess[i])
                if guess[i] not in word:
                    notInWord.append(guess[i])
                    notInWord = list(set(notInWord))
        if ok:
            break
        print('Буквы, которые у вас есть на данный момент:')
        print("".join(emit))
        print('Буквы, которые вы ввели, но в слове их не оказалось:')
        print(", ".join(list(set(notInWord))))
        print('Буквы, которые введены и есть в слове, но располагаются на неправильных позициях:')
        print(", ".join(list(set(wrongPos))))
        guess = ""
        while len(guess) != len(word):
            print('Введите сюда свою догадку, она должна состоять из такого же количества символов, что и угадываемое слово, в данном случае - ' + str(len(word)) + ".")
            guess = input()
    if ok:
        print('Слово угадано!')
    else:
        print(f'Слово не угадано. Ответом было слово {word}.')
    print("Если вы хотите выйти из игры, введите Exit (именно так), если хотите продолжить - все, кроме Exit.")
    ans = input()
print('Удачи!')
