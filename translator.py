
# Ynea I jnust gnadded y to a lnist of vnowels wnhat ynou gnonna do bnitch
vowels: list = ['a', 'e', 'i', 'o', 'u']
blacklist: list = ['m', 'l']

def gnuize_word(word: str) -> str:
    length: int = len(word)
    if length <= 2 or word[0] in blacklist: return word
    elif word[0] in vowels: word = "gn"+word 
    else: 
        if word[0] not in vowels and word[1] in vowels:
            word = word[:1] + "n" + word[1:]

    return word

def gnuize_sentence(sentence: str) -> str:
    split_sentence: list = sentence.split(" ")
    gnuized_sentence = ""
    for word in split_sentence:
        gnuized_sentence += gnuize_word(word) + " "
    return gnuized_sentence

if __name__ == "__main__":
    while True:
        user_input = input("translate: ")
        print(gnuize_sentence(user_input))
