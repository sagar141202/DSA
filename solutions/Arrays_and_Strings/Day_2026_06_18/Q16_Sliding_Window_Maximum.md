# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray. The subarray should be fully contained within the array, and the `k`-sized window should slide from the start of the array to the end. For example, given `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]`.

## Approach
We will use a deque to store the indices of the elements in the current window. The deque will be maintained in such a way that the front always contains the maximum element in the current window. We will iterate over the array, adding elements to the deque and removing elements that are out of the current window.

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
        // Remove elements from the back of the deque that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        // Add the current element to the deque
        dq.push_back(i);

        // Remove elements from the front of the deque that are out of the current window
        if (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }

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
```

## Key Takeaways
- Use a deque to efficiently maintain the maximum element in the current window.
- Remove elements from the deque that are out of the current window to avoid unnecessary comparisons.
- The time complexity is O(n) because each element is added and removed from the deque at most once.