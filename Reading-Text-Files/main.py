# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from importlib.resources import contents


def read_file_content(filename):
    # [assignment] Add your code here 
  
    with open(filename) as f:
     contents = f.read()

    
    return contents


    





def word_counts():
    text = read_file_content("./story.txt")
    words = text.split()
    counts = dict()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
   
    return counts

print( read_file_content('./story.txt'), '\n' )
print(word_counts())


