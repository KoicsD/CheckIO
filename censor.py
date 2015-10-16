def censor(text, word):
    lt = len(text)
    lw = len(word)
    censored = text
    for index in range(lt - lw + 1):
        if text[index : (index + lw)] == word:
            for i in range(lw):
                censored = censored[0 : (index + i)] + '*' + censored[(index + i + 1) : lt]
    return censored


def main():
    print(censor("hey hey hey", "hey"))


if __name__ == "__main__":
    main()