# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the first `k` elements. The array is 1-indexed, and the closest elements are defined as the elements with the smallest absolute difference with `x`. For example, given `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`.

## Approach
We can use a two-pointer technique to find the closest elements. We maintain two pointers, `left` and `right`, and try to find the `k` closest elements by comparing the absolute differences between `arr[left]` and `x`, and `arr[right]` and `x`. We move the pointers based on the comparison result.

## Complexity
- Time: O(log(n) + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        // Find the insertion point of x in the array
        int left = 0, right = arr.size() - k;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // If x - arr[mid] > arr[mid + k] - x, move the left pointer
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
Output: [1, 5, 10]
```

## Key Takeaways
- Use a two-pointer technique to find the closest elements.
- Compare the absolute differences between `arr[left]` and `x`, and `arr[right]` and `x` to move the pointers.
- Return the `k` closest elements based on the final position of the pointers.