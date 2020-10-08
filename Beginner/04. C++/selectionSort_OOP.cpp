//  Desc.:  Program for selection-sort algorithm (OOP concepts included).
//  Author: Dishant Vyas
//  Date:   07/10/2020



#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


template <typename dt>                                              // Template applied.
class selectionSort {
private:                                                            // Variables assigned.
    dt arr[10000];
    dt size = 0;


public:
    void fillArray(dt i, dt value) {                                // Function to fill array.
        arr[i] = value;
        size++;
    }

    void selection_sort() {                                         // Sorting function using Selection-Sort Algorithm.
        int min_index;
        for(int i=0 ; i<size-1 ; i++) {
            min_index=i;
            for(int j=i+1 ; j<size ; j++)
                if (arr[j] < arr[min_index])
                    min_index = j;

            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }
    }

    void dispArray() {                                              // Function to print the required result.
        for(int i=0 ; i<size ; i++)
            cout << arr[i] << " ";
    }
};



int main() {
    selectionSort<int> obj;
    int n, temp;
    cin >> n;
    for(int i=0 ; i<n ; i++) {
        cin >> temp;
        obj.fillArray(i, temp);
    }
    obj.selection_sort();
    obj.dispArray();
    return 0;
}