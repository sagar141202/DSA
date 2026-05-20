# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray. The subarray should be fully contained within the array, and the maximum value should be returned in the order that the subarrays appear in the array. For example, given `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]`.

## Approach
We can use a deque to store the indices of the elements in the current window, and remove elements that are out of the window or smaller than the current element. This way, the front of the deque will always contain the index of the maximum element in the current window.

## Complexity
- Time: O(n)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    // Create a deque to store the indices of the elements in the current window
    deque<int> dq;
    // Create a vector to store the maximum values
    vector<int> maxValues;
    
    // Iterate over the array
    for (int i = 0; i < nums.size(); i++) {
        // Remove elements that are out of the window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }
        // Remove elements that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }
        // Add the current element to the deque
        dq.push_back(i);
        // Add the maximum value to the result vector
        if (i >= k - 1) {
            maxValues.push_back(nums[dq.front()]);
        }
    }
    return maxValues;
}
```

## Test Cases
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Input: nums = [1], k = 1
Output: [1]
Input: nums = [1,-1], k = 1
Output: [1,-1]
```

## Key Takeaways
- Use a deque to store the indices of the elements in the current window.
- Remove elements that are out of the window or smaller than the current element to maintain the maximum value at the front of the deque.
- Add the maximum value to the result vector when the window is full.