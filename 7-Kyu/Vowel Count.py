def get_count(sentence):
    list = set("aeiou")
    count = 0
    for i in sentence:
        if i in list:
            count += 1
    return count
