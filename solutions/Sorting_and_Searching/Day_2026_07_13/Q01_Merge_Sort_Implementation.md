# Merge Sort Implementation

## Problem Statement
The problem requires implementing the merge sort algorithm to sort an array of integers in ascending order. The input array can contain duplicate elements and can be of any size. The algorithm should be stable, meaning that the order of equal elements should be preserved. For example, given the input array `[5, 2, 8, 3, 1, 6, 4]`, the output should be `[1, 2, 3, 4, 5, 6, 8]`. The algorithm should also handle edge cases such as an empty array or an array with a single element.

## Approach
Merge sort is a divide-and-conquer algorithm that recursively divides the input array into two halves until each half has only one element, and then merges the halves back together in sorted order. The algorithm uses a temporary array to store the merged result. The merging process involves comparing elements from the two halves and placing the smaller element in the temporary array.

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

    // Merge the two subarrays
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

// Function to implement merge sort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        // Calculate the midpoint of the subarray
        int mid = left + (right - left) / 2;

        // Recursively sort the left and right subarrays
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Merge the two sorted subarrays
        merge(arr, left, mid, right);
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
    int arr[] = {5, 2, 8, 3, 1, 6, 4};
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, size);

    mergeSort(arr, 0, size - 1);

    cout << "Sorted array: ";
    printArray(arr, size);

    return 0;
}
```

## Test Cases
```
Input: [5, 2, 8, 3, 1, 6, 4]
Output: [1, 2, 3, 4, 5, 6, 8]

Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]

Input: []
Output: []

Input: [1]
Output: [1]
```

## Key Takeaways
- Merge sort is a stable sorting algorithm, meaning that the order of equal elements is preserved.
- Merge sort has a time complexity of O(n log n) and a space complexity of O(n), making it suitable for large datasets.
- The algorithm uses a divide-and-conquer approach to recursively divide the input array into smaller subarrays and then merge them back together in sorted order.