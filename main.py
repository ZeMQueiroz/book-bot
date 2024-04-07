def main():
  book = 'books/frankenstein.txt'
  text = open_book_text(book)
  count = word_count(text)
  repeat = char_repetition(text)
  sort = sort_for_report(repeat)
  print(f"--- Begin report of {book} ---")
  print(f"{count} wordds found in the document")
  print()

  for item in sort:
    if not item["char"].isalpha():
          continue
    print(f"The '{item['char']}' character was found {item['num']} times")
  print(f"--- End of report ---")

def open_book_text(book):
  with open(book) as f:
    text = f.read()
  return text

def word_count(text):
  return len(text.split())

def char_repetition(text):
  char_count = {}
  for char in text:
    lowered = char.lower()
    if lowered in char_count:
      char_count[lowered] += 1
    else:
      char_count[lowered] = 1
  return char_count

def sort_on(dict):
    return dict["num"]

def sort_for_report(dict):
  sorted_list = []
  for key in dict:
    sorted_list.append({"char": key, "num": dict[key]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

main()