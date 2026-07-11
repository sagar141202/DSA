# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each subarray of size `k` using the sliding window technique. The function should return a vector of integers, where each integer represents the maximum value in the corresponding subarray. For example, given `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]`.

## Approach
The algorithm uses a deque to store the indices of the elements in the current window, ensuring that the front of the deque always contains the index of the maximum element. As the window slides, elements are added and removed from the deque based on their values and positions. This approach allows for efficient calculation of the maximum value in each subarray.

## Complexity
- Time: O(n)
- Space: O(k)

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
        // Remove elements from the back of the deque that are out of the current window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }

        // Remove elements from the back of the deque that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        // Add the current element to the back of the deque
        dq.push_back(i);

        // Add the maximum element to the result vector if the window is full
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
- Use a deque to store the indices of the elements in the current window, allowing for efficient calculation of the maximum value.
- Remove elements from the deque based on their values and positions to ensure that the front of the deque always contains the index of the maximum element.
- The time complexity is O(n) because each element is processed once, and the space complexity is O(k) because the deque stores at most k elements.