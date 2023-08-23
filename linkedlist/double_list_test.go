package linkedlist

import (
	"testing"
)

func TestBuildDouble(t *testing.T) {
	items := []any{"tahmoores", "sanaz", "kusha", "navid", "farzad"}
	d := BuildDouble(items)
	d.Print()
}
