# Merge Sort Implementation

## Problem Statement
Given an array of integers, implement the merge sort algorithm to sort the array in ascending order. The merge sort algorithm is a divide-and-conquer algorithm that splits the input array into two halves, recursively sorts them, and then merges them. The algorithm should have a time complexity of O(n log n) and a space complexity of O(n), where n is the number of elements in the array. For example, if the input array is [5, 2, 8, 1, 9], the output should be [1, 2, 5, 8, 9].

## Approach
The merge sort algorithm works by recursively splitting the input array into two halves until each half has only one element, and then merging the halves back together in sorted order. This process is repeated until the entire array is sorted. The key to the algorithm is the merge step, which combines two sorted arrays into a single sorted array.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// function to merge two sorted subarrays
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int L[n1], R[n2];
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    int i = 0, j = 0, k = left;
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
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// function to implement merge sort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
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
    int arr[] = {5, 2, 8, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, n - 1);
    printArray(arr, n);
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
- The merge sort algorithm has a time complexity of O(n log n) and a space complexity of O(n), making it efficient for large datasets.
- The algorithm uses a divide-and-conquer approach to split the input array into smaller subarrays, which are then merged back together in sorted order.
- The merge step is the key to the algorithm, as it combines two sorted subarrays into a single sorted subarray.