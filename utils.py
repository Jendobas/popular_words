from translate import Translator


def translates(path, ignore, count):
    translator = Translator(from_lang='English', to_lang='Russian')
    temp = {}
    results = []

    with open(path, 'r') as f:
        # ignore = ['and', 'you', 'the', 'for', 'can', 'app', 'url', 'code', 'web']

        for line in f:
            for word in line.split():
                word = word.lower().strip(',').strip('.').strip('!').strip('"').strip('?')
                if len(word) > 2 and word not in ignore and word.isalpha():
                    if word not in temp:
                        temp[word.strip(',').strip('.').strip('(').strip(')').lower()] = 1
                    else:
                        temp[word] += 1

    temp = sorted(temp.items(), key=lambda x: x[1])
    if count:
        res = [i for i in temp if i[1] >= count]
    else:
        res = [i for i in temp]

    for i in res:
        result = translator.translate(i[0]).lower()
        results.append(f'{i[0]} - {result} ({i[1]} раз)')

    return results
