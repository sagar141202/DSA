# Sliding Window Median

## Problem Statement
The median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values, and the median is their mean. Given a list of integers `nums` and an integer `k`, return the median of each `k`-sized subarray (or window) within the list. The test cases will be such that the size of each window is either even or odd, and the median will always be an integer.

## Approach
We can solve this problem using two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain the balance between the two heaps to efficiently calculate the median.

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
                mf.maxHeap = priority_queue<int>();
                for (int j = i - k + 1; j <= i; j++) {
                    mf.addNum(nums[j]);
                }
            } else {
                // remove from min heap
                mf.minHeap = priority_queue<int, vector<int>, greater<int>>();
                for (int j = i - k + 1; j <= i; j++) {
                    mf.addNum(nums[j]);
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
- Using two heaps (max heap and min heap) to store the smaller and larger half of the numbers can efficiently calculate the median.
- Maintaining the balance between the two heaps is crucial to ensure the correct calculation of the median.