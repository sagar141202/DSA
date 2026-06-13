# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, which is a sequence of numbers that are received one by one. The median is the middle value in the sorted list of numbers. If the total number of elements is odd, the median is the middle element. If the total number of elements is even, the median is the average of the two middle elements. The data stream can contain duplicate numbers and negative numbers.

## Approach
We can use two heaps to solve this problem: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. This way, the median can be easily calculated as the top element of the max heap (if the total number of elements is odd) or the average of the top elements of both heaps (if the total number of elements is even).

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
        // balance the heaps if necessary
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
Output: [1.5, 2]
Input: [1, 2]
Output: [1.5]
```

## Key Takeaways
- Use two heaps to balance the smaller and larger halves of the numbers.
- The max heap stores the smaller half of the numbers, and the min heap stores the larger half.
- The median can be calculated as the top element of the max heap (if the total number of elements is odd) or the average of the top elements of both heaps (if the total number of elements is even).