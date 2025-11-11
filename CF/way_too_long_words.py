n_lines=input()
for i in range(n_lines):
    ith_word = n_lines[i]

    if len(ith_word) > 10:
        word = ""
        word += ith_word[0]
        count = 0
        for i in range(1, len(ith_word)-1):
            count += 1

        word += count

        word += ith_word[-1]

        print(word)

    else:
        print(word)



