# Find Median from Data Stream

## Problem Statement
The median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values, and the median is their average. For example, the median of the list [1, 2, 3, 4] is (2 + 3) / 2 = 2.5. You are given a data stream, and you need to find the median of the data stream at any given time. The data stream is a sequence of integers, and you can receive the integers one by one. You can assume that the number of integers in the data stream will not exceed 10^5.

## Approach
We can use two heaps to solve this problem: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. We will maintain the property that the size of the max heap is either equal to the size of the min heap or one more.

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
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[],[1],[2],[],[3],[]]
Output: [null,null,null,1.5,null,2.0]
```

## Key Takeaways
- Use two heaps to store the smaller and larger halves of the numbers.
- Maintain the property that the size of the max heap is either equal to the size of the min heap or one more.
- Balance the heaps after adding a number to ensure the property is maintained.