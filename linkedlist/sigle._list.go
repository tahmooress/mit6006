package linkedlist

import "fmt"

type Single struct {
	Head *Node
	Tail *Node
	Size int
}

type Node struct {
	Value any
	Next  *Node
}

func Build(items []any) *Single {
	s := new(Single)

	for _, item := range items {
		s.InsertLast(item)
	}
	return s
}

func (s *Single) InsertLast(item any) {
	n := Node{
		Value: item,
	}

	if s.Size == 0 {
		s.Head = &n
		s.Tail = &n
		s.Size++
	}

	s.Tail.Next = &n
	s.Tail = &n
	s.Size++
}

func (s *Single) Print() {
	current := s.Head

	for current != nil {
		fmt.Printf("%s ->", current.Value)
		current = current.Next
	}
}
