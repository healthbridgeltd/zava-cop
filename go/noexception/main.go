package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter text: ")
	text, err := reader.ReadString('\n')

	if err != nil {
		fmt.Println("Input error:" + err.Error())
		return
	}

	text = strings.TrimSpace(text)
	num, err := strconv.Atoi(text)

	if err != nil {
		fmt.Println("Can't convert to string: " + err.Error())
		return
	}

	fmt.Println(num)
}
