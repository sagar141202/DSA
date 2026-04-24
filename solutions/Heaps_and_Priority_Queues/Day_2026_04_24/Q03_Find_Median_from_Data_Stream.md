# Find Median from Data Stream

## Problem Statement
The median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values, and the median is their average. For example, in the list [1, 2, 3, 4], the median is (2 + 3) / 2 = 2.5. Design a data structure that supports adding numbers to it and finding the median of the current data stream. The data stream is not sorted, and you don't know the size of the data stream in advance. The median of the data stream should be calculated after each addition of a number.

## Approach
We will use two priority queues (heaps) to solve this problem: a max heap to store the smaller half of the numbers and a min heap to store the larger half. This ensures that the max heap always contains the smaller half of the numbers and the min heap contains the larger half.

## Complexity
- Time: O(log n)
- Space: O(n)

## C++ Solution
```cpp
#include <queue>
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
```

## Test Cases
```
Input: MedianFinder mf; mf.addNum(1); mf.addNum(2); mf.findMedian(); mf.addNum(3); mf.findMedian();
Output: 1.5, 2
```

## Key Takeaways
- Use two priority queues (heaps) to efficiently calculate the median of a data stream.
- Balance the heaps after each addition to ensure the max heap always contains the smaller half of the numbers and the min heap contains the larger half.