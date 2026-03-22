# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. The closest elements are defined as the `k` elements with the smallest absolute difference to `x`. If there are multiple elements with the same absolute difference, the smaller element is considered closer. The array `arr` has `n` elements, and `1 <= k <= n`. The target value `x` can be any integer.

## Approach
We can use a two-pointer technique to find the `k` closest elements. We first find the insertion point of `x` in the sorted array using binary search. Then, we expand outwards from this point, comparing the absolute differences between `x` and the elements on either side.

## Complexity
- Time: O(log n + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findKClosestElements(vector<int>& arr, int k, int x) {
    // Find the insertion point of x in the sorted array using binary search
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        // If x - arr[mid] > arr[mid + k] - x, then the k closest elements must be to the right of mid
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    // Return the k closest elements
    return vector<int>(arr.begin() + left, arr.begin() + left + k);
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [1, 5, 10]
```

## Key Takeaways
- The two-pointer technique can be used to find the `k` closest elements in a sorted array.
- Binary search can be used to find the insertion point of the target value `x` in the sorted array.
- The time complexity is O(log n + k) because we perform a binary search and then expand outwards from the insertion point.