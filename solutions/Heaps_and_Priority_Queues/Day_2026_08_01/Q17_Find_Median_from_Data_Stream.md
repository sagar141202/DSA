# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, where the data stream is a sequence of numbers that are arriving one by one. The median is the middle value in the sorted data stream. If the data stream has an even number of elements, the median is the average of the two middle values. The data stream can contain duplicate numbers, and the numbers can be positive, negative, or zero. The solution should be able to handle a large number of numbers in the data stream.

## Approach
The approach is to use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. The max heap will be used to find the larger of the two middle values when the data stream has an odd number of elements.

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
        // find the median
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
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
Output: [1.5, 2]
Input: [1, 2]
Output: [1.5]
```

## Key Takeaways
- Use two heaps to store the smaller and larger half of the numbers.
- Balance the heaps to ensure the size difference is at most 1.
- Use the top elements of the heaps to find the median.