# Sliding Window Median

## Problem Statement
The Sliding Window Median problem is a classic problem that involves finding the median of a list of numbers within a sliding window of fixed size. Given an array of integers `nums` and an integer `k`, find the median of each subarray of size `k` and return a list of these medians. The median of a list of numbers is the middle value when the numbers are sorted in ascending order. If the list has an even number of elements, the median is the average of the two middle values.

## Approach
We can use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers and the min heap will store the larger half. We will maintain the balance between the two heaps such that the size of the max heap is either equal to the size of the min heap or one more than the size of the min heap.

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
        // add the number to the correct heap
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
            // remove the number that is out of the window
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
            // balance the heaps
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
- Use two heaps to maintain the balance between the smaller and larger halves of the numbers.
- The time complexity is O(n log k) due to the use of heaps.
- The space complexity is O(k) as we only need to store the numbers within the sliding window.