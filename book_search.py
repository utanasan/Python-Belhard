#Есть архив с книгами, необходимо сделать программу помощник читателя, прошу использовать ООП. Программа должна принять от пользователя слово или некоторое 
#количество слов, в ответ программа должна выдать все названия книг в тексте которых есть все введенные пользователем слова.


import glob
final_book_list = []
book_list = [f for f in glob.glob("*.txt")]

class Search:
    def __init__(self):
        pass

    def check_word(self,word):
        for filename in book_list:
          try:
            with open(filename, mode='r', encoding='windows-1251') as file:
                line = True
                while line:
                    line = file.readline()
                    if word.lower() in line.lower():
                        final_book_list.append(filename)
                        break
          except UnicodeDecodeError:
            with open(filename, mode='r', encoding='utf-8') as file:
                  line = True
                  while line:
                      line = file.readline()
                      if word.lower() in line.lower():
                          final_book_list.append(filename)
                          break

    def output(self):
        if not final_book_list:
            print(f"В представленных книгах нет слова/сочетания слов '{word}'")
        else:
            print(f"Слово/сочетание слов '{word}' найдено в следующих книгах: {final_book_list}")

word=input("Введите искомое слово: ")
obj=Search()
obj.check_word(word)
obj.output()









