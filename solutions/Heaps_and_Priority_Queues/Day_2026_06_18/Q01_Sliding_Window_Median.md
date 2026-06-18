# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` within an array of integers. The array is scanned from left to right, and at each position, the median of the current window is calculated. The window slides one step to the right after each calculation. The goal is to find the median at each window position. For example, given the array `[1, 3, -1, -3, 5, 3, 6, 7]` and a window size `k = 3`, the medians at each window position would be `[1, -1, -1, 3, 5, 6]`.

## Approach
The algorithm uses two heaps: a max heap to store the smaller half of the window and a min heap to store the larger half. The max heap stores the smaller half of the numbers, and the min heap stores the larger half. This allows for efficient calculation of the median.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max heap to store smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min heap to store larger half

    void addNum(int num) {
        // add num to correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // balance heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // calculate median
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }
};

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    MedianFinder mf;
    vector<double> medians;
    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            // remove num that is out of window
            if (nums[i - k] <= mf.maxHeap.top()) {
                // remove from max heap
                if (mf.maxHeap.top() == nums[i - k]) {
                    mf.maxHeap.pop();
                }
            } else {
                // remove from min heap
                if (mf.minHeap.top() == nums[i - k]) {
                    mf.minHeap.pop();
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
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1, -1, -1, 3, 5, 6]
```

## Key Takeaways
- Use two heaps to efficiently calculate the median of a sliding window.
- Balance the heaps to ensure the max heap stores the smaller half and the min heap stores the larger half.
- Remove numbers that are out of the window from the heaps.