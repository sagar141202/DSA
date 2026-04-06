# Find Median from Data Stream

## Problem Statement
Median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values, and the median is their average. For example, for the list [1, 2, 3, 4], the median is (2 + 3) / 2 = 2.5. Given a data stream, find the median of the stream at any point in time. The stream is a sequence of integers and can be positive, negative, or zero. The input is a sequence of integers, and the output is the median at each point in time.

## Approach
We can use two heaps to solve this problem: a max-heap to store the smaller half of the numbers and a min-heap to store the larger half. The max-heap will store the smaller half of the numbers, and the min-heap will store the larger half. We will balance the heaps to ensure the size difference between them is at most one.

## Complexity
- Time: O(log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    // max-heap to store the smaller half of the numbers
    priority_queue<int> maxHeap;
    // min-heap to store the larger half of the numbers
    priority_queue<int, vector<int>, greater<int>> minHeap;

    MedianFinder() {}

    void addNum(int num) {
        // Add the number to the correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // Balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // Calculate the median
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
Output: [1.0, 1.5, 2.0]
```

## Key Takeaways
- Use two heaps to store the smaller and larger halves of the numbers.
- Balance the heaps to ensure the size difference between them is at most one.
- Calculate the median based on the sizes of the heaps.