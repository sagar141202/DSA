# Sliding Window Median

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the median of each `k`-sized subarray. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[1, -1, -1, 3, 5, 6]`. The subarrays are `[1, 3, -1], [3, -1, -3], [-1, -3, 5], [-3, 5, 3], [5, 3, 6], [3, 6, 7]` and their medians are `1, -1, -1, 3, 5, 6` respectively.

## Approach
The algorithm uses two heaps, a max heap to store the smaller half of the window and a min heap to store the larger half. The max heap stores the larger elements of the smaller half and the min heap stores the smaller elements of the larger half. This ensures that the median can be calculated efficiently.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    // max heap to store the smaller half of the window
    priority_queue<int> maxHeap;
    // min heap to store the larger half of the window
    priority_queue<int, vector<int>, greater<int>> minHeap;

    void addNum(int num) {
        // add num to the correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // calculate the median
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }
};

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    MedianFinder mf;
    vector<double> result;
    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            // remove the num that is out of the window
            int numToRemove = nums[i - k];
            if (numToRemove <= mf.maxHeap.top()) {
                // remove from max heap
                priority_queue<int> temp;
                while (mf.maxHeap.top() != numToRemove) {
                    temp.push(mf.maxHeap.top());
                    mf.maxHeap.pop();
                }
                mf.maxHeap.pop();
                while (!temp.empty()) {
                    mf.maxHeap.push(temp.top());
                    temp.pop();
                }
            } else {
                // remove from min heap
                priority_queue<int, vector<int>, greater<int>> temp;
                while (mf.minHeap.top() != numToRemove) {
                    temp.push(mf.minHeap.top());
                    mf.minHeap.pop();
                }
                mf.minHeap.pop();
                while (!temp.empty()) {
                    mf.minHeap.push(temp.top());
                    temp.pop();
                }
            }
        }
        if (i >= k - 1) {
            result.push_back(mf.findMedian());
        }
    }
    return result;
}
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1, -1, -1, 3, 5, 6]
```

## Key Takeaways
- Use two heaps to store the smaller and larger half of the window to efficiently calculate the median.
- Balance the heaps to ensure the size difference is at most 1.
- Remove the num that is out of the window from the correct heap when sliding the window.