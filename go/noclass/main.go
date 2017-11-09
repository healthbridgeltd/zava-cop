package main

import (
	"fmt"
)

// Question: Ambitious: Which one is displayed?
type Animal struct {
	Name string
}

func (a Animal) display() {
	fmt.Println("Hey, I'm " + a.Name)
}

type Duck struct {
	Name string
}

type RubberDuck struct {
	Duck
	// Animal Question: Which one is displayed?
	Material string
}

type DecoyDuck struct {
	Duck
}

func (d DecoyDuck) display() {
	fmt.Println("Quack! I'm DecoyDuck!")
}

// Question: How to overwrite display()?
func (d RubberDuck) display() {
	fmt.Println("Quack! I'm RubberDuck!")
	// Question: How to call Duck's display?
	d.Duck.display()
}

func (d Duck) display() {
	fmt.Println("Hey, I'm " + d.Name)
}

func main() {
	d := &RubberDuck{
		// Question: How to write Duck inside RubberDuck?
		Material: "Excelent Rubber",
		Duck: Duck{
			Name: "Kohei",
		},
	}

	d.display()
}
