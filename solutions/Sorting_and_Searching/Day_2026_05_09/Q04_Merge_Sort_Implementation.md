# Merge Sort Implementation

## Problem Statement
Given an array of integers, implement the merge sort algorithm to sort the array in ascending order. The merge sort algorithm is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, and then merges them. The algorithm should be able to handle arrays of size up to 10^5 and integers in the range of -10^9 to 10^9. For example, if the input array is [5, 2, 8, 3, 1, 6, 4], the output should be [1, 2, 3, 4, 5, 6, 8].

## Approach
The merge sort algorithm works by recursively dividing the input array into two halves until each subarray has only one element, and then merging the subarrays to produce the sorted array. The merge step involves comparing elements from two subarrays and placing the smaller element in the output array.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// function to merge two subarrays
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // create temporary arrays
    int leftArr[n1], rightArr[n2];

    // copy data to temporary arrays
    for (int i = 0; i < n1; i++)
        leftArr[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        rightArr[j] = arr[mid + 1 + j];

    // merge the temporary arrays
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

    // copy remaining elements, if any
    while (i < n1) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

// function to implement merge sort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // recursively sort the subarrays
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // merge the sorted subarrays
        merge(arr, left, mid, right);
    }
}

// function to print the array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
    int arr[] = {5, 2, 8, 3, 1, 6, 4};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, n);

    mergeSort(arr, 0, n - 1);

    cout << "Sorted array: ";
    printArray(arr, n);

    return 0;
}
```

## Test Cases
```
Input: [5, 2, 8, 3, 1, 6, 4]
Output: [1, 2, 3, 4, 5, 6, 8]
Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]
```

## Key Takeaways
- Merge sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, and then merges them.
- The time complexity of merge sort is O(n log n), making it suitable for large datasets.
- The space complexity of merge sort is O(n), as it requires additional space for the temporary arrays.