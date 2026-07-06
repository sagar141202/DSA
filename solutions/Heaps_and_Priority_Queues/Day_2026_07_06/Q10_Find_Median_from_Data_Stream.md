# Find Median from Data Stream

## Problem Statement
The median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values, and the median is their average. For example, for the list [1, 3], the median is (1 + 3) / 2 = 2, and for the list [1, 2], the median is (1 + 2) / 2 = 1.5. You are given a data stream as an array of integers, and you need to find the median of the data stream at each point. The data stream is an array of integers nums, and you can assume that the array will not be empty and will only contain integers.

## Approach
We can solve this problem using two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. We will maintain the property that the size of the max heap is either equal to the size of the min heap or one more.

## Complexity
- Time: O(log n) for each insertion
- Space: O(n) for storing the heaps

## C++ Solution
```cpp
#include <queue>
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
```

## Test Cases
```
Input: nums = [1, 2]
Output: [1, 1.5]
Input: nums = [1, 2, 3]
Output: [1, 1.5, 2]
```

## Key Takeaways
- Use two heaps to store the smaller and larger halves of the numbers
- Maintain the property that the size of the max heap is either equal to the size of the min heap or one more
- Balance the heaps after each insertion to ensure the property is maintained