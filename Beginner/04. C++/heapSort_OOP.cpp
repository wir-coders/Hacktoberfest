//  Desc.:  Program for selection-sort algorithm (OOP concepts included).
//  Author: Dishant Vyas
//  Date:   07/10/2020



#include<iostream>
using namespace std;

template <typename dt>
class heapSort {
private:
    dt arr[10000];
    dt size = 0;
    dt largest = -1;

public:
    void exchange(dt m, dt n) {
        dt temp = arr[m];
        arr[m] = arr[n];
        arr[n] = temp;
    }
    
    dt left(dt i) {
        return 2*i;
    }

    dt right(dt i) {
        return 2*i+1;
    }

    dt parent(dt i) {
        return i/2;
    }

    void fillArray(dt i, dt value) {
        arr[i] = value;
        size++;
    }
    
    void heapify(dt i) {
            if(right(i) <= size) {
                if(arr[left(i)] > arr[right(i)])
                    largest = left(i);
                else
                    largest = right(i);
            }
            else
                if(left(i) <=size)
                    largest = left(i);
            if(arr[i] < arr[largest]) {
                exchange(i, largest);
                heapify(largest);
            }
    }

    void buildHeap() {
        dt n = size;
        for(dt i=parent(n) ; i>=0 ; i--)
            heapify(i);
    }

    void heap_sort() {
        buildHeap();
        for(dt i=size ; i>0 ; i--) {
            exchange(0,i);
            size--;
            heapify(0);
        }
    }

    void dispArray(dt n) {
        for(dt i=0 ; i<=n ; i++)
        cout << arr[i] << " ";
    }
};

int main() {
    heapSort<int> obj;
    int n;
    double temp;
    cin >> n;
    for(int i=0 ; i<n ; i++) {
        cin >> temp;
        obj.fillArray(i, temp);
    }
    obj.heap_sort();
    obj.dispArray(n);
    return 0;
}