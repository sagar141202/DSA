# Merge Sort Implementation

## Problem Statement
Merge sort is a divide-and-conquer algorithm that splits a given list of elements into two halves, recursively sorts each half, and then merges the two sorted halves. The problem requires implementing the merge sort algorithm to sort a list of integers in ascending order. The input list can contain duplicate elements and can be of any size. For example, given the list [64, 34, 25, 12, 22, 11, 90], the output should be [11, 12, 22, 25, 34, 64, 90].

## Approach
The merge sort algorithm works by recursively dividing the input list into two halves until each sublist contains only one element. Then, it merges the sublists in a way that maintains the sorted order. This process continues until the entire list is sorted. The algorithm uses a temporary array to store the merged sublists.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to merge two sublists
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Create temporary arrays
    int L[n1], R[n2];

    // Copy data to temporary arrays
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Merge the temporary arrays
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy remaining elements of L[], if any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy remaining elements of R[], if any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Function to implement merge sort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Merge the sorted halves
        merge(arr, left, mid, right);
    }
}

// Function to print the array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    cout << "Sorted array: ";
    printArray(arr, arr_size);

    return 0;
}
```

## Test Cases
```
Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]
Input: [10, 7, 4, 1, 9, 3, 6, 8, 2, 5]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Key Takeaways
- Merge sort is a divide-and-conquer algorithm that splits the input list into two halves, recursively sorts each half, and then merges the two sorted halves.
- The time complexity of merge sort is O(n log n), making it suitable for large datasets.
- The space complexity of merge sort is O(n), as it requires a temporary array to store the merged sublists.