def main():
  # get contents of books/ from file and add it to buffer
  file_contents = get_contents_of_book("./books/frankenstein.txt") 
  # count the number of words in file
  word_count = get_num_of_words(file_contents)
  print(word_count)

def get_num_of_words(file):
  return len(file.split())

def get_contents_of_book(filepath):
  with open(filepath) as file:
    return file.read()

main()