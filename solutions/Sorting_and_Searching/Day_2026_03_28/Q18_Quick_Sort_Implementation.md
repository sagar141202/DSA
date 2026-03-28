# Quick Sort Implementation

## Problem Statement
Given an array of integers, implement the Quick Sort algorithm to sort the array in ascending order. The array can contain duplicate elements and the size of the array can range from 1 to 10^5. For example, if the input array is [5, 2, 9, 1, 7], the output should be [1, 2, 5, 7, 9].

## Approach
The Quick Sort algorithm works by selecting a pivot element, partitioning the array around the pivot, and recursively sorting the subarrays. The pivot element is chosen and the array is partitioned such that all elements less than the pivot are on the left and all elements greater are on the right.

## Complexity
- Time: O(n log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

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

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {5, 2, 9, 1, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    printArray(arr, n);
    return 0;
}
```

## Test Cases
```
Input: [5, 2, 9, 1, 7]
Output: [1, 2, 5, 7, 9]
Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]
```

## Key Takeaways
- The Quick Sort algorithm has an average time complexity of O(n log n) but can be O(n^2) in the worst case if the pivot is chosen poorly.
- The choice of pivot is crucial in determining the performance of the Quick Sort algorithm.
- Quick Sort is an in-place sorting algorithm, meaning it does not require any additional storage space.