# Quick Sort Implementation

## Problem Statement
The problem requires implementing the Quick Sort algorithm to sort an array of integers in ascending order. The input array can contain duplicate elements and negative numbers. The output should be the sorted array. For example, given the input array `[5, 2, 9, 1, 7, 3]`, the output should be `[1, 2, 3, 5, 7, 9]`. The constraints are that the input array can have a maximum size of `10^5` elements and the elements can be in the range of `[-10^9, 10^9]`.

## Approach
The Quick Sort algorithm works by selecting a pivot element, partitioning the array around the pivot, and recursively sorting the sub-arrays. The algorithm uses a divide-and-conquer approach to sort the array efficiently. The pivot element is chosen, and the array is partitioned such that all elements less than the pivot are on the left, and all elements greater than the pivot are on the right.

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
Input: [-5, 0, 5, -10, 10]
Output: [-10, -5, 0, 5, 10]
```

## Key Takeaways
- Quick Sort is a divide-and-conquer algorithm that works by selecting a pivot element and partitioning the array around it.
- The choice of pivot element can affect the performance of the algorithm, and there are various techniques to choose a good pivot.
- Quick Sort has an average time complexity of O(n log n), but it can be O(n^2) in the worst case if the pivot is chosen poorly.