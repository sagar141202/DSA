# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` within an array of integers. Given an array `nums` and an integer `k`, return the median of all numbers in the sliding window. The sliding window should move from left to right, and the median is calculated for each position of the window. For example, if `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the medians for each window position are `[1, 1, -1, -1, 3, 3]`. The constraints are `1 <= k <= nums.size()` and `nums.size()` will be between 1 and 10^5.

## Approach
To solve this problem, we can utilize two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain a balance between the two heaps to efficiently calculate the median. The max heap stores the smaller half of the numbers, and the min heap stores the larger half.

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
        // Add the number to the correct heap
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
        // Calculate the median
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
            // Remove the number that is out of the window
            if (nums[i - k] <= mf.maxHeap.top()) {
                // If the number is in the max heap, remove it
                priority_queue<int> temp;
                while (mf.maxHeap.top() != nums[i - k]) {
                    temp.push(mf.maxHeap.top());
                    mf.maxHeap.pop();
                }
                mf.maxHeap.pop();
                while (!temp.empty()) {
                    mf.maxHeap.push(temp.top());
                    temp.pop();
                }
            } else {
                // If the number is in the min heap, remove it
                priority_queue<int, vector<int>, greater<int>> temp;
                while (mf.minHeap.top() != nums[i - k]) {
                    temp.push(mf.minHeap.top());
                    mf.minHeap.pop();
                }
                mf.minHeap.pop();
                while (!temp.empty()) {
                    mf.minHeap.push(temp.top());
                    temp.pop();
                }
            }
            // Balance the heaps again
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
Output: [1, 1, -1, -1, 3, 3]
```

## Key Takeaways
- Use two heaps, a max heap and a min heap, to store the smaller and larger halves of the numbers in the sliding window.
- Balance the heaps to ensure the max heap size is either equal to the min heap size or one more than the min heap size.
- Calculate the median based on the sizes of the two heaps.