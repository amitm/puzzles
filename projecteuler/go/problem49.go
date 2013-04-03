package main

import (
	"fmt"
	"math"
	"sort"
)

func seive(size int) []byte {
	size += 1
	s := make([]byte, size)
	for i := 0; i < size; i += 1 {
		s[i] = 1
	}
	limit := int(math.Sqrt(float64(size)))
	for i := 2; i < limit; i += 1 {
		if s[i] == 1 {
			for j := i + i; j < size; j += i {
				s[j] = 0
			}
		}
	}
	return s
}

var sort_temp []int

func sort4digit(x int) int {
	if len(sort_temp) == 0 {
		sort_temp = make([]int, 4)
	}
	for i := 0; i < 4; i += 1 {
		sort_temp[i] = x % 10
		x /= 10
	}
	sort.Ints(sort_temp)
	for i := 0; i < 4; i += 1 {
		x += int(math.Pow(10, float64(i))) * sort_temp[3-i]
	}
	return x
}

func inSlice(slice []int, value int) bool {
	for _, v := range slice {
		if v == value {
			return true
		}
	}
	return false
}

func main() {
	s := seive(10000)
	perms := make(map[int][]int, 2000)
	for i := 1000; i < 10000; i += 1 {
		if s[i] == 1 {
			sorted := sort4digit(i)
			if sorted < 1000 {
				continue
			}
			list, ok := perms[sorted]
			if !ok {
				perms[sorted] = make([]int, 1, 4)
				perms[sorted][0] = i
			} else {
				perms[sorted] = append(list, i)
			}
		}
	}
	for _, items := range perms {
		if len(items) >= 3 {
			sort.Ints(items)
			for i := 0; i < len(items)-2; i += 1 {
				for j := i + 1; j < len(items); j += 1 {
					final_item := 2*items[j] - items[i]
					if inSlice(items, final_item) {
						fmt.Printf("%d%d%d\n", items[i], items[j], final_item)
					}
				}
			}
		}
	}
}
