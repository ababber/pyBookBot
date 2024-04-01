import os
from pathlib import Path 

def main(directory):
  # gets books in books/
  books = os.listdir(f"./{directory}")

  # alternate way to check for directory existence 
  # if os.path.isdir(directory) and len(books) > 0:

  if Path(directory).is_dir() and len(books) > 0:
    for book in books:
      curr_path = f"{Path.cwd()}/{directory}/{book}"
      _, file_ext = os.path.splitext(curr_path)
      is_text_file = file_ext == ".txt"
      if (Path.cwd() / directory / book).exists() and is_text_file:
        # get contents of books/ from file and add it to memory 
        file_contents = get_contents_of_book(f"./{directory}/{book}") 
        # count the number of words in file
        word_cnt = get_num_of_words(file_contents)
        # create a char freq count
        all_char_dict = char_freq_counter(file_contents)
        # convert freq count dict into a sortable dict_list
        char_list_dict = create_list_dict(all_char_dict)
        gen_report(char_list_dict, word_cnt, book)
      else: print("Please add books to the \'books/\' folder for analysis and ensure they are \'.txt\' files")
  else: print("Please add books to the \'books/\' folder for analysis! Books can be found at https://www.gutenberg.org/")

def get_contents_of_book(filepath):
  with open(filepath) as file:
    return file.read()

def get_num_of_words(file):
  # file.read() returns as a string
  # print(type(file))
  return len(file.split())

def char_freq_counter(words):
  freq_cntr = {}
  for ch in words:
    # if a chr can be a lowercase, lower() converts it, if not it does nothing
    char = ch.lower()
    if char in freq_cntr:
      freq_cntr[char] += 1
    else: freq_cntr[char] = 1
  return freq_cntr

def create_list_dict(dict):
  list_of_dict = []
  for char in dict:
    list_of_dict.append({"char": char, "num": dict[char]})
  return list_of_dict

# defines how to sort dict_list
def sort_on(list_dict):
  return list_dict["num"]

def gen_report(char_list_dict, word_count, title):
  char_list_dict.sort(reverse=True, key=sort_on)
  print(f"--- report of books/{title} --- \n")
  print(f"{word_count} words found in document. \n")
  for item in char_list_dict:
    if item["char"].isalpha():
      print(f"The \'{item["char"]}\' character was found {item["num"]} times")
  print("\n")

main("books")
