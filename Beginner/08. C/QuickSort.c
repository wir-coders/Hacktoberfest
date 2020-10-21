#include<stdio.h>


void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

/* This function takes last element as pivot, places
   the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
   to left of pivot and all greater elements to right
   of pivot */
int partition (int arr[], int start, int end)
{
    int pivot = arr[end];    // pivot
    int i = (start - 1);  // Index of smaller element

    for (int j =start; j <= end-1; j++)
    {
        // If current element is smaller than the pivot
        if (arr[j] < pivot)
        {
            i++;    // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[end]);
    return (i + 1);
}

/* The main function that implements QuickSort
 arr[] --> Array to be sorted,
  start  --> Starting index,
  end --> Ending index */
void quickSort(int arr[], int start, int end)
{
    if (start < end)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        int pi = partition(arr,start,end);

        // Separately sort elements before
        // partition and after partition
        quickSort(arr,start,pi-1);
        quickSort(arr,pi+1,end);
    }
}

void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int n;
    scanf("%d", &n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    quickSort(arr, 0, n-1);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}
