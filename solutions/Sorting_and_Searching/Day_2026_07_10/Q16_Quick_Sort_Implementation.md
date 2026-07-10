# Quick Sort Implementation

## Problem Statement
The problem requires implementing the Quick Sort algorithm to sort an array of integers in ascending order. The input array can contain duplicate elements and can be of any size. The algorithm should be efficient and scalable. For example, given the input array `[5, 2, 9, 1, 7, 3]`, the output should be `[1, 2, 3, 5, 7, 9]`. The constraints are that the input array can contain at most 10^5 elements and each element can be in the range of -10^9 to 10^9.

## Approach
The Quick Sort algorithm uses the divide-and-conquer technique to sort the array. It selects a pivot element, partitions the array around the pivot, and recursively sorts the sub-arrays. The algorithm has an average time complexity of O(n log n) and is suitable for large datasets. The key steps are selecting a pivot, partitioning the array, and recursively sorting the sub-arrays.

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
    int pivot = arr[high]; // Select the last element as the pivot
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

// Driver code
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
```

## Key Takeaways
- The Quick Sort algorithm has an average time complexity of O(n log n) and is suitable for large datasets.
- The choice of pivot element can affect the performance of the algorithm, and a good pivot can reduce the number of recursive calls.
- The Quick Sort algorithm is not stable, meaning that equal elements may not keep their original order after sorting.