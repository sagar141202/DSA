# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` within an array of integers. The window slides one step at a time, and for each position, we need to find the median of the numbers within the current window. The array can contain both positive and negative integers, and the window size `k` is given as input. For example, given the array `[1, 3, -1, -3, 5, 3, 6, 7]` and a window size of `3`, the medians for each window position would be calculated.

## Approach
We utilize two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap stores the smaller half of the numbers, and the min heap stores the larger half. This allows us to efficiently calculate the median.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max heap for smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min heap for larger half

    void addNum(int num) {
        // Add number to correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // Balance heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // Calculate median based on heap sizes
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }

    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> medians;
        for (int i = 0; i < nums.size(); i++) {
            addNum(nums[i]);
            if (i >= k) {
                // Remove number going out of window
                int num = nums[i - k];
                if (num <= maxHeap.top()) {
                    // Remove from max heap
                    maxHeap = priority_queue<int>();
                    for (int j = i - k + 1; j <= i; j++) {
                        addNum(nums[j]);
                    }
                } else {
                    // Remove from min heap
                    minHeap = priority_queue<int, vector<int>, greater<int>>();
                    for (int j = i - k + 1; j <= i; j++) {
                        addNum(nums[j]);
                    }
                }
            }
            if (i >= k - 1) {
                medians.push_back(findMedian());
            }
        }
        return medians;
    }
};
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

## Key Takeaways
- Use two heaps to efficiently calculate the median of a sliding window.
- Balance the heaps to ensure the max heap size is at most one more than the min heap size.
- Remove numbers going out of the window by rebalancing the heaps.