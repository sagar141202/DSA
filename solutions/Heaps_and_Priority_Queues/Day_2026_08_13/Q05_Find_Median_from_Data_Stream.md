# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream. The data stream is a sequence of numbers that are received one by one, and after each number is received, the median of all the numbers received so far needs to be calculated. The median is the middle value in a sorted list of numbers. If the total number of values is odd, the median is the middle value. If the total number of values is even, the median is the average of the two middle values. The data stream can contain duplicate numbers and negative numbers.

## Approach
To solve this problem, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half of the numbers. We maintain the property that the max heap always contains one more element than the min heap if the total number of elements is odd.

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
Output: [1.0, 1.5, 2.0]
```

## Key Takeaways
- Use two heaps to store the smaller and larger half of the numbers.
- Maintain the property that the max heap always contains one more element than the min heap if the total number of elements is odd.
- Balance the heaps after each insertion to ensure the property is maintained.