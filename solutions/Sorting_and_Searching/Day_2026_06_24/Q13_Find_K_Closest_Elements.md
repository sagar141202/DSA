# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. The array `arr` contains distinct integers and is sorted in ascending order. The constraints are: `1 <= k <= arr.length` and `arr.length` is at most `10^4`.

## Approach
The approach is to use a two-pointer technique to find the closest elements. We will use the `lower_bound` function to find the closest element to the target `x`. Then, we will expand our search range to include `k` closest elements.

## Complexity
- Time: O(log n + k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    // Find the closest element to x using lower_bound
    auto it = lower_bound(arr.begin(), arr.end(), x);
    
    // Initialize two pointers
    int left = it - arr.begin();
    int right = left;
    
    // Expand the search range to include k closest elements
    while (right - left < k) {
        if (left == 0) {
            right++;
        } else if (right == arr.size()) {
            left--;
        } else if (x - arr[left - 1] <= arr[right] - x) {
            left--;
        } else {
            right++;
        }
    }
    
    // Return the k closest elements
    return vector<int>(arr.begin() + left, arr.begin() + right);
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
- The `lower_bound` function is used to find the closest element to the target `x`.
- The two-pointer technique is used to expand the search range to include `k` closest elements.
- The solution has a time complexity of O(log n + k) and a space complexity of O(k).