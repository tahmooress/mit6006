package selection

func Sort(arr []int) {
	for i := len(arr); i > 1; i-- {
		m := max(arr[:i])
		arr[m], arr[i-1] = arr[i-1], arr[m]
	}
}

func max(arr []int) int {
	index, max := 0, 0

	for i := range arr {
		if arr[i] > max {
			max = arr[i]
			index = i
		}
	}

	return index
}
