# Merge Sort Implementation

## Problem Statement
Given an array of integers, sort the array in ascending order using the Merge Sort algorithm. The array can contain duplicate elements and the size of the array is not fixed. For example, if the input array is `[5, 2, 8, 1, 9]`, the output should be `[1, 2, 5, 8, 9]`. The algorithm should be efficient and scalable for large inputs.

## Approach
The Merge Sort algorithm works by dividing the input array into two halves, recursively sorting each half, and then merging the sorted halves. This process continues until the base case is reached, where the array has only one element. The merge step combines two sorted arrays into a single sorted array.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to merge two sorted subarrays
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int L[n1], R[n2];

    // Copy data to temp arrays
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    // Merge the temp arrays back into arr[left..right]
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

// Function to perform Merge Sort
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
- Merge Sort is a divide-and-conquer algorithm that splits the input array into two halves, recursively sorts each half, and then merges the sorted halves.
- The time complexity of Merge Sort is O(n log n), making it suitable for large inputs.
- The space complexity of Merge Sort is O(n), which is the additional space required for the temporary arrays used during the merge step.