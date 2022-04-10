def main():
    array_words = [57.8, 45.05, 96.08, 46.51, 97, 34.1, 23.16, 99.99, 1000, 235.12, 89, 30, 5.23, 65.89, 77, 33, 47.19, 46.07]
    for cent in array_words:
        kopeiki = 100*(cent%1)
        if kopeiki <= 0:
            print(f"{int(cent)}руб {(kopeiki)}0коп", end=', ')
        elif  10 > kopeiki > 0:
            print(f"{int(cent)}руб 0{round(kopeiki)}коп", end=', ')
        else:
            print(f"{int(cent)}руб {round(kopeiki)}коп", end=', ')
    print(f"\n")    
    
        
    """
    2Б сортированный список и вывод цен, доказательство что это список
    """
    array_sort_max = sorted(array_words)
    for cent in array_sort_max:
        kopeiki = 100*(cent%1)
        if kopeiki <= 0:
            print(f"{int(cent)}руб {(kopeiki)}0коп", end=', ')
        elif  10 > kopeiki > 0:
            print(f"{int(cent)}руб 0{round(kopeiki)}коп", end=', ')
        else:
            print(f"{int(cent)}руб {round(kopeiki)}коп", end=', ')
    print()
    print(f"{type(array_words)}\n")
    
    
    """
    2В новый список но сортировка по убыванию и вывод цен 
    """
    sort_list_min=[]
    for i in array_words:
        sort_list_min.append(i)
    sort_list_min.sort(reverse=True)
    for cent in sort_list_min:
        kopeiki = 100*(cent%1)
        if kopeiki <= 0:
            print(f"{int(cent)}руб {(kopeiki)}0коп", end=', ')
        elif  10 > kopeiki > 0:
            print(f"{int(cent)}руб 0{round(kopeiki)}коп", end=', ')
        else:
            print(f"{int(cent)}руб {round(kopeiki)}коп", end=', ')
    print(f"\n")
    
    """
    2Г вывод 5 цен самых дорогих товаров с наименьшим кодом
    допустим у нас есть какой либо список
    """
    array_new_two = [57.8, 45.05, 96.08, 46.51, 97, 34.1, 23.16, 99.99, 1000, 235.12, 89, 30, 5.23, 65.89, 77, 33, 47.19, 46.07]
    array_new_two.sort()
    big_cent = array_new_two[-5:]
    for cent in big_cent:
        kopeiki = 100*(cent%1)
        if kopeiki <= 0:
            print(f"{int(cent)}руб {(kopeiki)}0коп", end=', ')
        elif  10 > kopeiki > 0:
            print(f"{int(cent)}руб 0{round(kopeiki)}коп", end=', ')
        else:
            print(f"{int(cent)}руб {round(kopeiki)}коп", end=', ')
    
if __name__ == "__main__":
    main()