def word_count(filename):
    with open(filename) as file_object:
        # Read file contents
        contents = file_object.read()
        
        # Extract each word separated by whitespace from the file into a list
        word_list = contents.split()
        
        return len(word_list)

print('The file alice.txt has about %d words.' % word_count('alice.txt'))