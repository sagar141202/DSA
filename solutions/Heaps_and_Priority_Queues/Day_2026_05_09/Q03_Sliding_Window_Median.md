# Sliding Window Median

## Problem Statement
The Sliding Window Median problem is defined as finding the median of all numbers in a sliding window of size `k` over a list of integers `nums`. The window slides one step at a time to the right, and at each step, we need to find the median of the numbers within the current window. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values.

## Approach
We will use two heaps to solve this problem: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. This allows us to efficiently find the median at each step.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> max_heap; // max heap to store the smaller half
    priority_queue<int, vector<int>, greater<int>> min_heap; // min heap to store the larger half

    void addNum(int num) {
        // Add the number to the correct heap
        if (max_heap.empty() || num <= max_heap.top()) {
            max_heap.push(num);
        } else {
            min_heap.push(num);
        }

        // Balance the heaps if necessary
        if (max_heap.size() > min_heap.size() + 1) {
            min_heap.push(max_heap.top());
            max_heap.pop();
        } else if (min_heap.size() > max_heap.size()) {
            max_heap.push(min_heap.top());
            min_heap.pop();
        }
    }

    double findMedian() {
        // Calculate the median based on the sizes of the heaps
        if (max_heap.size() == min_heap.size()) {
            return (max_heap.top() + min_heap.top()) / 2.0;
        } else {
            return (double)max_heap.top();
        }
    }
};

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    MedianFinder mf;
    vector<double> medians;
    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            // Remove the number that is out of the window
            if (nums[i - k] <= mf.max_heap.top()) {
                // Remove from max heap
                priority_queue<int> new_max_heap;
                while (mf.max_heap.top() != nums[i - k]) {
                    new_max_heap.push(mf.max_heap.top());
                    mf.max_heap.pop();
                }
                mf.max_heap.pop();
                while (!new_max_heap.empty()) {
                    mf.max_heap.push(new_max_heap.top());
                    new_max_heap.pop();
                }
            } else {
                // Remove from min heap
                priority_queue<int, vector<int>, greater<int>> new_min_heap;
                while (mf.min_heap.top() != nums[i - k]) {
                    new_min_heap.push(mf.min_heap.top());
                    mf.min_heap.pop();
                }
                mf.min_heap.pop();
                while (!new_min_heap.empty()) {
                    mf.min_heap.push(new_min_heap.top());
                    new_min_heap.pop();
                }
            }
        }
        if (i >= k - 1) {
            medians.push_back(mf.findMedian());
        }
    }
    return medians;
}
```

## Test Cases
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1,-1,-1,3,5,6]
```

## Key Takeaways
- The use of two heaps allows for efficient calculation of the median at each step.
- The heaps must be balanced to ensure the median can be calculated correctly.
- Removing elements from the heaps can be done by creating a new heap and pushing all elements except the one to be removed.