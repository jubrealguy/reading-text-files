# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        story = f.read()
        return story

def count_words():
    text = read_file_content("./story.txt")
    splitted_text = text.split()

    count = {}
    for word in splitted_text:
        if word in count :
            count[word] += 1
        else:
            count[word] = 1

    return count

print(count_words())
