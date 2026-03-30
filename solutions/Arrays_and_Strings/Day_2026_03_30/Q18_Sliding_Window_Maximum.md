# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray. The subarray should be a contiguous part of the original array. For example, given `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]`. The constraints are `1 <= nums.length <= 10^5` and `1 <= k <= nums.length`.

## Approach
The algorithm uses a deque to store the indices of the elements in the current window. The deque is maintained in such a way that the front always contains the index of the maximum element in the current window. The deque is updated by removing the elements that are out of the current window and the elements that are smaller than the current element.

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
        std::vector<int> result;
        std::deque<int> dq;

        for (int i = 0; i < nums.size(); i++) {
            // Remove elements that are out of the current window
            while (!dq.empty() && dq.front() < i - k + 1) {
                dq.pop_front();
            }

            // Remove elements that are smaller than the current element
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }

            // Add the current element to the deque
            dq.push_back(i);

            // Add the maximum element to the result if the window is full
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
Input: nums = [1,-1], k = 1
Output: [1,-1]
```

## Key Takeaways
- Use a deque to store the indices of the elements in the current window.
- Maintain the deque in such a way that the front always contains the index of the maximum element in the current window.
- Update the deque by removing the elements that are out of the current window and the elements that are smaller than the current element.