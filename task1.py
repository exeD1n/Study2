def main():
    a = 15 * 3
    b = 15 / 3
    c = 15 // 2
    d = 15 ** 2
    
    array_expressions = [a, b, c, d]
    print(array_expressions)
    
    for expressions in array_expressions:
        print(type(expressions))

if __name__ == "__main__":
    main()