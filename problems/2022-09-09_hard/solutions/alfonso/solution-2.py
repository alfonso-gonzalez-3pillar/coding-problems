
def main(my_array):
    result = [1] * len(my_array)
    i = 0
    j = 0
    
    while True:
        if i != j:
            result[i] = result[i]  * my_array[j]
        j = j + 1
        if j >= len(my_array):
            j = 0
            i = i + 1
        if i >= len(my_array):
            break
        
    print(result)

if __name__ == "__main__":
    main([1, 2, 3, 4, 5])
    main([3, 2, 1])
