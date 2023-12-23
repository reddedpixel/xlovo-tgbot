import random
import datetime

GRN = '🟩'
YLW = '🟨'
GRY = '⬛'
wordfile = 'words.txt'

def chooseword(seed: int = 0):
    '''
    Выбирает случайное слово из числа допустимых. При seed=0 выбирает случайное значение для рандомизации.
    :param seed: значение для рандомизации
    :return: string
    '''
    if seed == 0:
        random.seed()
    else:
        random.seed(a=seed)
    with open(wordfile, 'r', encoding='utf-8') as words:
        wordlist = [a.strip() for a in words.readlines()]
        word = wordlist[random.randrange(len(wordlist))]
    return word


def checkword(guess, answer):
    '''
    Возвращает список, содержащий значения для каждой буквы в предположении: 0 - нет в слове, 2 - точное совпадение, 1 - иначе.
    :param guess: проверяемое слово
    :param answer: ответ
    :return: list
    '''
    guess = guess.lower()
    checklist = []
    with open(wordfile, 'r', encoding='utf-8') as words:
        wordlist = [a.strip() for a in words.readlines()]
        if guess not in wordlist:
            return checklist # возвращаем пустой список, если слова нет в списке допустимых
    answer = answer.lower()
    checklist = [[x, 0] for x in guess] # упорядоченный список пар (буква, значение)
    answer_dict = {x: answer.count(x) for x in answer}
    checked_letters = [] # индексы, которые уже проверены и помечены
    for i in range(5):
        if guess[i] == answer[i]:
            checklist[i][1] = 2 # если буква стоит на правильном месте, то 2
            checked_letters.append(i)
            answer_dict[answer[i]] -= 1
    for i in range(5):
        if i not in checked_letters and answer_dict.get(guess[i],0) > 0: # если индекс еще не проверен и осталось как минимум одно повторение этой буквы в ответе
            checklist[i][1] = 1
            answer_dict[guess[i]] -= 1
    checklist = [checklist[i][1] for i in range(5)] # избавляемся от букв, оставляем только значения
    return checklist


def guessreply(checklist):
    reply = ''
    for check in checklist:
        if check == 2:
            reply += GRN
        elif check == 1:
            reply+=YLW
        else:
            reply+=GRY
    return reply


def getanswer(gametype='new'):
    if gametype == 'new':
        answer = chooseword()
    if gametype == 'daily':
        today = datetime.date.today()
        answer = chooseword(seed=today.toordinal())# в качестве сида передается порядковый номер сегодняшнего дня с 01.01.0001
    return answer

def addword(word : str):
    alphabet = {'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я'}
    word = word.lower()
    if len(word) != 5:
        return False
    for letter in word:
        if letter not in alphabet:
            return False
    with open(wordfile, 'r', encoding='utf-8') as words:
        wordlist = [a.strip() for a in words.readlines()]
        if word in wordlist:
            return False
    with open('suggestions.txt', 'r', encoding='utf-8') as suggestions:
        wordlist = [a.strip() for a in suggestions.readlines()]
    wordlist.append(word)
    wordlist.sort()
    with open('suggestions.txt', 'w', encoding='utf-8') as suggestions:
        for word in wordlist:
            suggestions.write(word+'\n')
    return True