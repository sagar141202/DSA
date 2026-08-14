# Sliding Window Median

## Problem Statement
The problem requires finding the median of all numbers in a sliding window of size k, where the window moves over an array of integers. The array is of size n, and the window size k is given. The task is to find the median of the numbers in the window at each position. For example, given the array [1, 3, -1, -3, 5, 3, 6, 7] and k = 3, the medians at each position are [1, -1, -1, 3, 5, 6].

## Approach
The algorithm uses two priority queues, a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap stores the k/2 smaller numbers, and the min heap stores the k/2 larger numbers. The median is then the top element of the max heap if k is odd, or the average of the top elements of the max and min heaps if k is even.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // stores the smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // stores the larger half

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
        // return the median
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
                // remove the number that is out of the window
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
};

int main() {
    Solution solution;
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> medians = solution.medianSlidingWindow(nums, k);
    for (double median : medians) {
        cout << median << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1, -1, -1, 3, 5, 6]
```

## Key Takeaways
- The time complexity is O(n log k) because we are using priority queues to store the numbers in the window.
- The space complexity is O(k) because we are storing at most k numbers in the priority queues.
- The solution uses two priority queues to store the smaller and larger halves of the numbers in the window, and it balances the heaps to ensure that the median is always the top element of the max heap or the average of the top elements of the max and min heaps.