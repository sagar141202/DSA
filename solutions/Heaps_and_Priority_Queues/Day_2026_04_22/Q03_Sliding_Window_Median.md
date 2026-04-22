# Sliding Window Median

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the median of each `k`-sized subarray. The median is the middle value in the sorted subarray. If the subarray has an even number of elements, the median is the average of the two middle values. The function should return a vector of medians, where the `i`-th element is the median of the subarray `nums[i - k + 1..i]`. The constraints are `1 <= k <= nums.size()` and `nums.size()` will be at most `10^5`.

## Approach
The approach involves using two heaps, a max heap to store the smaller half of the elements and a min heap to store the larger half. The max heap will store the `k/2` smallest elements and the min heap will store the `k/2` largest elements. The median will be the top element of the max heap if `k` is odd, or the average of the top elements of both heaps if `k` is even.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max heap to store the smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min heap to store the larger half

    void addNum(int num) {
        // add the number to the correct heap
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
    vector<double> medians;
    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            // remove the oldest number from the window
            int oldest = nums[i - k];
            if (oldest <= mf.maxHeap.top()) {
                // remove from max heap
                priority_queue<int> newMaxHeap;
                while (!mf.maxHeap.empty()) {
                    if (mf.maxHeap.top() != oldest) {
                        newMaxHeap.push(mf.maxHeap.top());
                    }
                    mf.maxHeap.pop();
                }
                mf.maxHeap = newMaxHeap;
            } else {
                // remove from min heap
                priority_queue<int, vector<int>, greater<int>> newMinHeap;
                while (!mf.minHeap.empty()) {
                    if (mf.minHeap.top() != oldest) {
                        newMinHeap.push(mf.minHeap.top());
                    }
                    mf.minHeap.pop();
                }
                mf.minHeap = newMinHeap;
            }
            // rebalance the heaps
            if (mf.maxHeap.size() > mf.minHeap.size() + 1) {
                mf.minHeap.push(mf.maxHeap.top());
                mf.maxHeap.pop();
            } else if (mf.minHeap.size() > mf.maxHeap.size()) {
                mf.maxHeap.push(mf.minHeap.top());
                mf.minHeap.pop();
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
- Use two heaps to maintain the balance between the smaller and larger halves of the elements.
- The max heap stores the `k/2` smallest elements and the min heap stores the `k/2` largest elements.
- The median is the top element of the max heap if `k` is odd, or the average of the top elements of both heaps if `k` is even.