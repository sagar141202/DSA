# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array is sorted in ascending order. For example, given `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`. The constraints are `1 <= k <= arr.size()` and `arr` is a sorted array.

## Approach
The algorithm uses a two-pointer approach to find the subarray of `k` closest elements. It first finds the closest element to `x` using binary search. Then, it expands outwards from the closest element to find the `k` closest elements.

## Complexity
- Time: O(log n + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0, right = arr.size() - k;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // If x - arr[mid] > arr[mid + k] - x, it means the closest element is on the right side
            if (x - arr[mid] > arr[mid + k] - x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        // Return the subarray of k closest elements
        return vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [1, 5, 10]
```

## Key Takeaways
- Use binary search to find the closest element to the target value.
- Expand outwards from the closest element to find the `k` closest elements.
- Use a two-pointer approach to find the subarray of `k` closest elements.