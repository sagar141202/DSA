# Find Median from Data Stream

## Problem Statement
 Median from Data Stream: Design a class to find the kth largest element in a stream of numbers. The class should have the following methods: `addNum(int num)` which adds a new number to the stream, and `findMedian()` which returns the median of the current data stream. The median of a data stream can be either the average of the two middle numbers if the total number of elements is even, or the middle number if the total number of elements is odd. For example, given the numbers [1, 2], the median is (1 + 2) / 2 = 1.5, and given the numbers [1, 2, 3], the median is 2.

## Approach
To solve this problem efficiently, we use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers in descending order, and the min heap will store the larger half in ascending order. By maintaining a balance between the two heaps, we can find the median in O(1) time.

## Complexity
- Time: O(log n) for `addNum` and O(1) for `findMedian`
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    // max heap to store the smaller half of the numbers
    priority_queue<int> maxHeap;
    // min heap to store the larger half of the numbers
    priority_queue<int, vector<int>, greater<int>> minHeap;

    MedianFinder() {}

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
        // if the total number of elements is odd, return the top of the max heap
        if (maxHeap.size() > minHeap.size()) {
            return (double)maxHeap.top();
        }
        // if the total number of elements is even, return the average of the tops of the two heaps
        return (maxHeap.top() + minHeap.top()) / 2.0;
    }
};
```

## Test Cases
```
Input: MedianFinder mf; mf.addNum(1); mf.addNum(2); mf.findMedian();
Output: 1.5
Input: MedianFinder mf; mf.addNum(1); mf.addNum(2); mf.addNum(3); mf.findMedian();
Output: 2
```

## Key Takeaways
- Use two heaps to store the smaller and larger halves of the numbers to find the median efficiently.
- Balance the heaps to ensure the max heap always has one more element than the min heap when the total number of elements is odd.
- Use the `priority_queue` class in C++ to implement the max and min heaps.