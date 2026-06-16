# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a stream of numbers in real-time. The stream can be thought of as a sequence of numbers that are added one by one, and after each addition, the median of the current sequence needs to be calculated. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle numbers. For example, given the stream of numbers [1, 2, 3, 4, 5], the medians after each addition would be 1, 1.5, 2, 2.5, 3, respectively.

## Approach
To solve this problem efficiently, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain the property that the max heap always contains one more element than the min heap if the total number of elements is odd.

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
Input: [1, 2, 3, 4, 5]
Output: [1, 1.5, 2, 2.5, 3]
```

## Key Takeaways
- We use two heaps to maintain the smaller and larger halves of the numbers.
- The max heap stores the smaller half, and the min heap stores the larger half.
- We balance the heaps after each addition to ensure the max heap always contains one more element than the min heap if the total number of elements is odd.