# Ynea I jnust gnadded y to a lnist of vnowels wnhat ynou gnonna do bnitch
vowels: list = ['a', 'e', 'i', 'o', 'u']
blacklist: list = ['m', 'l']


def gnuize_word(word: str) -> str:
    length: int = len(word)
    if length <= 2 or word[0] in blacklist:
        return word
    elif word[0] in vowels:
        return "gn" + word
    else:
        if word[0] not in vowels and word[1] in vowels:
            return word[:1] + "n" + word[1:]


def gnuize_sentence(sentence: str) -> str:
    return " ".join([gnuize_word(word) for word in sentence.split(" ")])


if __name__ == "__main__":
    while True:
        user_input = input("translate: ")
        print(gnuize_sentence(user_input))
