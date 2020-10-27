#include <stdio.h>

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void print_array(int array[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d\n", array[i]);
    }
}
int main(void) {
    int array[5] = {99, 34, 12, 73, 84};
    int counter = 5; // Size of array
    
    for (int i = 0; i < counter; i++) {
        for (int j = i + 1; j < counter; j++) {
            if (array[j] < array[i]) {
                swap(&array[j], &array[i]);
            }
        }
    }

    print_array(array, counter);
}