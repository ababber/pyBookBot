import main
from test_helpers import freq_cntr_test
from test_helpers import list_dict_test
import json
import os
from pathlib import Path
import subprocess

directory = "books"
books = os.listdir(f"./{directory}")

# ensure there is a books/ for source material
def test00():
  assert os.path.isdir(directory) == True, "should have books/ in project directory"

# ensure at least one book exists
def test01():
  assert len(books) > 0, "should have at least a book to run project on" 

# check that all source documents are .txt
def test02():
  for book in books:
    curr_path = f"{Path.cwd()}/{directory}/{book}"
    _, file_ext = os.path.splitext(curr_path)
    assert file_ext == ".txt", "should have .txt file type"

# check that the contents of frankenstein.txt are extracted correctly
def test03():
  book_path = f"./{directory}/{books[0]}"
  with open(book_path) as test_file:
    assert main.get_contents_of_book(book_path) == test_file.read(), f"should return contents of {books[0]}"

def test04():
  with open("./test_helpers/word_count_test.json", "r") as f:
    word_count = json.load(f)
    for book in books:
      curr_path = f"{Path.cwd()}/{directory}/{book}"
      file_contents = main.get_contents_of_book(curr_path)
      assert main.get_num_of_words(file_contents) == word_count[book], "should have the same number of word counts"

def test05():
  test_data = freq_cntr_test.get_data()
  for book in books:
    curr_path = f"{Path.cwd()}/{directory}/{book}"
    file_contents = main.get_contents_of_book(curr_path)
    assert main.char_freq_counter(file_contents) == test_data[book], "should have the same frequency counter dictionary"

def test06():
  test_data = list_dict_test.get_data()
  for book in books:
    curr_path = f"{Path.cwd()}/{directory}/{book}"
    file_contents = main.get_contents_of_book(curr_path)
    freq_cntr = main.char_freq_counter(file_contents) 
    list_dict = main.create_list_dict(freq_cntr)
    for item in list_dict:
      is_item_here = False
      for data in test_data[book]:
        if item["char"] == data["char"] and item["num"] == data["num"]:
          is_item_here = True
      assert is_item_here == True, "should have the same number of characters" 

# TODO finish final test by writing gen_report() to file and comparing with test data
# def test07():
#   for book in books:
#     report_filepath = f"{Path.cwd()}/test_helpers/reports/{book}"
#     book_filepath = f"{Path.cwd()}/{directory}/{book}"
#     file_contents = main.get_contents_of_book(book_filepath)
#     num_of_words = main.get_num_of_words(file_contents)
#     freq_cntr = main.char_freq_counter(file_contents) 
#     list_dict = main.create_list_dict(freq_cntr)
#     with open(report_filepath) as test_file:

def test08():
  subprocess.run(["bash", "./test_helpers/test_helper0.sh"])
  assert main.main("books_test0") == "Please add books to the \'books/\' folder for analysis! Books can be found at https://www.gutenberg.org/", "should return correct response for empty directory"
  subprocess.run(["bash", "./test_helpers/test_helper1.sh"])
  assert main.main("books_test0") == "Please add books to the \'books/\' folder for analysis and ensure they are \'.txt\' files"
  subprocess.run(["bash", "./test_helpers/test_cleanup.sh"])
