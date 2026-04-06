# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray. The subarray should be fully contained within the array, and the maximum value should be returned in the order of the subarrays. For example, given `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the function should return `[3,3,5,5,6,7]`. The array `nums` has a length of `n`, where `1 <= n <= 10^5`, and `1 <= k <= n`. The array `nums` contains integers in the range `[-10^4, 10^4]`.

## Approach
The solution utilizes a deque to store the indices of the elements in the current window, where the front of the deque stores the index of the maximum element. The deque is updated by removing elements that are out of the current window and elements that are smaller than the current element. The maximum element in each window is added to the result.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    // Initialize the result vector and the deque
    vector<int> result;
    deque<int> dq;

    // Iterate over the array
    for (int i = 0; i < nums.size(); i++) {
        // Remove elements from the back of the deque that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        // Remove elements from the front of the deque that are out of the current window
        while (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }

        // Add the current element to the deque
        dq.push_back(i);

        // Add the maximum element in the current window to the result
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
Input: nums = [1,-1], k = 1
Output: [1,-1]
```

## Key Takeaways
- Use a deque to store the indices of the elements in the current window.
- Update the deque by removing elements that are out of the current window and elements that are smaller than the current element.
- The maximum element in each window is the element at the front of the deque.