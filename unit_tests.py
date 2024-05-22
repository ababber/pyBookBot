import pyBookBot
from test_helpers import freq_cntr_test
from test_helpers import list_dict_test
import json
import os
from pathlib import Path
import subprocess

directory = "books"
books = os.listdir(f"./{directory}")

def test_books_dir_exists():
  assert os.path.isdir(directory) == True, "should have books/ in project directory"

def test_a_book_exists_in_books_dir():
  assert len(books) > 0, "should have at least a book to run project on" 

def test_book_formats():
  for book in books:
    curr_path = f"{Path.cwd()}/{directory}/{book}"
    _, file_ext = os.path.splitext(curr_path)
    assert file_ext == ".txt", "should have .txt file type"

def test_books_extracted_correctly():
  book_path = f"./{directory}/{books[0]}"
  with open(book_path) as test_file:
    assert pyBookBot.get_contents_of_book(book_path) == test_file.read(), f"should return contents of {books[0]}"

def test_words_counted_correctly():
  with open("./test_helpers/word_count_test.json", "r") as f:
    word_count = json.load(f)
    for book in books:
      curr_path = f"{Path.cwd()}/{directory}/{book}"
      file_contents = pyBookBot.get_contents_of_book(curr_path)
      assert pyBookBot.get_num_of_words(file_contents) == word_count[book], "should have the same number of word counts"

def test_frequency_counter_created_correctly():
  test_data = freq_cntr_test.get_data()
  for book in books:
    curr_path = f"{Path.cwd()}/{directory}/{book}"
    file_contents = pyBookBot.get_contents_of_book(curr_path)
    assert pyBookBot.char_freq_counter(file_contents) == test_data[book], "should have the same frequency counter dictionary"

def test_list_dict_created_correctly():
  test_data = list_dict_test.get_data()
  for book in books:
    curr_path = f"{Path.cwd()}/{directory}/{book}"
    file_contents = pyBookBot.get_contents_of_book(curr_path)
    freq_cntr = pyBookBot.char_freq_counter(file_contents) 
    list_dict = pyBookBot.create_list_dict(freq_cntr)
    for item in list_dict:
      is_item_here = False
      for data in test_data[book]:
        if item["char"] == data["char"] and item["num"] == data["num"]:
          is_item_here = True
      assert is_item_here == True, "should have the same number of characters" 

def test_reports_generated_correctly():
  for book in books:
    data_filepath = f"{Path.cwd()}/test_helpers/reports/{book}"
    book_filepath = f"{Path.cwd()}/{directory}/{book}"
    file_contents = pyBookBot.get_contents_of_book(book_filepath)
    num_of_words = pyBookBot.get_num_of_words(file_contents)
    freq_cntr = pyBookBot.char_freq_counter(file_contents) 
    list_dict = pyBookBot.create_list_dict(freq_cntr)
    pyBookBot.gen_report(list_dict, num_of_words, book)
    report_filepath = f"{Path.cwd()}/reports/report_{book}"
    with open(data_filepath) as d, open(report_filepath) as r:
      assert d.read() == r.read(), "should generate correctly formatted report to a file"
    subprocess.run(["bash", "./test_helpers/test_cleanup0.sh"])

def test_error_responses():
  subprocess.run(["bash", "./test_helpers/test_helper0.sh"])
  assert pyBookBot.main("books_test0") == "Please add books to the \'books/\' folder for analysis! Books can be found at https://www.gutenberg.org/", "should return correct response for empty directory"
  subprocess.run(["bash", "./test_helpers/test_helper1.sh"])
  assert pyBookBot.main("books_test0") == "Please add books to the \'books/\' folder for analysis and ensure they are \'.txt\' files"
  subprocess.run(["bash", "./test_helpers/test_cleanup1.sh"])
