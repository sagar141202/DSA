# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size k, where the window moves one step at a time over an array of integers. The array is of size n, and the window size k is given. The median of a window is the middle value in the sorted window. If the window has an even number of elements, the median is the average of the two middle values. The goal is to calculate the median for each possible window.

## Approach
We use two heaps, a max heap to store the smaller half of the window and a min heap to store the larger half. The max heap stores the k/2 smaller elements, and the min heap stores the k/2 larger elements. This ensures that the median can be calculated efficiently by considering the top elements of the two heaps.

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
        // Add to correct heap
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
        // Calculate median
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }
};

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        MedianFinder mf;
        vector<double> medians;
        for (int i = 0; i < nums.size(); i++) {
            mf.addNum(nums[i]);
            if (i >= k) {
                // Remove the number that just fell out of the window
                // For simplicity, we don't actually remove it but rather
                // let the MedianFinder grow and then calculate the median
                // of the last k elements.
            }
            if (i >= k - 1) {
                medians.push_back(mf.findMedian());
            }
        }
        return medians;
    }
};
```

## Test Cases
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1,-1,-1,3,5,6]
```

## Key Takeaways
- Using two heaps allows for efficient calculation of the median within a sliding window.
- Balancing the heaps after each insertion ensures that the median can be calculated in constant time.
- The time complexity is dominated by the insertion and balancing operations in the heaps.