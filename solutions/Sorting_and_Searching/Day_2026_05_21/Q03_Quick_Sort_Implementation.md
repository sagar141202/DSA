# Quick Sort Implementation

## Problem Statement
The problem requires implementing the Quick Sort algorithm to sort an array of integers in ascending order. Given an array of integers, the task is to rearrange the elements in such a way that all elements smaller than a pivot element are on the left of it, and all elements greater are on the right. The pivot element can be any element from the array. The constraints are that the array can contain duplicate elements and the input size can range from 1 to 10^5. For example, if the input array is [5, 2, 9, 1, 7], the output should be [1, 2, 5, 7, 9].

## Approach
The Quick Sort algorithm uses a divide-and-conquer approach to sort the array. It selects a pivot element, partitions the array around it, and recursively sorts the sub-arrays. The algorithm ensures that all elements smaller than the pivot are on the left and all elements greater are on the right.

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
    int pivot = arr[high]; // pivot element
    int i = low - 1; // index of smaller element

    // Iterate through the array from low to high-1
    for (int j = low; j < high; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++; // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }

    // Swap the pivot element with the greater element
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

// Function to implement Quick Sort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);

        // Recursively sort the sub-arrays
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
Input: [5, 2, 9, 1, 7]
Output: [1, 2, 5, 7, 9]

Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]
```

## Key Takeaways
- Quick Sort is an efficient sorting algorithm with an average time complexity of O(n log n).
- The algorithm uses a divide-and-conquer approach to sort the array by selecting a pivot element and partitioning the array around it.
- The choice of pivot element can significantly affect the performance of the algorithm, and there are various techniques to select a good pivot.