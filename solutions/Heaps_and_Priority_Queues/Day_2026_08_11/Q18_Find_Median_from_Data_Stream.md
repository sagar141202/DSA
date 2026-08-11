# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream as the numbers are being added to it. The data stream is a sequence of numbers that are being added one by one, and after each addition, the median of the current sequence needs to be calculated. The median is the middle value in the sorted sequence. If the sequence has an even length, the median is the average of the two middle values. The solution should be able to handle a large number of additions and calculate the median efficiently.

## Approach
To solve this problem, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain the property that the max heap always has one more element than the min heap if the total number of elements is odd. This way, the median can be calculated as the top element of the max heap if the total number of elements is odd, or the average of the top elements of the two heaps if the total number of elements is even.

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
Input: [1, 3, 5]
Output: [1, 3, 3.5]
```

## Key Takeaways
- Use two heaps to maintain the smaller and larger halves of the numbers.
- Balance the heaps after each addition to ensure the max heap has at most one more element than the min heap.
- Calculate the median based on the top elements of the two heaps.