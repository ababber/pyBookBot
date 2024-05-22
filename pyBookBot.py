import sys
import os
import subprocess
from pathlib import Path 

def main(directory):
  # gets books from books/
  books = os.listdir(f"./{directory}")

  # alternate way to check for directory existence 
  # if os.path.isdir(directory) and len(books) > 0:

  if Path(directory).is_dir() and len(books) > 0:
    for book in books:
      curr_path = f"{Path.cwd()}/{directory}/{book}"
      _, file_ext = os.path.splitext(curr_path)
      is_text_file = file_ext == ".txt"
      # TODO: review the following line
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
      else: return "Please add books to the \'books/\' folder for analysis and ensure they are \'.txt\' files"
  else: return "Please add books to the \'books/\' folder for analysis! Books can be found at https://www.gutenberg.org/"

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

# TODO find a way to sort freq_cntr directly
def create_list_dict(dict):
  list_of_dict = []
  for char in dict:
    list_of_dict.append({"char": char, "num": dict[char]})
  return list_of_dict

# defines how to sort list_dict 
def sort_on(list_dict):
  return list_dict["num"]

# all reports logic isolated in gen_report(), i.e. char frequency sort and check for alphabetic chars
def gen_report(char_list_dict, word_count, title):
  char_list_dict.sort(reverse=True, key=sort_on)
  report = []
  report.append(f"--- report of books/{title} ---\n")
  report.append("\n")
  report.append(f"{word_count} words found in document.\n")
  report.append("\n")
  for item in char_list_dict:
    if item["char"].isalpha():
      report.append(f"The \'{item["char"]}\' character was found {item["num"]} times\n")
  subprocess.run(["bash", "./reports_setup.sh"])
  with open(f"./reports/report_{title}", "w") as f:
    for line in report:
      f.write(line)

if __name__ == "__main__":
  sys.tracebacklimit = 0
  if len(sys.argv) == 2 and sys.argv[1] == "test.sh":
    test = sys.argv[1]
    subprocess.run(["bash", f"{test}"])
  else:
    raise Exception("Test file argument missing...did you mean to type: 'python pyBookBot.py test.sh'?")
