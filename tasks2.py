def main():
    my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    """
    2А Задание
    """
    new_list = []
    for words in my_list:
        if words.isdigit():
            if len(words) == 1:
                words = f"{int(words):02}"
            elif len(words) == 2:
                words = f"{int(words)}"
        elif words.find('+') != -1 or words.find('-') != -1:
            if words.isdigit() < 10:
                words = f"{words[0]}{int(words):02}"
            else:
                words = f"{words[0]}{int(words)}"  
        new_list.append(words)
    
    i = 1
    while i < len(new_list):
        new_list.insert(i, "'")
        i += 2
    print(new_list)
    
    
    """
    2Б задание вывести из этого списка строку
    """
    for words in my_list:
        if words.isdigit():
            if len(words) == 1:
                words = f"'{int(words):02}'"
            elif len(words) == 2:
                words = f"'{int(words)}'"
        elif words.find('+') != -1 or words.find('-') != -1:
            if words.isdigit() < 10:
                words = f"'{words[0]}{int(words):02}'"
            else:
                words = f"'{words[0]}{int(words)}'"  
        print(f'{words}', end=" ")   
            
if __name__ == "__main__":
    main()