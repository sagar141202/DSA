# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, i.e., a sequence of numbers that are received one by one. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. The solution should support the following operations: 
- `void addNum(int num)`: adds a number to the data stream
- `double findMedian()`: returns the median of the current data stream
The input data stream will contain at most 10^5 numbers. The numbers in the data stream are in the range [0, 10^5].

## Approach
We use two priority queues (heaps) to solve this problem: a max-heap to store the smaller half of the numbers and a min-heap to store the larger half. The max-heap will store the smaller half of the numbers, and the min-heap will store the larger half. We ensure that the size of the max-heap is always greater than or equal to the size of the min-heap.

## Complexity
- Time: O(log n) for addNum and findMedian operations
- Space: O(n) for storing the numbers in the heaps

## C++ Solution
```cpp
#include <queue>
using namespace std;

class MedianFinder {
public:
    // max-heap to store the smaller half of the numbers
    priority_queue<int> maxHeap;
    // min-heap to store the larger half of the numbers
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
        // if the total number of elements is odd, return the top of the max-heap
        if (maxHeap.size() > minHeap.size()) {
            return (double)maxHeap.top();
        } 
        // if the total number of elements is even, return the average of the tops of the two heaps
        else {
            return (maxHeap.top() + minHeap.top()) / 2.0;
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
- We use two heaps to store the smaller and larger halves of the numbers, ensuring that the size of the max-heap is always greater than or equal to the size of the min-heap.
- The addNum operation takes O(log n) time, where n is the number of elements in the data stream.
- The findMedian operation takes O(1) time, as we only need to access the top elements of the two heaps.