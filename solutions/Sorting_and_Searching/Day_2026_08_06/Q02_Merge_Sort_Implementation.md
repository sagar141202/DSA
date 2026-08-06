# Merge Sort Implementation

## Problem Statement
Given an array of integers, implement the merge sort algorithm to sort the array in ascending order. The merge sort algorithm is a divide-and-conquer algorithm that splits the input array into two halves, recursively sorts each half, and then merges the two sorted halves. The algorithm should be able to handle arrays of any size and should have a time complexity of O(n log n). For example, if the input array is [5, 2, 8, 1, 9], the output should be [1, 2, 5, 8, 9].

## Approach
The merge sort algorithm works by recursively splitting the input array into two halves until each half has only one element, and then merging the halves back together in sorted order. This process continues until the entire array is sorted. The algorithm uses a temporary array to store the merged result.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to merge two sorted subarrays
void merge(int arr[], int left, int mid, int right) {
    // Create a temporary array to store the merged result
    int temp[right - left + 1];
    int i = left, j = mid + 1, k = 0;

    // Merge the two sorted subarrays
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }

    // Copy any remaining elements from the left subarray
    while (i <= mid) {
        temp[k++] = arr[i++];
    }

    // Copy any remaining elements from the right subarray
    while (j <= right) {
        temp[k++] = arr[j++];
    }

    // Copy the merged result back into the original array
    for (i = left, k = 0; i <= right; i++, k++) {
        arr[i] = temp[k];
    }
}

// Function to implement the merge sort algorithm
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Recursively sort the left and right subarrays
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Merge the two sorted subarrays
        merge(arr, left, mid, right);
    }
}

int main() {
    int arr[] = {5, 2, 8, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Print the original array
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Sort the array using the merge sort algorithm
    mergeSort(arr, 0, n - 1);

    // Print the sorted array
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

## Test Cases
```
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]

Input: [10, 7, 4, 1, 9]
Output: [1, 4, 7, 9, 10]

Input: [3, 6, 1, 8, 2, 4]
Output: [1, 2, 3, 4, 6, 8]
```

## Key Takeaways
- The merge sort algorithm is a divide-and-conquer algorithm that splits the input array into two halves, recursively sorts each half, and then merges the two sorted halves.
- The algorithm has a time complexity of O(n log n) and a space complexity of O(n).
- The merge sort algorithm is a stable sorting algorithm, meaning that it preserves the order of equal elements.