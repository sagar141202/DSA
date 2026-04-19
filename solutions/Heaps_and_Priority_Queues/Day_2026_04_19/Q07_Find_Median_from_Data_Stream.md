# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, which is a sequence of numbers that are received one by one. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. The data stream can contain duplicate numbers and the numbers are not guaranteed to be in any particular order. The solution should be able to handle a large number of numbers in the data stream.

## Approach
To solve this problem, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain the property that the max heap always has one more element than the min heap if the total number of elements is odd. This allows us to efficiently calculate the median at any point.

## Complexity
- Time: O(log n)
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

    void addNum(int num) {
        // add the number to the correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // balance the heaps if necessary
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
```

## Test Cases
```
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[],[1],[2],[],[3],[]]
Output: [null,null,null,1.5,null,2.0]
```

## Key Takeaways
- Use two heaps to maintain the smaller and larger halves of the numbers.
- Balance the heaps after adding each number to ensure the max heap has at most one more element than the min heap.
- Calculate the median based on the sizes of the heaps.