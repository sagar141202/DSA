# Find Median from Data Stream

## Problem Statement
The median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values, and the median is their average. Given a data stream of integers, design an algorithm to find the median of all integers in the stream. The algorithm should use constant space (excluding the space needed to store the input) and run in O(log n) time per operation, where n is the number of integers in the stream. For example, given the integers [1, 2], the median is 1.5. Given the integers [1, 2, 3, 4], the median is 2.5.

## Approach
We can use two heaps to solve this problem: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. We will balance the two heaps to ensure the size difference between them is at most 1.

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
        // balance the two heaps
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
- Balance the two heaps to ensure the size difference between them is at most 1.
- Calculate the median based on the sizes of the two heaps.