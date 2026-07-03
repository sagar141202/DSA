# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size k in a given array of integers. The array is not sorted, and the window moves one step at a time. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. The problem requires an efficient algorithm to compute the median for each window position. For example, given the array [1, 3, -1, -3, 5, 3, 6, 7] and k = 3, the medians for each window position are [1, -1, -1, 3, 5, 6].

## Approach
The algorithm utilizes two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. This approach ensures that the max heap always contains the smaller half of the numbers and the min heap contains the larger half, allowing for efficient computation of the median.

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
        // compute median
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
                // remove num out of window
                if (nums[i - k] <= mf.maxHeap.top()) {
                    // num is in max heap
                    if (nums[i - k] == mf.maxHeap.top()) {
                        mf.maxHeap.pop();
                    }
                } else {
                    // num is in min heap
                    if (nums[i - k] == mf.minHeap.top()) {
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
};
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1, -1, -1, 3, 5, 6]
```

## Key Takeaways
- Utilize two heaps to efficiently compute the median of a sliding window.
- Balance the heaps to ensure the max heap always contains the smaller half of the numbers.
- Remove numbers out of the window by checking which heap they belong to.