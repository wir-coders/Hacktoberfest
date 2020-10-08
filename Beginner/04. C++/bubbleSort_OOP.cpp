//  Desc.:  Program for selection-sort algorithm (OOP concepts included).
//  Author: Dishant Vyas
//  Date:   07/10/2020



#include<iostream>
using namespace std;

template <typename dt>
class bubbleSort {
private:
    dt arr[10000];
    dt swapCount = 0;
    dt size = 0;

public:
    void fillArray(dt i, dt value) {
        arr[i] = value;
        size++;
    }

    void bubble_sort() {
        for(int i=0 ; i<size-1 ; i++)
            for(int j=size-1 ; j>=i+1 ; j--)
                if (arr[j] < arr[j-1]) {
                    int temp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                    swapCount++;
                }
    }

    void dispArray() {
        cout << "Array is sorted in " << swapCount << " swaps." << endl;
        cout << "Sorted array: ";
        for(int i=0 ; i<size ; i++)
            cout << arr[i] << " ";
    }
};

int main() {
    bubbleSort<int> obj;
    int n, temp;
    cin >> n;
    for(int i=0 ; i<n ; i++) {
        cin >> temp;
        obj.fillArray(i, temp);
    }
    obj.bubble_sort();
    obj.dispArray();
    return 0;
}