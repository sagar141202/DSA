# Merge Sort Implementation

## Problem Statement
The problem requires implementing the Merge Sort algorithm to sort an array of integers in ascending order. Merge Sort is a divide-and-conquer algorithm that splits the input array into two halves, recursively sorts them, and then merges the sorted halves. The input array can contain duplicate elements and can be of any size. For example, given the array [5, 2, 8, 1, 9], the output should be [1, 2, 5, 8, 9].

## Approach
The Merge Sort algorithm works by dividing the input array into two halves, recursively sorting them, and then merging the sorted halves. This process continues until the base case is reached, at which point the sorted subarrays are merged to form the final sorted array. The merge step involves comparing elements from the two sorted subarrays and placing the smaller element in the resulting array.

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
    int leftArr[n1], rightArr[n2];

    // Copy data to temporary arrays
    for (int i = 0; i < n1; i++)
        leftArr[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        rightArr[j] = arr[mid + 1 + j];

    // Merge the temporary arrays
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of leftArr[], if there are any
    while (i < n1) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }

    // Copy the remaining elements of rightArr[], if there are any
    while (j < n2) {
        arr[k] = rightArr[j];
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

// Function to print the sorted array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
    int arr[] = {5, 2, 8, 1, 9};
    int arrSize = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, arrSize);

    mergeSort(arr, 0, arrSize - 1);

    cout << "Sorted array: ";
    printArray(arr, arrSize);

    return 0;
}
```

## Test Cases
```
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]

Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]

Input: [4, 2, 9, 6, 23, 12, 34, 0, 1]
Output: [0, 1, 2, 4, 6, 9, 12, 23, 34]
```

## Key Takeaways
- Merge Sort has a time complexity of O(n log n), making it suitable for large datasets.
- The algorithm uses a divide-and-conquer approach to sort the array, which helps to reduce the time complexity.
- Merge Sort is a stable sorting algorithm, meaning that the order of equal elements is preserved.