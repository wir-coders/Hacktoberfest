import java.util.Arrays;

class BubbleSort
{
	void bubbleSort(int array[])
	{
		int n = array.length;
		for (int i = 0; i < n-1; i++)
			for (int j = 0; j < n-i-1; j++)
				if (array[j] > array[j+1])
				{
					array[j+1] = array[j] + array[j+1] - (array[j] = array[j+1]); // Optimized Swapping
				}
	}

	public static void main(String args[])
	{
		BubbleSort bs = new BubbleSort();
		int array[] = {64, 34, 25, 12, 22, 11, 90};
		System.out.println("Before Bubble Sort:"+Arrays.toString(array));
		bs.bubbleSort(array);
		System.out.println("After Bubble Sort:"+Arrays.toString(array));
	}
}
