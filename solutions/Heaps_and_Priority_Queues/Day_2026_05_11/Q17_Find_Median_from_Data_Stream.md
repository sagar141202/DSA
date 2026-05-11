# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, which is a sequence of numbers that are received one by one. The median is the middle value in the sorted sequence. If the sequence has an even number of elements, the median is the average of the two middle values. The solution should be able to handle a large number of elements and provide an efficient way to calculate the median after each insertion.

## Approach
We can use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. We will maintain the property that the size of the max heap is either equal to the size of the min heap or one more.

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
        // if max heap is empty or num is smaller than the top of max heap, push it to max heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            // otherwise, push it to min heap
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
        // if the total number of elements is odd, return the top of max heap
        if (maxHeap.size() > minHeap.size()) {
            return (double)maxHeap.top();
        } else {
            // if the total number of elements is even, return the average of the tops of max heap and min heap
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
- Using two heaps (max heap and min heap) to store the smaller and larger halves of the numbers allows for efficient calculation of the median.
- Maintaining the property that the size of the max heap is either equal to the size of the min heap or one more ensures that the median can be calculated correctly.
- The time complexity of the solution is O(log n) due to the use of heaps, and the space complexity is O(n) as we need to store all the numbers in the heaps.