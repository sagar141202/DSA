# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size k, where the window moves one step at a time over the entire array. Given an array of integers `nums` and an integer `k`, return the median of each window of size `k` as the window slides over the array. The array `nums` has a length of `n`, where `n` is at least `k`, and `k` is at most `n`. The median of a window is defined as the middle number when the numbers in the window are sorted. If the window has an even number of elements, the median is the average of the two middle numbers.

## Approach
The algorithm uses two heaps, a max heap to store the smaller half of the window and a min heap to store the larger half. The max heap stores the smaller half of the window and the min heap stores the larger half. The median is then calculated based on the sizes and tops of the two heaps.

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
        // calculate median based on heap sizes and tops
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
            // remove num that just fell out of window
            if (nums[i - k] <= mf.maxHeap.top()) {
                // remove from max heap
                priority_queue<int> newMaxHeap;
                while (mf.maxHeap.top() != nums[i - k]) {
                    newMaxHeap.push(mf.maxHeap.top());
                    mf.maxHeap.pop();
                }
                mf.maxHeap.pop();
                while (!newMaxHeap.empty()) {
                    mf.maxHeap.push(newMaxHeap.top());
                    newMaxHeap.pop();
                }
            } else {
                // remove from min heap
                priority_queue<int, vector<int>, greater<int>> newMinHeap;
                while (mf.minHeap.top() != nums[i - k]) {
                    newMinHeap.push(mf.minHeap.top());
                    mf.minHeap.pop();
                }
                mf.minHeap.pop();
                while (!newMinHeap.empty()) {
                    mf.minHeap.push(newMinHeap.top());
                    newMinHeap.pop();
                }
            }
            // rebalance heaps if necessary
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

int main() {
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> medians = medianSlidingWindow(nums, k);
    for (double median : medians) {
        cout << median << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

## Key Takeaways
- Use two heaps to maintain the smaller and larger halves of the window.
- Balance the heaps to ensure the max heap size is at most one more than the min heap size.
- Calculate the median based on the sizes and tops of the two heaps.