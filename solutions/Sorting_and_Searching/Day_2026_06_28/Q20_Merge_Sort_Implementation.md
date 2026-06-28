# Merge Sort Implementation

## Problem Statement
Given an array of integers, implement the Merge Sort algorithm to sort the array in ascending order. The array can contain duplicate elements and can be of any size. The algorithm should be efficient and scalable. For example, if the input array is `[5, 2, 8, 1, 9]`, the output should be `[1, 2, 5, 8, 9]`. The algorithm should handle edge cases such as an empty array or an array with a single element.

## Approach
Merge Sort is a divide-and-conquer algorithm that splits the input array into two halves, recursively sorts each half, and then merges the two sorted halves. The merging process involves comparing elements from each half and placing the smaller element in the result array. This process continues until the entire array is sorted.

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

    // Merge the temp arrays back into arr[]
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
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

// Function to print the array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Driver code
int main() {
    int arr[] = {5, 2, 8, 1, 9};
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
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]
Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]
Input: []
Output: []
Input: [1]
Output: [1]
```

## Key Takeaways
- Merge Sort is a divide-and-conquer algorithm that splits the input array into two halves, recursively sorts each half, and then merges the two sorted halves.
- The time complexity of Merge Sort is O(n log n), making it suitable for large datasets.
- The space complexity of Merge Sort is O(n), as it requires additional memory to store the temporary arrays during the merging process.