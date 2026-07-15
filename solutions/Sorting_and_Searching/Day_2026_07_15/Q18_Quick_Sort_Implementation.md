# Quick Sort Implementation

## Problem Statement
The problem requires implementing the Quick Sort algorithm to sort an array of integers in ascending order. The array can contain duplicate elements and can be of any size. The goal is to rearrange the elements in the array such that all elements are in ascending order. For example, given the array `[5, 2, 9, 1, 7, 3]`, the output should be `[1, 2, 3, 5, 7, 9]`. The algorithm should be efficient and scalable to handle large inputs.

## Approach
The Quick Sort algorithm uses a divide-and-conquer approach, selecting a pivot element and partitioning the array around it. The algorithm recursively sorts the sub-arrays on either side of the pivot element. The intuition behind Quick Sort is to minimize the number of comparisons required to sort the array by choosing a good pivot element.

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

// Function to partition the array and return the pivot index
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
    int arr[] = {5, 2, 9, 1, 7, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
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

Input: [4, 2, 9, 6, 5, 1]
Output: [1, 2, 4, 5, 6, 9]
```

## Key Takeaways
- Quick Sort is an efficient sorting algorithm with an average time complexity of O(n log n).
- The choice of pivot element can significantly impact the performance of the Quick Sort algorithm.
- Quick Sort is a divide-and-conquer algorithm that recursively sorts the sub-arrays on either side of the pivot element.