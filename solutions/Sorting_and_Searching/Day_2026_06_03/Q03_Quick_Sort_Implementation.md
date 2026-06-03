# Quick Sort Implementation

## Problem Statement
Given an array of integers, implement the Quick Sort algorithm to sort the array in ascending order. The Quick Sort algorithm is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. The algorithm should have an average time complexity of O(n log n) and a space complexity of O(log n). For example, given the array [5, 2, 9, 1, 7], the sorted array should be [1, 2, 5, 7, 9].

## Approach
The Quick Sort algorithm works by selecting a pivot element, partitioning the array around the pivot, and recursively sorting the sub-arrays. The algorithm uses a divide-and-conquer approach to achieve efficient sorting. The pivot element is chosen and the array is partitioned, with elements less than the pivot on the left and elements greater than the pivot on the right. The sub-arrays are then recursively sorted.

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
    int pivot = arr[high]; // Choose the last element as the pivot
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
        int pivotIndex = partition(arr, low, high);
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

// Function to print the sorted array
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
- The Quick Sort algorithm has an average time complexity of O(n log n) and a space complexity of O(log n).
- The choice of pivot element can affect the performance of the Quick Sort algorithm.
- The Quick Sort algorithm is a divide-and-conquer algorithm that works by selecting a pivot element, partitioning the array, and recursively sorting the sub-arrays.