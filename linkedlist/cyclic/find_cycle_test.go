package cyclic

import (
	"code6006/linkedlist"
	"testing"
)

func TestFindCycle(t *testing.T) {
	items := []any{"tahmoores", "sanaz", "kusha", "navid", "farzad"}
	list := linkedlist.Build(items)

	startCycle := list.Head.Next.Next
	list.Tail.Next = startCycle

	_, count := FindCycle(*list)

	if count != 3 {
		t.Errorf("expected count: %v but got: %v", 3, count)
	}
}
