# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, which is a sequence of numbers that are received one by one. The median is the middle value in the sorted sequence. If the sequence has an even number of elements, the median is the average of the two middle values. The solution should be able to handle a large number of elements and provide an efficient way to calculate the median. For example, given the sequence [1, 2, 3, 4, 5], the median is 3, and given the sequence [1, 2, 3, 4], the median is (2 + 3) / 2 = 2.5.

## Approach
To solve this problem, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain the property that the max heap always has one more element than the min heap if the total number of elements is odd. This allows us to efficiently calculate the median.

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
Input: MedianFinder medianFinder = new MedianFinder();
       medianFinder.addNum(1);
       medianFinder.addNum(2);
       medianFinder.findMedian(); // return 1.5
       medianFinder.addNum(3);
       medianFinder.findMedian(); // return 2
Output: 1.5, 2
```

## Key Takeaways
- Using two heaps allows for efficient calculation of the median.
- Maintaining the property that the max heap always has one more element than the min heap if the total number of elements is odd is crucial.
- Balancing the heaps after each insertion ensures that the median can be calculated in O(1) time.