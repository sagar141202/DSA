# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each subarray of size `k`. The subarray can start at any index `i` where `0 <= i <= nums.size() - k`. The result should be an array of maximum values, one for each subarray of size `k`.

## Approach
The algorithm uses a deque to store the indices of the elements in the current window. It maintains the deque such that the front always contains the index of the maximum element in the window. The deque is updated as the window slides to the right. This approach ensures that the maximum element in each window is found efficiently.

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
        // Remove the elements from the back of the deque that are out of the current window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }

        // Remove the elements from the back of the deque that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        // Add the current element to the deque
        dq.push_back(i);

        // Add the maximum element of the current window to the result
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
```

## Key Takeaways
- The deque is used to store the indices of the elements in the current window, which allows for efficient removal of elements that are out of the window.
- The deque is maintained such that the front always contains the index of the maximum element in the window, which allows for efficient retrieval of the maximum element.
- The algorithm has a time complexity of O(n) because each element is pushed and popped from the deque exactly once.