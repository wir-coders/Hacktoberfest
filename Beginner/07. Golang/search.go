package main 

import ( 
	"fmt"
	"sort"
) 

func main() { 
	res1 := sort.SearchInts([]int{1, 2, 3, 
						4, 5, 6, 7, 8}, 5) 
	
	res2 := sort.SearchInts([]int{200, 300, 
				400, 500, 600, 700}, 400) 

	// Displaying the results 
	fmt.Println("Result 1: ", res1) 
	fmt.Println("Result 2: ", res2) 

} 
