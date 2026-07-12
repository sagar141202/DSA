# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array is 1-indexed, and the closest elements are defined as the elements with the smallest absolute difference to the target `x`. For example, given `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`.

## Approach
We will use a two-pointer approach to find the closest elements. We will first find the index of the closest element to `x` using binary search, then expand outwards to find the `k` closest elements. The key idea is to maintain a window of `k` elements and slide it to the left or right based on the comparison of the elements at the window boundaries.

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
        // if x - arr[mid] > arr[mid + k] - x, move left pointer to mid + 1
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
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
- Use binary search to find the closest element to `x` in the array.
- Expand outwards from the closest element to find the `k` closest elements.
- Maintain a window of `k` elements and slide it to the left or right based on the comparison of the elements at the window boundaries.