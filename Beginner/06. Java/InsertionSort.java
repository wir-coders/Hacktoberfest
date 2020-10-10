import java.util.*;

public class InsertionSort {
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

    //Insertion Sort Algo
    for (int counter = 1; counter < n; counter++)
    {
      int temp = arr[counter];
      int i = counter - 1;
      while (i >= 0 && temp < arr[i])
      {
        arr[i + 1] = arr[i];
        i--;
      }
      arr[++i] = temp;
    }

    //Print Sorted Array
    for(int i : arr)
      System.out.print(i + "\t");
  }
}
