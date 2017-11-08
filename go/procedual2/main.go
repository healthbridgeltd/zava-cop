// >>> print sum(range(1,1001))
// 500500
package main

func main() {
	var a [1001]int

	for i := 0; i < len(a); i++ {
		a[i] = i
	}

	total := 0
	for _, num := range a {
		total += num
	}

	println(total)
}
