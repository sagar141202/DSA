# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray. The subarray is defined as the set of elements between indices `i` and `i + k - 1` (inclusive) where `0 <= i <= nums.size() - k`. The result should be returned as an array of integers where each element is the maximum value in the corresponding `k`-sized subarray.

## Approach
We will use a deque to store the indices of the elements in the current window. The deque will be maintained in such a way that the front always contains the index of the maximum element in the current window. We will remove the elements from the back of the deque that are out of the current window and the elements from the front that are smaller than the current element.

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

        // Add the current element to the back of the deque
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
```

## Key Takeaways
- The deque is used to store the indices of the elements in the current window.
- The deque is maintained in such a way that the front always contains the index of the maximum element in the current window.
- The time complexity is O(n) because each element is pushed and popped from the deque exactly once.