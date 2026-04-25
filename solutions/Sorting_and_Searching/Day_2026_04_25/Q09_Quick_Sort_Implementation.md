# Quick Sort Implementation

## Problem Statement
The problem requires implementing the Quick Sort algorithm to sort an array of integers in ascending order. The input array can contain duplicate elements and can be of any size. The Quick Sort algorithm should have an average time complexity of O(n log n) and should be able to handle arrays with a large number of elements. For example, given the input array `[5, 2, 9, 1, 7, 3]`, the output should be `[1, 2, 3, 5, 7, 9]`.

## Approach
The Quick Sort algorithm uses a divide-and-conquer approach to sort the array. It selects a pivot element, partitions the array around the pivot, and recursively sorts the sub-arrays. The algorithm uses a recursive function to sort the array.

## Complexity
- Time: O(n log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to swap two elements
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to partition the array
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

// Function to implement Quick Sort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);

        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
}

// Function to print the array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {5, 2, 9, 1, 7, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, n);

    quickSort(arr, 0, n - 1);

    cout << "Sorted array: ";
    printArray(arr, n);

    return 0;
}
```

## Test Cases
```
Input: [5, 2, 9, 1, 7, 3]
Output: [1, 2, 3, 5, 7, 9]
Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]
```

## Key Takeaways
- The Quick Sort algorithm has an average time complexity of O(n log n) but can be O(n^2) in the worst case if the pivot is chosen poorly.
- The algorithm is not stable, meaning that equal elements may not keep their original order.
- The Quick Sort algorithm is suitable for large datasets and is widely used in many applications due to its efficiency and simplicity.