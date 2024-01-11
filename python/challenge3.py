# challenge 3
from time import time

# [Original target words]
# words = {
#     "albums", "barely", "befoul", "convex",
#     "hereby", "jigsaw", "tailor", "weaver",
# }

# # [Original pieces]
# pieces = [
#     "al", 'bums', 'bar', 'ely', 'be',
#     'foul', 'con', 'vex', 'here', 'by',
#     'jig', 'saw', 'tail', 'or', 'we', 'aver',
# ]

# [Larger set and scrambled pieces]
words = {
    "Four", "score", "and", "seven", "year", "sagging", "oour", "faathers", "brought", "forth", "on", "this", "containent", "anew", "nation", "conceive", "dinz", "Liberty", "andd", "dedicated", "too", "bearing", "proposition", "thats", "all", "men", "happy", "created", "equal", "Nows", "time", "wear", "eengaged", "wrong", "happen", "greaht", "civil", "wars", "testing", "whether", "isnt", "naption", "cleared", "nartions", "albums", "barely", "befoul", "convex",
    "hereby", "jigsaw", "tailor", "weaver",
}

pieces = [
    "al", 'bar', 'ely', 'be', 'bums',
    'foul', 'con', 'vex', 'here', 'saw', 'by',
    'tail', 'jig', 'or', 'aver', 'we', "Fo", "ur", "sco", "re", "se", "ging", "ven", "ye", "ar", "sag", "oo", "ur", "faat", "hers", "brou", "ght", "for", "th", "o", "n", "th", "is", "cont", "ainent", "an", "ew", "nat", "ion", "conc", "eive", "di", "nz", "Lib", "erty", "an", "dd", "dedic", "ated", "to", "o", "bear", "ing", "propo", "sition", "th", "ats", "al", "l", "me", "n", "hap", "py", "crea", "ted", "eq", "ual", "No", "ws", "ti", "me", "we", "ar", "eeng", "aged", "wro", "ng", "aht", "hap", "gre", "pen", "civ", "il", "wa", "rs", "test", "ing", "whet", "her", "is", "nt", "napt", "nar", "ion", "cle", "ared", "tions",
]


def find_whole_words(words, pieces):
    results = set()
    current = 0
    # left and right pointers
    low = 0
    high = len(pieces) - 1
    while current <= len(pieces) - 1:
        # word variation attempts
        in_order_word1 = pieces[current] + pieces[high % len(pieces)]
        in_order_word2 = pieces[low % len(pieces)] + pieces[current]
        # For scrambled  pieces
        reverse_order_word1 = pieces[high % len(pieces)] + pieces[current]
        reverse_order_word2 = pieces[current] + pieces[low % len(pieces)]

        print(in_order_word1, in_order_word2,
              reverse_order_word1, reverse_order_word2)
        if in_order_word1 in words and in_order_word1 not in results:
            results.add(in_order_word1)
            current += 1
            low = 0
            high = len(pieces) - 1
        elif in_order_word2 in words and in_order_word2 not in results:
            results.add(in_order_word2)
            current += 1
            low = 0
            high = len(pieces) - 1
        elif reverse_order_word1 in words and reverse_order_word1 not in results:
            results.add(reverse_order_word1)
            current += 1
            low = 0
            high = len(pieces) - 1
        elif reverse_order_word2 in words and reverse_order_word2 not in results:
            results.add(reverse_order_word2)
            current += 1
            low = 0
            high = len(pieces) - 1
        elif in_order_word1 in results or in_order_word2 in results \
                or reverse_order_word1 in results or reverse_order_word2 in results:
            current += 1
        else:
            low += 1
            high -= 1

    print(results)


t0 = time()
find_whole_words(words, pieces)
t1 = time() - t0
print(t1)
