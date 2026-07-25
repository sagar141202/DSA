# Find K Closest Elements

## Problem Statement
Given a sorted array, find the K closest elements to a given target. The closest elements are defined as the elements with the smallest absolute difference to the target. If there are multiple elements with the same smallest absolute difference, the ones with the smaller value should be considered closer. For example, given the array [1, 2, 3, 4, 5] and the target 3, the 3 closest elements are [2, 3, 4]. The array is guaranteed to be sorted in ascending order.

## Approach
We can use a two-pointer technique to find the K closest elements. The idea is to maintain a window of size K and adjust the window based on the absolute difference between the elements and the target. We start by finding the first element that is greater than or equal to the target, then we expand the window to the left and right based on the absolute difference.

## Complexity
- Time: O(logN + K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        // Find the first element that is greater than or equal to the target
        auto it = lower_bound(arr.begin(), arr.end(), x);
        
        // Initialize the left and right pointers
        int left = it - arr.begin();
        int right = left;
        
        // Adjust the window based on the absolute difference
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
        
        // Return the K closest elements
        return vector<int>(arr.begin() + left, arr.begin() + right);
    }
};
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 3, x = 3
Output: [2, 3, 4]

Input: arr = [1, 5, 10, 15, 20], k = 2, x = 8
Output: [5, 10]
```

## Key Takeaways
- Use a two-pointer technique to maintain a window of size K.
- Adjust the window based on the absolute difference between the elements and the target.
- The time complexity is O(logN + K) due to the use of lower_bound and the while loop.