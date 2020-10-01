import java.util.*;

public class BubbleSort {
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

    //Bubble Sort Algo
    for (int i = 0; i <= n - 2; i++)
    {
      for (int j = 0; j <= n - 2 - i; j++)
      {
        if (arr[j] > arr[j + 1])
        {
          int temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }

    //Print sorted array
    for(int i : arr)
      System.out.print(i + "\t");
  }
}
