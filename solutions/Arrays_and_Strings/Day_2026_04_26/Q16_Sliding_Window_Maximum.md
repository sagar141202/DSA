# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray. The subarray should be fully contained within the array, and the subarray should have a fixed size `k`. For example, given `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]`.

## Approach
The algorithm uses a deque to keep track of the indices of the maximum elements in the current window. It iterates over the array, adding elements to the deque and removing elements that are out of the current window or smaller than the current element.

## Complexity
- Time: O(n)
- Space: O(k)

## C++ Solution
```cpp
#include <deque>
#include <vector>

class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        // Initialize the result vector and the deque
        std::vector<int> result;
        std::deque<int> dq;

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

            // Add the current element to the deque
            dq.push_back(i);

            // Add the maximum element in the current window to the result vector
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }

        return result;
    }
};
```

## Test Cases
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Input: nums = [1], k = 1
Output: [1]
```

## Key Takeaways
- Use a deque to keep track of the indices of the maximum elements in the current window.
- Remove elements from the deque that are out of the current window or smaller than the current element.
- Add the maximum element in the current window to the result vector.