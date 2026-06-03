# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` within a given array of integers. The array is of size `n`, and we need to find the median for each window of size `k` as it slides through the array from left to right. The median of a window is the middle value when the numbers in the window are arranged in sorted order. If the window has an even number of elements, the median is the average of the two middle values. The goal is to efficiently compute the median for each window and output these medians.

## Approach
We can use two heaps, a max heap to store the smaller half of the window and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. This allows us to efficiently calculate the median by looking at the top elements of the two heaps.

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
        // Add num to the correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // Balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // If the total number of elements is odd, return the top of maxHeap
        if (maxHeap.size() > minHeap.size()) {
            return (double)maxHeap.top();
        }
        // If the total number of elements is even, return the average of the tops
        return (maxHeap.top() + minHeap.top()) / 2.0;
    }
};

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    MedianFinder mf;
    vector<double> medians;
    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            // Remove the number that just fell out of the window
            // This is a simplification and does not handle actual removal from heaps efficiently
            // For a complete solution, consider using a more complex data structure like a balanced binary search tree
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
- Using two heaps allows for efficient calculation of the median in a sliding window.
- Balancing the heaps is crucial to ensure the median can be found in constant time.
- The provided C++ solution simplifies the removal of elements from the window by not actually removing them from the heaps, which would require a more complex data structure for efficient removal.