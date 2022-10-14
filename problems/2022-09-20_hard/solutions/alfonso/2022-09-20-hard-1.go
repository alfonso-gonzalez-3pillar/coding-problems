package main

import "fmt"

func process(word string, distinctChars int, expectedResult string) bool {
	fmt.Println("Input: ", word)
	var totalLen int = len(word)
	var pointer int = 0
	var step int  = 2
	var returnValue string = ""

	for {
		if (pointer + step) <= totalLen {
			var substr string = string(word[pointer:pointer + step])
			var charDict = make(map[string]int)
			for _, char := range substr {
				charDict[string(char)] = charDict[string(char)] + 1
				if charDict[string(char)] == distinctChars {
					returnValue = substr
				}
			}
		}
		
		pointer++
		
		if pointer == totalLen {
            pointer = 0
            step++
		}

		if (pointer >= totalLen || step > (totalLen - 1) || len(returnValue) > 0) {
			break
		}
	}
	fmt.Println("Expected: ", expectedResult, " result: ", returnValue)
	return returnValue == expectedResult
}

func main() {
    process("abcba", 2, "bcb")
	process("xababa", 2, "aba")
}
