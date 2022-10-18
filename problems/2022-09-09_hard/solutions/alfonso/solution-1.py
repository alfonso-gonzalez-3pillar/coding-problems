
def main(the_list, expected):
    print('List: ', the_list)
    print('Expected:', expected)

    factor = 1
    for item in the_list:
        factor = factor * item
    print('Factor:', factor)    
    
    result = []
    for item in the_list:
        i = 0
        while (i < factor):
            i = i + 1
            if (i * item == factor):
                result.append(i)
                
    print('Result:', result)

    return 0

if __name__ == "__main__":
    main([1, 2, 3, 4, 5], [120, 60, 40, 30, 24])
    main([3, 2, 1], [2, 3, 6])
