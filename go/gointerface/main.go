package main

import (
	"fmt"
)

type Quackable interface {
	Quack() string
}

type Flyable interface {
	Fly() string
}

type Duck struct {
	Name string
}

func (d Duck) display() {
	fmt.Println("Hey, I'm " + d.Name)
}

func (d Duck) Quack() string {
	fmt.Println("Quack!")
	return "Quack"
}

func doQuack(q Quackable) {
	q.Quack()
}

func main() {
	d := &Duck{
		Name: "Kohei",
	}

	doQuack(d)
}
