def word_count(s):
    cache = {}
    ignored = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")
    word_lower_case = s.lower()


    for chr in ignored:
        word_lower_case =word_lower_case.replace(chr, "")

    for word in word_lower_case.split():
        if word == " ":
            continue
        elif word in cache:
            cache[word] += 1
        else:
            cache[word] = 1

    return cache
        


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))