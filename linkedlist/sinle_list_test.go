package linkedlist

import (
	"testing"
)

func TestBuild(t *testing.T) {
	items := []any{"tahmoores", "sanaz", "kusha", "navid", "farzad"}
	d := Build(items)
	d.Print()
}
