# Merge Sort Implementation

## Problem Statement
Merge sort is a divide-and-conquer algorithm that splits a given list into two halves, recursively sorts them, and then merges them. The problem requires implementing the merge sort algorithm to sort a list of integers in ascending order. The input list can contain duplicate elements and negative numbers. For example, given the list `[5, 2, 8, 1, 9]`, the output should be `[1, 2, 5, 8, 9]`.

## Approach
The merge sort algorithm works by recursively dividing the list into two halves until each sublist contains only one element. Then, it merges the sublists in a way that maintains the sorted order. This process continues until the entire list is sorted. The algorithm uses a temporary array to store the merged sublists.

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

    // Merge the temporary arrays back into arr[]
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

    // Copy the remaining elements of L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if there are any
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
    int arr[] = {5, 2, 8, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, n);

    mergeSort(arr, 0, n - 1);

    cout << "Sorted array: ";
    printArray(arr, n);

    return 0;
}
```

## Test Cases
```
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]

Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]

Input: [4, 2, 9, 6, 23, 12, 34, 0, 1]
Output: [0, 1, 2, 4, 6, 9, 12, 23, 34]
```

## Key Takeaways
- Merge sort is a divide-and-conquer algorithm that splits the list into two halves, recursively sorts them, and then merges them.
- The time complexity of merge sort is O(n log n), making it efficient for large datasets.
- The space complexity of merge sort is O(n), as it requires a temporary array to store the merged sublists.