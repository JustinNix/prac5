def main():
    WORDS_IN_A_STRING = {}
    string = input("Please enter a phrase: ").split()
    for word in string:
        if word not in WORDS_IN_A_STRING:
            WORDS_IN_A_STRING[word] = 1
        else:
            WORDS_IN_A_STRING[word] +=1
    width = len(max(WORDS_IN_A_STRING.keys()))
    sorted(WORDS_IN_A_STRING.values()) # doesnt work
    for word, count in WORDS_IN_A_STRING.items():
        print("{:{width}} : {:>{width}}".format(word, count, width = width))
main()
