# Quick Sort Implementation

## Problem Statement
Given an array of integers, implement the quick sort algorithm to sort the array in ascending order. The quick sort algorithm is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. The algorithm should be able to handle arrays of size up to 10^5 and should have an average time complexity of O(n log n). Example: input = [5, 2, 9, 1, 7], output = [1, 2, 5, 7, 9].

## Approach
The quick sort algorithm works by selecting a pivot element, partitioning the array around the pivot, and recursively sorting the sub-arrays. The pivot can be chosen in various ways, such as the first element, the last element, or a random element. The partitioning step is the key to the algorithm, as it ensures that the pivot is in its final sorted position.

## Complexity
- Time: O(n log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// function to swap two elements
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// function to partition the array and return the pivot index
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // choose the last element as the pivot
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

// function to implement quick sort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

// function to print the array
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
- The quick sort algorithm has an average time complexity of O(n log n), making it suitable for large datasets.
- The choice of pivot element can affect the performance of the algorithm, and a good choice can lead to better performance.
- The partitioning step is the key to the algorithm, as it ensures that the pivot is in its final sorted position.