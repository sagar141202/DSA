# Find K Closest Elements

## Problem Statement
Given a sorted array, find the K closest elements to a target value. The closest elements are defined as the elements with the smallest absolute difference to the target. If there are multiple elements with the same smallest absolute difference, the elements with the smaller value are considered closer. The function should return the K closest elements in sorted order.

## Approach
The algorithm uses a two-pointer technique to find the K closest elements. It first finds the closest element to the target using binary search, then expands outwards to find the remaining K-1 closest elements. The elements are compared based on their absolute difference to the target.

## Complexity
- Time: O(logN + K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    // Find the insertion point for x in arr to determine the closest element
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        // Decide whether to move the left pointer or the right pointer
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    // Return the k closest elements
    return vector<int>(arr.begin() + left, arr.begin() + left + k);
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 4;
    int x = 3;
    vector<int> result = findClosestElements(arr, k, x);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [5, 10, 15]
```

## Key Takeaways
- The two-pointer technique is useful for finding the closest elements in a sorted array.
- Binary search can be used to find the insertion point for the target value in the array.
- The comparison of elements is based on their absolute difference to the target value.