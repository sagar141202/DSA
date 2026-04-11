# Merge Sort Implementation

## Problem Statement
Given an array of integers, implement the Merge Sort algorithm to sort the array in ascending order. The array can contain duplicate elements and the size of the array is not fixed. The algorithm should be efficient and scalable. For example, if the input array is [64, 34, 25, 12, 22, 11, 90], the output should be [11, 12, 22, 25, 34, 64, 90].

## Approach
Merge Sort is a divide-and-conquer algorithm that splits the input array into two halves, recursively sorts them, and then merges the sorted halves. The algorithm uses a temporary array to store the merged result. The key idea is to divide the array into smaller sub-arrays, sort them individually, and then combine the sorted sub-arrays.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
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
Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]
Input: [10, 7, 4, 1, 9, 3]
Output: [1, 3, 4, 7, 9, 10]
```

## Key Takeaways
- Merge Sort has a time complexity of O(n log n) in all cases (best, average, worst).
- Merge Sort is a stable sorting algorithm, preserving the order of equal elements.
- Merge Sort requires extra space for the temporary array, making it less efficient in terms of memory usage.