package main

type AnimalType string

const (
	Dog AnimalType = "dog"
	Cat AnimalType = "cat"
)

type Animal struct {
	Type AnimalType
	Name string
}

type ListNodeAnimal struct {
	Val  Animal
	Next *ListNodeAnimal
}

func NewAnimalShelter() *AnimalShelter {
	return &AnimalShelter{}
}

type AnimalShelter struct {
	cats *ListNodeAnimal
	dogs *ListNodeAnimal
	all  *ListNodeAnimal
}

func (a *AnimalShelter) Enqueue(animal Animal) {
	if a.all == nil {
		a.all = &ListNodeAnimal{
			Val:  animal,
			Next: nil,
		}
		if animal.Type == Cat {
			a.cats = &ListNodeAnimal{
				Val:  animal,
				Next: nil,
			}
		}

		if animal.Type == Dog {
			a.dogs = &ListNodeAnimal{
				Val:  animal,
				Next: nil,
			}
		}

		return
	}

	head := a.all

	for a.all.Next != nil {
		a.all = a.all.Next
	}

	a.all.Next = &ListNodeAnimal{
		Val:  animal,
		Next: nil,
	}

	a.all = head

	if animal.Type == Dog {
		head = a.dogs

		if head == nil {
			a.dogs = &ListNodeAnimal{
				Val:  animal,
				Next: nil,
			}

			return
		}
		for a.dogs.Next != nil {
			a.dogs = a.dogs.Next
		}

		a.dogs.Next = &ListNodeAnimal{
			Val:  animal,
			Next: nil,
		}

		if head != nil {
			a.dogs = head
		}
	}
	if animal.Type == Cat {
		head = a.cats
		if head == nil {
			a.cats = &ListNodeAnimal{
				Val:  animal,
				Next: nil,
			}

			return
		}
		for a.cats.Next != nil {
			a.cats = a.cats.Next
		}

		a.cats.Next = &ListNodeAnimal{
			Val:  animal,
			Next: nil,
		}

		if head != nil {
			a.cats = head
		}

	}
}

// 1-7-8-2 //     cats: 1-2   all: 1-7-8-2  	dog: 7-8

func (a *AnimalShelter) DequeueAny() Animal {
	if a.all == nil {
		return Animal{}
	}

	animal := a.all.Val
	a.all = a.all.Next

	if animal.Type == Cat {
		a.cats = a.cats.Next
	}

	if animal.Type == Dog {
		a.dogs = a.dogs.Next
	}

	return animal
}

func (a *AnimalShelter) DequeueDog() Animal {
	if a.dogs == nil {
		return Animal{}
	}
	animal := a.dogs.Val
	a.dogs = a.dogs.Next

	if a.all.Val == animal {
		a.all = a.all.Next
		return animal
	}

	head := a.all
	for a.all.Next != nil {
		if a.all.Next.Val == animal {
			a.all.Next = a.all.Next.Next
			break
		}
		a.all = a.all.Next
	}
	a.all = head

	return animal
}

func (a *AnimalShelter) DequeueCat() Animal {
	if a.cats == nil {
		return Animal{}
	}
	animal := a.cats.Val
	a.cats = a.cats.Next

	if a.all.Val == animal {
		a.all = a.all.Next
		return animal
	}

	head := a.all
	for a.all.Next != nil {
		if a.all.Next.Val == animal {
			a.all.Next = a.all.Next.Next
			break
		}
		a.all = a.all.Next
	}
	a.all = head

	return animal
}
