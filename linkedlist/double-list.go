package linkedlist

import (
	"fmt"
)

type Double struct {
	Head *DoubleNode
	Tail *DoubleNode
	Size int
}

type DoubleNode struct {
	Value    any
	Next     *DoubleNode
	Previous *DoubleNode
}

func BuildDouble(items []any) *Double {
	d := new(Double)

	for _, item := range items {
		d.InsertLast(item)
	}

	return d
}

func (d *Double) InsertLast(item any) {
	n := DoubleNode{
		Value: item,
	}

	if d.Size == 0 {
		d.Head = &n
		d.Tail = &n
		d.Size++
		return
	}

	n.Previous = d.Tail
	d.Tail.Next = &n
	d.Tail = &n
	d.Size++
}

func (d *Double) Print() {
	current := d.Head

	for current != nil {
		fmt.Printf("%s ->", current.Value)
		current = current.Next
	}
}
