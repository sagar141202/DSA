# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` in an array of integers. The array is given as `nums`, and the size of the sliding window is given as `k`. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. The problem requires finding the median for each position of the sliding window and returning these medians in a list. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[1, -1, -1, 3, 5, 6]`.

## Approach
The approach to solving this problem is to use two heaps: a max heap to store the smaller half of the numbers in the window and a min heap to store the larger half. This allows for efficient calculation of the median.

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
    vector<double> medians;
    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            // remove the num that is out of the window
            if (nums[i - k] <= mf.maxHeap.top()) {
                // remove from max heap
                priority_queue<int> newMaxHeap;
                while (!mf.maxHeap.empty()) {
                    if (mf.maxHeap.top() != nums[i - k]) {
                        newMaxHeap.push(mf.maxHeap.top());
                    }
                    mf.maxHeap.pop();
                }
                mf.maxHeap = newMaxHeap;
            } else {
                // remove from min heap
                priority_queue<int, vector<int>, greater<int>> newMinHeap;
                while (!mf.minHeap.empty()) {
                    if (mf.minHeap.top() != nums[i - k]) {
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
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1, -1, -1, 3, 5, 6]
```

## Key Takeaways
- The use of two heaps allows for efficient calculation of the median in a sliding window.
- Balancing the heaps is necessary to ensure the median can be calculated correctly.
- Removing numbers from the heaps that are out of the window is necessary to maintain the correctness of the median calculation.