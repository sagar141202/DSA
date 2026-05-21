# Find Median from Data Stream

## Problem Statement
Given a stream of integers, find the median of the data stream at any given time. The median is the middle value in the sorted list of numbers. If the total number of elements is even, the median is the average of the two middle numbers. The data stream can be very large, so we need to find an efficient solution that can handle a large number of elements.

## Approach
We can use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. We will maintain the property that the max heap will always have one more element than the min heap if the total number of elements is odd.

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
        if (maxHeap.size() > minHeap.size()) {
            return (double)maxHeap.top();
        } else {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        }
    }
};

int main() {
    MedianFinder mf;
    mf.addNum(1);
    mf.addNum(2);
    cout << mf.findMedian() << endl;  // Output: 1.5
    mf.addNum(3);
    cout << mf.findMedian() << endl;  // Output: 2
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: [1.0, 1.5, 2.0]
```

## Key Takeaways
- We use two heaps to maintain the smaller and larger halves of the numbers.
- We balance the heaps after each insertion to ensure the max heap has at most one more element than the min heap.
- The time complexity of the solution is O(log n) due to the heap operations.