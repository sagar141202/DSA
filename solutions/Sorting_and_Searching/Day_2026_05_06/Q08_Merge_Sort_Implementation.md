# Merge Sort Implementation

## Problem Statement
Merge sort is a divide-and-conquer algorithm that splits a given list of elements into two halves, recursively sorts them, and then merges them. The problem requires implementing the merge sort algorithm to sort a list of integers in ascending order. The input list can contain duplicate elements and can be of any size. The algorithm should be efficient and scalable. For example, given the list [5, 2, 8, 1, 9], the output should be [1, 2, 5, 8, 9].

## Approach
The merge sort algorithm works by dividing the input list into two halves, sorting them recursively, and then merging the sorted halves. This process continues until the base case is reached, where the list contains only one element. The merge step combines two sorted lists into a single sorted list.

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

    // Merge the temporary arrays
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

    // Copy remaining elements, if any
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

// Function to implement merge sort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Recursively sort the subarrays
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

    mergeSort(arr, 0, n - 1);

    // Print the sorted array
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
```

## Test Cases
```
Input: [5, 2, 8, 1, 9]
Output: [1, 2, 5, 8, 9]
Input: [10, 7, 4, 1, 9]
Output: [1, 4, 7, 9, 10]
```

## Key Takeaways
- Merge sort is a divide-and-conquer algorithm that splits the input list into two halves, recursively sorts them, and then merges them.
- The merge step combines two sorted lists into a single sorted list.
- The time complexity of merge sort is O(n log n), making it efficient for large datasets.