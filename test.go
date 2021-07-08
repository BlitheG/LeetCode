package main

import (
	"fmt"
)

func main() {
	l1 := []int{3, 4, 1, 2}
	l2 := []int{3, 6, 7, 8}
	l3 := make([]int, len(l1), cap(l1))
	copy(l3, l1)
	fmt.Println(l3)
	for _, v := range l2 {
		l3 = append(l3, int(v))
	}
	fmt.Println(l3)
}