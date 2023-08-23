package selection

import "testing"

type testCase struct {
	arr      []int
	expected []int
}

var testCases = []testCase{
	{
		arr:      []int{1, 2, 7, 4, 9, 1, 25, 3},
		expected: []int{1, 1, 2, 3, 4, 7, 9, 25},
	},
	{
		arr:      []int{10, 9, 8, 7, 6, 5, 4, 3, 2, 1},
		expected: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
	}, {
		arr:      []int{10, 2, 4, 3, 7, 8, 14, 5},
		expected: []int{2, 3, 4, 5, 7, 8, 10, 14},
	},
}

func TestSort(t *testing.T) {
	for _, c := range testCases {
		Sort(c.arr)
		for i := range c.arr {
			if c.arr[i] != c.expected[i] {
				t.Errorf("expected: %v got :%v", c.expected, c.arr)
			}
		}
	}
}
