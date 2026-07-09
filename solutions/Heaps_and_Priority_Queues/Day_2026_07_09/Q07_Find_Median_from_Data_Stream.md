# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream as the numbers are being added to it. The data stream is a sequence of numbers that are added one by one, and after each addition, the median of the current sequence needs to be found. The median is the middle value in a sorted sequence. If the sequence has an even number of elements, the median is the average of the two middle values. The sequence can contain duplicate numbers, and the numbers can be positive, negative, or zero.

## Approach
To solve this problem efficiently, we will use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. This ensures that the median can be found in O(log n) time.

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

        // balance the heaps to ensure the size difference is at most 1
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
- Use two heaps to store the smaller and larger halves of the numbers to find the median in O(log n) time.
- Balance the heaps to ensure the size difference is at most 1.
- Handle the cases when the total number of elements is odd or even to find the median correctly.