# Find Median from Data Stream

## Problem Statement
Median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values and the median is their average. For example, for `arr = [1, 2, 3, 4]`, the median is `(2 + 3) / 2 = 2.5` and for `arr = [1, 2, 3, 4, 5]`, the median is `3`. Implement a data structure to find the median of a data stream. It supports the following operations: `addNum(int num)` - adds the integer `num` from the data stream to the data structure and `findMedian()` - returns the median of the current data stream.

## Approach
To efficiently find the median from a data stream, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain the property that the max heap always has one more element than the min heap if the total number of elements is odd.

## Complexity
- Time: O(log n) for both addNum and findMedian operations
- Space: O(n) for storing the elements in the heaps

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
Input: 
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output: 
[null, null, null, 1.5, null, 2.0]
```

## Key Takeaways
- Using two heaps allows for efficient maintenance of the median in a data stream.
- The max heap stores the smaller half of the numbers and the min heap stores the larger half.
- Balancing the heaps after each insertion ensures that the median can be found in O(1) time.