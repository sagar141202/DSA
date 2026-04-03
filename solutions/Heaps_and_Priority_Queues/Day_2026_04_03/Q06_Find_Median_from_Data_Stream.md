# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, which is a sequence of numbers that are received one by one. The median is the middle value in the sorted sequence. If the sequence has an even number of elements, the median is the average of the two middle values. The solution should be able to handle a large number of elements and should be efficient in terms of time and space complexity. For example, if the input stream is [1, 2, 3, 4, 5], the median should be 3, and if the input stream is [1, 2, 3, 4], the median should be (2 + 3) / 2 = 2.5.

## Approach
The algorithm uses two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap is used to store the smaller half of the numbers, and the min heap is used to store the larger half. The max heap is always one element larger than the min heap if the total number of elements is odd.

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
Input: [1, 2, 3, 4, 5]
Output: 3
Input: [1, 2, 3, 4]
Output: 2.5
```

## Key Takeaways
- Use two heaps to store the smaller and larger halves of the numbers.
- Balance the heaps to ensure the max heap is always one element larger than the min heap if the total number of elements is odd.
- Calculate the median based on the sizes of the heaps.