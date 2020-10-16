class BinarySearch {

	int binarySearch(int arr[], int start, int end, int x){
		if(end >= start){
			int mid = start + (end - start)/2;
			if(arr[mid] == x)
				return mid;

			if (arr[mid] > x) 
                return binarySearch(arr, start, mid - 1, x); 
  
            
            return binarySearch(arr, mid + 1, end, x); 
		}
		return -1;
	}
	public static void main(String[] args) {
		BinarySearch bs = new BinarySearch(); 
        int arr[] = { 1, 3, 5, 10, 35 }; 
        int n = arr.length; 
        int x = 10; 
        int result = bs.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element is not present in the given array"); 
        else
            System.out.println(result); // prints index of the element;
	}
}
