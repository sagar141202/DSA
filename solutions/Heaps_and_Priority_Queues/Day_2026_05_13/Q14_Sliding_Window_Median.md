# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size k, where the window moves one step at a time over a given array of integers. The array can contain duplicate elements, and the window size k is a positive integer. For example, given the array [1, 3, -1, -3, 5, 3, 6, 7] and k = 3, the medians for each window position are [1, -1, -1, 3, 5, 6]. The goal is to write an efficient algorithm to calculate these medians.

## Approach
To solve this problem, we can utilize two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the k/2 smaller numbers, and the min heap will store the k/2 larger numbers. We maintain the balance between the two heaps to ensure the median can be easily calculated.

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
                // Remove from min heap
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
- Use two heaps to maintain the balance between the smaller and larger halves of the numbers.
- The time complexity is O(n log k) due to the heap operations.
- The space complexity is O(k) for storing the numbers in the heaps.