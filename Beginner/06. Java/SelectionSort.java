import java.util.*;

public class SelectionSort {
  public static void main(String[] args)
  {
    Scanner scn = new Scanner(System.in);
    Random r = new Random();

    //Input size of Array
    int n = scn.nextInt();
    int[] arr = new int[n];

    //Random values for Array
    for (int i = 0; i < n; i++)
      arr[i] = r.nextInt(n);

    //Selection Sort Algo
    for (int counter = 0; counter <= n - 2; counter++)
    {
      int min = counter;
      for (int i = counter + 1; i < n; i++)
      {
        if (arr[min] > arr[i])
        {
          min = i;
        }
      }
      int temp = arr[counter];
      arr[counter] = arr[min];
      arr[min] = temp;
    }

    //Print Sorted Array
    for(int i : arr)
      System.out.print(i + "\t");
  }
}
