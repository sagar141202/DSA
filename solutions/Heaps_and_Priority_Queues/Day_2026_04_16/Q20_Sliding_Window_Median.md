# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size k, where the window moves one step at a time over a given array of integers. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. For example, given the array [1, 3, -1, -3, 5, 3, 6, 7] and k = 3, the medians for each window are [1, -1, -1, 3, 5, 6].

## Approach
We can use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain the balance between the two heaps to ensure the max heap size is either equal to the min heap size or one more. This allows us to efficiently calculate the median for each window.

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
                // Remove from max heap
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
                // Remove from min heap
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
            // Rebalance the heaps
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
- We use two heaps to efficiently calculate the median of a sliding window.
- The max heap stores the smaller half of the numbers and the min heap stores the larger half.
- We maintain the balance between the two heaps to ensure the max heap size is either equal to the min heap size or one more.