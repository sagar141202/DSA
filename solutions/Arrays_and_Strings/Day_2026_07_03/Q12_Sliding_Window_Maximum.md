# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each subarray of size `k`. The subarray can start at any index in the array and must contain `k` consecutive elements. The goal is to find the maximum value in each of these subarrays and return them in an array. For example, if `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]`.

## Approach
The algorithm uses a deque to store the indices of the elements in the current window. It iterates over the array, removing elements from the back of the deque that are out of the current window and elements from the front that are smaller than the current element. The maximum element in the current window is then added to the result array.

## Complexity
- Time: O(n)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    // Initialize the result array and the deque
    vector<int> result;
    deque<int> dq;

    // Iterate over the array
    for (int i = 0; i < nums.size(); i++) {
        // Remove elements from the back of the deque that are out of the current window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }

        // Remove elements from the front of the deque that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        // Add the current element to the deque
        dq.push_back(i);

        // Add the maximum element in the current window to the result array
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
- The deque is used to store the indices of the elements in the current window, allowing for efficient removal of elements that are out of the window or smaller than the current element.
- The algorithm has a time complexity of O(n) because each element is added and removed from the deque at most once.
- The space complexity is O(k) because the deque can contain at most k elements.