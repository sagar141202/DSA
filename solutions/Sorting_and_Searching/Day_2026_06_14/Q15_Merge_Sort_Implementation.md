# Merge Sort Implementation

## Problem Statement
Given an array of integers, implement the merge sort algorithm to sort the array in ascending order. The array can contain duplicate elements and the size of the array can range from 1 to 10^5. For example, if the input array is [5, 3, 8, 4, 2], the output should be [2, 3, 4, 5, 8].

## Approach
The merge sort algorithm works by recursively dividing the array into two halves until each half contains one element, and then merging the halves back together in sorted order. This process continues until the entire array is sorted. The algorithm uses a divide-and-conquer approach to achieve a time complexity of O(n log n).

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

    // Create temporary arrays
    int L[n1], R[n2];

    // Copy data to temporary arrays
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Merge the temporary arrays back into arr
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
        // Same as (left+right)/2, but avoids overflow for large left and right
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

// Driver code
int main() {
    int arr[] = {5, 3, 8, 4, 2};
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
Input: [5, 3, 8, 4, 2]
Output: [2, 3, 4, 5, 8]

Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]

Input: [1, 2, 3, 4, 5]
Output: [1, 2, 3, 4, 5]
```

## Key Takeaways
- Merge sort is a divide-and-conquer algorithm that splits the array into two halves, recursively sorts them, and then merges them back together in sorted order.
- The time complexity of merge sort is O(n log n), making it suitable for large datasets.
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements.