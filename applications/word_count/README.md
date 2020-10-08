# Count the words in an input string

## Input

This function takes a single string as an argument.

```
Hello, my cat. And my cat doesn't say "hello" back.
```

## Output

It returns a dictionary of words and their counts:

```
{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
```

Case should be ignored. Output keys must be lowercase.

Key order in the dictionary doesn't matter.

Split the strings into words on any whitespace.

Ignore each of the following characters:

```
" : ; , . - + = / \ | [ ] { } ( ) * ^ &
```

If the input is empty or contains only ignored characters, return an empty dictionary.



# need cache consisting of words + amount of times word occurs, must be sorted by freq
  <!--   cache = {}
    # case doesn't effect word count, so lowercase all the words
    words_lowercased = s.lower()
    # ignore chars
    ignored_chars = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")
    # iterate through string
    for chars in ignored_chars:
        # replace all non words with space
        words_lowercased = words_lowercased.replace(chars, "")
    for words in words_lowercased.split():
        print(words)
        # continue if iterating through space
        if words == "":
            continue
        if words not in cache:
            cache[words] = 1
        else:
            cache[words] += 1
    return cache
    # only count words, ignore grammar
    # if " " or non-letter than push everything between last " " or non letter into cache
    # return cache -->