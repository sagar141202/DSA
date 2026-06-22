# Quick Sort Implementation

## Problem Statement
The problem requires implementing the Quick Sort algorithm to sort an array of integers in ascending order. The input array can contain duplicate elements and can be of any size. The goal is to rearrange the elements in the array such that all elements are in ascending order. For example, given the array `[5, 2, 9, 1, 7]`, the output should be `[1, 2, 5, 7, 9]`. The constraints are that the input array can contain up to 10^5 elements, and each element can be in the range of 1 to 10^9.

## Approach
The Quick Sort algorithm works by selecting a pivot element, partitioning the array around the pivot, and recursively sorting the sub-arrays. The intuition behind this algorithm is to divide the array into smaller sub-arrays and solve them individually. The partitioning step is crucial, as it determines the efficiency of the algorithm. The algorithm has an average time complexity of O(n log n), making it suitable for large datasets.

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
- The Quick Sort algorithm has an average time complexity of O(n log n), making it suitable for large datasets.
- The choice of pivot element can significantly affect the performance of the algorithm.
- The partitioning step is crucial in the Quick Sort algorithm, as it determines the efficiency of the algorithm.