# Merge Sort Implementation

## Problem Statement
Given an array of integers, implement the merge sort algorithm to sort the array in ascending order. The merge sort algorithm is a divide-and-conquer algorithm that works by splitting the input array into two halves, recursively sorting each half, and then merging the two sorted halves. The algorithm should be able to handle arrays of any size and should have a time complexity of O(n log n). For example, given the array [5, 2, 8, 3, 1, 6, 4], the output should be [1, 2, 3, 4, 5, 6, 8].

## Approach
The merge sort algorithm works by recursively dividing the input array into two halves until each half has only one element, and then merging the halves back together in sorted order. This process is repeated until the entire array is sorted. The algorithm uses a temporary array to store the merged halves.

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

    // Copy data to temp arrays L[] and R[]
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

// Function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
    int arr[] = {5, 2, 8, 3, 1, 6, 4};
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
Input: [5, 2, 8, 3, 1, 6, 4]
Output: [1, 2, 3, 4, 5, 6, 8]
Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]
```

## Key Takeaways
- Merge sort is a divide-and-conquer algorithm that works by splitting the input array into two halves, recursively sorting each half, and then merging the two sorted halves.
- The algorithm has a time complexity of O(n log n) and a space complexity of O(n).
- Merge sort is a stable sorting algorithm, meaning that the order of equal elements is preserved.