# Merge Sort Implementation

## Problem Statement
Given an array of integers, implement the Merge Sort algorithm to sort the array in ascending order. The array can contain duplicate elements and can be of any size. The goal is to divide the array into smaller sub-arrays, sort them individually, and then merge them back together in a sorted manner. For example, if the input array is `[5, 2, 8, 1, 9]`, the output should be `[1, 2, 5, 8, 9]`.

## Approach
The Merge Sort algorithm uses a divide-and-conquer approach, splitting the array into two halves, sorting them recursively, and then merging the sorted halves. This process continues until the entire array is sorted. The algorithm relies on the concept of merging two sorted arrays into a single sorted array.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to merge two sorted sub-arrays
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Create temporary arrays
    int leftArr[n1], rightArr[n2];

    // Copy data to temporary arrays
    for (int i = 0; i < n1; i++)
        leftArr[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        rightArr[j] = arr[mid + 1 + j];

    // Merge the temporary arrays
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (leftArr[i] <= rightArr[j])
            arr[k] = leftArr[i++];
        else
            arr[k] = rightArr[j++];
        k++;
    }

    // Copy remaining elements, if any
    while (i < n1)
        arr[k++] = leftArr[i++];
    while (j < n2)
        arr[k++] = rightArr[j++];
}

// Function to implement Merge Sort
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

// Example usage
int main() {
    int arr[] = {5, 2, 8, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, 0, n - 1);

    // Print the sorted array
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
```

## Test Cases
```
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]

Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]

Input: [4, 2, 9, 6, 5, 1]
Output: [1, 2, 4, 5, 6, 9]
```

## Key Takeaways
- Merge Sort has a time complexity of O(n log n), making it suitable for large datasets.
- The algorithm uses a divide-and-conquer approach, dividing the array into smaller sub-arrays and sorting them recursively.
- Merge Sort is a stable sorting algorithm, preserving the order of equal elements.