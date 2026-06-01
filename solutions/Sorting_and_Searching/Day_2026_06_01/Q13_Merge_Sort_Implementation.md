# Merge Sort Implementation

## Problem Statement
Merge sort is a divide-and-conquer algorithm that splits an input array into two halves, recursively sorts them, and then merges them. Given an array of integers, implement the merge sort algorithm to sort the array in ascending order. The input array can contain duplicate elements and can be of any size. For example, if the input array is `[5, 2, 8, 1, 9]`, the output should be `[1, 2, 5, 8, 9]`.

## Approach
The merge sort algorithm works by dividing the input array into two halves, sorting them recursively, and then merging the sorted halves. This process continues until the base case is reached, at which point the sorted array is returned. The merge step combines two sorted arrays into a single sorted array.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to merge two sorted subarrays
void merge(int arr[], int left, int mid, int right) {
    // Create temporary arrays to store the left and right subarrays
    int leftSize = mid - left + 1;
    int rightSize = right - mid;
    int leftArr[leftSize], rightArr[rightSize];

    // Copy the left and right subarrays into the temporary arrays
    for (int i = 0; i < leftSize; i++) {
        leftArr[i] = arr[left + i];
    }
    for (int i = 0; i < rightSize; i++) {
        rightArr[i] = arr[mid + 1 + i];
    }

    // Merge the left and right subarrays into the original array
    int i = 0, j = 0, k = left;
    while (i < leftSize && j < rightSize) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }

    // Copy any remaining elements from the left subarray
    while (i < leftSize) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }

    // Copy any remaining elements from the right subarray
    while (j < rightSize) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

// Function to implement the merge sort algorithm
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        // Calculate the midpoint of the array
        int mid = left + (right - left) / 2;

        // Recursively sort the left and right subarrays
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Merge the sorted subarrays
        merge(arr, left, mid, right);
    }
}

// Example usage
int main() {
    int arr[] = {5, 2, 8, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Print the original array
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Sort the array using merge sort
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

Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]

Input: [4, 2, 9, 6, 5, 1]
Output: [1, 2, 4, 5, 6, 9]
```

## Key Takeaways
- Merge sort has a time complexity of O(n log n) and is suitable for large datasets.
- The algorithm uses a divide-and-conquer approach to sort the array.
- The merge step is the key to the merge sort algorithm, as it combines two sorted subarrays into a single sorted array.