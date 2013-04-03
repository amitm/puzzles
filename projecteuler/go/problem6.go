package main

import (
	"fmt"
)

func main() {
	sum, sum_of_squares := 0, 0
	for i := 1; i <= 100; i += 1 {
		sum += i
		sum_of_squares += i * i
	}
	fmt.Printf("%d\n", sum*sum-sum_of_squares)
}
