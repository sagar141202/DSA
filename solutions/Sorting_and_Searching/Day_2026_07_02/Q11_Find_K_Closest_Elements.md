# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array is 1-indexed, and the answer should be returned in ascending order. For example, given `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`. The constraints are `1 <= k <= arr.length` and `-10^7 <= arr[i] <= 10^7`.

## Approach
The approach involves using a two-pointer technique to find the closest elements. We will first find the index of the closest element to the target `x` using binary search. Then, we will expand outwards from this index to find the `k` closest elements.

## Complexity
- Time: O(log n + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    vector<int> result(arr.begin() + left, arr.begin() + left + k);
    return result;
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 7
Output: [1, 5, 10]
```

## Key Takeaways
- Use binary search to find the index of the closest element to the target `x`.
- Expand outwards from the closest index to find the `k` closest elements.
- The two-pointer technique can be used to efficiently find the closest elements.