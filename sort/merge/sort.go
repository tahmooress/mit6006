package merge

func Sort(arr []int) {
	sort(arr, 0, len(arr))
}

func sort(arr []int, low, high int) {
	if high-low > 1 {
		mid := (low + high) >> 1
		sort(arr, low, mid)
		sort(arr, mid, high)
		merge(arr, low, mid, high)
	}
}

func merge(arr []int, low, mid, high int) {
	left := make([]int, mid-low)
	copy(left, arr[low:mid])
	right := make([]int, high-mid)
	copy(right, (arr[mid:high]))
	i, j := 0, 0
	for l := low; l < high; l++ {
		if i < len(left) && j < len(right) && left[i] < right[j] {
			arr[l] = left[i]
			i++
		} else if i < len(left) && j < len(right) && left[i] >= right[j] {
			arr[l] = right[j]
			j++
		} else if j < len(right) {
			arr[l] = right[j]
			j++
		} else if i < len(left) {
			arr[l] = left[i]
			i++
		}
	}
}
