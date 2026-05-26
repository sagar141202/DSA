# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each window of size `k` that slides over the entire array. The window slides to the right by one position at a time. If the input array is empty or `k` is larger than the array length, return an empty array. For example, if `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]`.

## Approach
The algorithm uses a deque to store the indices of the elements in the current window. It maintains the deque in such a way that the front always contains the index of the maximum element in the current window. The deque is updated by removing the elements that are out of the window and the elements that are smaller than the current element.

## Complexity
- Time: O(n)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    // Check if the input array is empty or k is larger than the array length
    if (nums.empty() || k > nums.size()) {
        return {};
    }

    // Initialize the result vector and the deque
    vector<int> result;
    deque<int> dq;

    // Iterate over the array
    for (int i = 0; i < nums.size(); i++) {
        // Remove the elements that are out of the window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }

        // Remove the elements that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        // Add the current element to the deque
        dq.push_back(i);

        // Add the maximum element in the current window to the result vector
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }

    return result;
}
```

## Test Cases
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Input: nums = [1], k = 1
Output: [1]
Input: nums = [], k = 1
Output: []
```

## Key Takeaways
- Use a deque to store the indices of the elements in the current window.
- Maintain the deque in such a way that the front always contains the index of the maximum element in the current window.
- Update the deque by removing the elements that are out of the window and the elements that are smaller than the current element.