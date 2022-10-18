
def main (the_list, k):
    i = 0
    j = 0
    success = False
    while (i < len(the_list)):
        while (j < len(the_list)):
            if (i != j):
                if (the_list[i] + the_list[j] == k):
                    print(the_list[i])
                    print(the_list[j])
                    success = True
            j = j + 1
            if (success):
                break
        j = 0
        i = i + 1
        if (success):
            break
    print(success)

if __name__ == "__main__":
    main([10, 15, 3, 7], 17)
