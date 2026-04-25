# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the first `k` elements. The array is 1-indexed, and the answer should be 1-indexed as well. For example, if `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`.

## Approach
We can use a two-pointer approach to find the closest elements. First, we find the index of the closest element to `x` using binary search. Then, we expand outwards from this index to find the `k` closest elements.

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
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [1, 5, 10]
```

## Key Takeaways
- The two-pointer approach allows us to efficiently find the closest elements.
- Binary search can be used to find the index of the closest element to `x`.
- Expanding outwards from the closest element allows us to find the `k` closest elements.