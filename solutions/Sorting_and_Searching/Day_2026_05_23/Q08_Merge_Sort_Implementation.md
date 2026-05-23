# Merge Sort Implementation

## Problem Statement
The problem requires implementing the Merge Sort algorithm to sort an array of integers in ascending order. Given an array of integers, the goal is to rearrange the elements in a way that they are in increasing order. The array can contain duplicate elements and can be of any size. For example, if the input array is `[64, 34, 25, 12, 22, 11, 90]`, the output should be `[11, 12, 22, 25, 34, 64, 90]`.

## Approach
The Merge Sort algorithm uses a divide-and-conquer approach to sort the array. It divides the array into two halves, recursively sorts each half, and then merges the two sorted halves. This process continues until the entire array is sorted.

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
```

## Key Takeaways
- Merge Sort is a divide-and-conquer algorithm that splits the array into two halves, recursively sorts each half, and then merges the two sorted halves.
- The time complexity of Merge Sort is O(n log n), making it suitable for large datasets.
- Merge Sort is a stable sorting algorithm, meaning that the order of equal elements is preserved.