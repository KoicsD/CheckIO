__author__ = 'KoicsD'


def checkio(text):

    def init_counts():  # initialize dictionary for counting: keys -- letters of alphabet, values -- int 0 for each
        # like a counter: initializing, for-loop and returning
        counts = {}  # init: empty-dict
        for c in [chr(i) for i in range(ord('a'), ord('z') + 1)]:  # for ascii-codes of lower-case letters
            counts[c] = 0
        return counts

    def count_letters(text):  # counts the letters of text and returns the result as a dict
        # it's a simple counter: initializing, for-loop and returning
        counts = init_counts()
        for c in text.lower():  # everything to lowercase
            if c in counts:
                    counts[c] += 1
        return counts

    def most_frequent(counts):
        # the same algorithm: init, for-loop and returning
        # init: list of most wanted letters -- empty list, highest count -- int 0
        mw_lets = []
        highest_c = 0
        # for:  key-value pairs of the dict
        for letter, count in counts.items():
            if count > highest_c:  # if count gt so-far highest
                # refresh both the mw letter and the highest c:
                mw_lets = [letter]
                highest_c = count
            elif count == highest_c:  # if count eq so-far highest
                # just append the letter to mw letters:
                mw_lets.append(letter)
        return mw_lets, highest_c

    # counting the letters of 'text' in a dict:
    counts = count_letters(text)
    # finding the most frequent one(s):
    most_wanted = most_frequent(counts)[0]
    # returning the first-in-alphabet of them:
    return min(most_wanted)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
