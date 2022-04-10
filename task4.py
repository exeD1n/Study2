def main():
    array_words =['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
    for words in array_words:
        words_list = words.split()
        print(f'Привет, {words_list[-1].title()}!')

if __name__ == "__main__":
    main()