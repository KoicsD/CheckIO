__author__ = "KoicsD&VeghA"


def check_pangram(text: str):
    s_letters = set()
    s_alphabet = set()
    for c in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
        s_alphabet.add(c)
    for c in text.lower():
        if c in s_alphabet:
            s_letters.add(c)
    return s_alphabet == s_letters


if __name__ == "__main__":
    assert check_pangram("The quick brown fox jumps over the lazy dog.") == True, "1st example"
    assert check_pangram("ABCDEF.") == False, "2nd example"
