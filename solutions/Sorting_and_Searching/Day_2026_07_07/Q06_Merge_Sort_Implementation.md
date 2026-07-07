# Merge Sort Implementation

## Problem Statement
Merge sort is a divide-and-conquer algorithm that splits an input array into two halves, recursively sorts each half, and then merges the two sorted halves. The problem requires implementing the merge sort algorithm to sort an array of integers in ascending order. The input array can contain duplicate elements and can be of any size. For example, given the array [5, 2, 8, 1, 9], the output should be [1, 2, 5, 8, 9]. The algorithm should have a time complexity of O(n log n) and a space complexity of O(n).

## Approach
The merge sort algorithm works by recursively dividing the input array into two halves until each sub-array contains only one element. Then, it merges the sub-arrays in a way that maintains the sorted order. The merge step uses a temporary array to store the merged result.

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
```

## Key Takeaways
- Merge sort is a divide-and-conquer algorithm that splits the input array into two halves, recursively sorts each half, and then merges the two sorted halves.
- The merge step uses a temporary array to store the merged result, which requires O(n) extra space.
- The time complexity of merge sort is O(n log n) due to the recursive division and merging of the array.