def main():
  # get contents of books/ from file and add it to buffer
  file_contents = get_contents_of_book("./books/frankenstein.txt") 

  # count the number of words in file
  word_cnt = get_num_of_words(file_contents)

  # create a char freq count
  all_char_dict = char_freq_counter(file_contents)

  # convert freq count dict into a sortable dict_list
  char_list_dict = create_list_dict(all_char_dict)

  gen_report(char_list_dict, word_cnt)

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
def sort_on(dict_list):
  return dict_list["num"]

def gen_report(char_list_dict, word_count):
  char_list_dict.sort(reverse=True, key=sort_on)
  print("--- report of books/frankenstein.txt --- \n")
  print(f"{word_count} words found in document. \n")
  for item in char_list_dict:
    if item["char"].isalpha():
      print(f"The \'{item["char"]}\' character was found {item["num"]} times")

main()
