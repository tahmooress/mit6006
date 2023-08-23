package cyclic

import (
	"code6006/linkedlist"
)

// FindCycle return node which cycle start on and the nubmber
// of nodes in cycle.
func FindCycle(list linkedlist.Single) (*linkedlist.Node, int) {
	// i, j are slow and fast pointers respectivly.
	var i, j *linkedlist.Node = list.Head, list.Head

	for j.Next != i {
		j = j.Next.Next
		i = i.Next
	}

	head := i
	count := 1

	for head.Next != i {
		head = head.Next
		count++
	}

	return i, count
}
