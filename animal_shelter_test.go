package main

import (
	"testing"
)

func TestAnimalShelter(t *testing.T) {
	t.Run("enqueue and dequeueAny operations", func(t *testing.T) {
		shelter := NewAnimalShelter()

		// Add animals to the shelter
		shelter.Enqueue(Animal{Type: "dog", Name: "Rex"})
		shelter.Enqueue(Animal{Type: "cat", Name: "Whiskers"})
		shelter.Enqueue(Animal{Type: "dog", Name: "Buddy"})

		// Dequeue any animal (should be the first one - Rex)
		animal := shelter.DequeueAny()
		if animal.Name != "Rex" || animal.Type != "dog" {
			t.Errorf("Expected Rex (dog), got %s (%s)", animal.Name, animal.Type)
		}

		// Dequeue any animal again (should be Whiskers)
		animal = shelter.DequeueAny()
		if animal.Name != "Whiskers" || animal.Type != "cat" {
			t.Errorf("Expected Whiskers (cat), got %s (%s)", animal.Name, animal.Type)
		}
	})

	t.Run("dequeueDog operation", func(t *testing.T) {
		shelter := NewAnimalShelter()

		// Add animals to the shelter
		shelter.Enqueue(Animal{Type: "cat", Name: "Mittens"})
		shelter.Enqueue(Animal{Type: "dog", Name: "Max"})
		shelter.Enqueue(Animal{Type: "cat", Name: "Felix"})
		shelter.Enqueue(Animal{Type: "dog", Name: "Spot"})

		// Dequeue a dog (should be Max)
		dog := shelter.DequeueDog()
		if dog.Name != "Max" || dog.Type != "dog" {
			t.Errorf("Expected Max (dog), got %s (%s)", dog.Name, dog.Type)
		}

		// Dequeue another dog (should be Spot)
		dog = shelter.DequeueDog()
		if dog.Name != "Spot" || dog.Type != "dog" {
			t.Errorf("Expected Spot (dog), got %s (%s)", dog.Name, dog.Type)
		}

		// Try to dequeue a dog when there are none left
		dog = shelter.DequeueDog()
		if dog.Name != "" || dog.Type != "" {
			t.Errorf("Expected empty animal, got %s (%s)", dog.Name, dog.Type)
		}
	})

	t.Run("dequeueCat operation", func(t *testing.T) {
		shelter := NewAnimalShelter()

		// Add animals to the shelter
		shelter.Enqueue(Animal{Type: "dog", Name: "Rover"})
		shelter.Enqueue(Animal{Type: "cat", Name: "Fluffy"})
		shelter.Enqueue(Animal{Type: "dog", Name: "Fido"})
		shelter.Enqueue(Animal{Type: "cat", Name: "Snowball"})

		// Dequeue a cat (should be Fluffy)
		cat := shelter.DequeueCat()
		if cat.Name != "Fluffy" || cat.Type != "cat" {
			t.Errorf("Expected Fluffy (cat), got %s (%s)", cat.Name, cat.Type)
		}

		// Dequeue another cat (should be Snowball)
		cat = shelter.DequeueCat()
		if cat.Name != "Snowball" || cat.Type != "cat" {
			t.Errorf("Expected Snowball (cat), got %s (%s)", cat.Name, cat.Type)
		}

		// Try to dequeue a cat when there are none left
		cat = shelter.DequeueCat()
		if cat.Name != "" || cat.Type != "" {
			t.Errorf("Expected empty animal, got %s (%s)", cat.Name, cat.Type)
		}
	})

	t.Run("mixed operations", func(t *testing.T) {
		shelter := NewAnimalShelter()

		// Add animals to the shelter
		shelter.Enqueue(Animal{Type: "dog", Name: "Buddy"})
		shelter.Enqueue(Animal{Type: "cat", Name: "Whiskers"})
		shelter.Enqueue(Animal{Type: "dog", Name: "Rex"})
		shelter.Enqueue(Animal{Type: "cat", Name: "Mittens"})

		// Dequeue a dog (should be Buddy)
		dog := shelter.DequeueDog()
		if dog.Name != "Buddy" || dog.Type != "dog" {
			t.Errorf("Expected Buddy (dog), got %s (%s)", dog.Name, dog.Type)
		}

		// Dequeue any animal (should be Whiskers)
		animal := shelter.DequeueAny()
		if animal.Name != "Whiskers" || animal.Type != "cat" {
			t.Errorf("Expected Whiskers (cat), got %s (%s)", animal.Name, animal.Type)
		}

		// Dequeue a cat (should be Mittens)
		cat := shelter.DequeueCat()
		if cat.Name != "Mittens" || cat.Type != "cat" {
			t.Errorf("Expected Mittens (cat), got %s (%s)", cat.Name, cat.Type)
		}

		// Dequeue any animal (should be Rex)
		animal = shelter.DequeueAny()
		if animal.Name != "Rex" || animal.Type != "dog" {
			t.Errorf("Expected Rex (dog), got %s (%s)", animal.Name, animal.Type)
		}

		// Shelter should be empty now
		animal = shelter.DequeueAny()
		if animal.Name != "" || animal.Type != "" {
			t.Errorf("Expected empty animal, got %s (%s)", animal.Name, animal.Type)
		}
	})
}
