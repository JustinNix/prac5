def main():
    word_counts = {}
    string = input("Please enter a phrase: ").split()
    for word in string:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] +=1
    words = sorted(word_counts.keys())
    width = max((len(word) for word in words))
    sorted(word_counts.values()) # doesnt work
    for word in words:
        print("{:{width}} : {:>{width}}".format(word, word_counts[word], width = width))
main()
