// >>> print map(lambda x: x * 2, range(1,11))
// [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
package main

func time2(n int) int {
	return n * 2
}

func main() {
	var s [10]int

	for i := 0; i < len(s); i++ {
		s[i] = i + 1
	}

	var t2s [10]int

	for i, num := range s {
		t2s[i] = time2(num)
	}

	for _, n := range t2s {
		print(n)
		print(" ")
	}
}
