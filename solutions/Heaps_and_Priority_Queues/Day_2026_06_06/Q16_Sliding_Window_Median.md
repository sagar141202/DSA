# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` in an array of integers. The window moves one step at a time, and at each step, we need to find the median of the numbers in the current window. The array contains `n` integers, and the window size `k` is given. The median is the middle value in the sorted list of numbers. If the list has an even number of elements, the median is the average of the two middle values.

## Approach
We will use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the `k/2` smallest numbers, and the min heap will store the `k/2` largest numbers. We will balance the heaps to ensure the size difference is at most 1.

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
            // remove num from window
            if (nums[i - k] <= mf.maxHeap.top()) {
                // remove from max heap
                mf.maxHeap.pop();
            } else {
                // remove from min heap
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
Output: [1.0,-1.0,-1.0,3.0,5.0,6.0]
```

## Key Takeaways
- Use two heaps to efficiently calculate the median of a sliding window.
- Balance the heaps to ensure the size difference is at most 1.
- Remove numbers from the window by checking which heap they belong to.