# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array `arr` contains distinct integers and is sorted in ascending order. The constraints are: `1 <= k <= arr.size()` and `arr` does not contain `x`.

## Approach
The algorithm uses a two-pointer technique to find the closest elements. It first finds the insertion point of `x` in the array using binary search, then expands outwards to find the `k` closest elements. This approach ensures that the closest elements are found efficiently.

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
        // Find the insertion point of x in the array using binary search
        int left = 0, right = arr.size() - k;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // If x - arr[mid] > arr[mid + k] - x, move the left pointer to mid + 1
            if (x - arr[mid] > arr[mid + k] - x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        // Return the k closest elements
        return vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};
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
- Binary search can be used to find the insertion point of a target value in a sorted array.
- Expanding outwards from the insertion point can help find the k closest elements.