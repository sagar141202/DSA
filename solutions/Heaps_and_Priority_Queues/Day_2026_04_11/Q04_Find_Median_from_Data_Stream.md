# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream. The data stream is a sequence of numbers that are received one by one. The median is the middle value in the sorted sequence. If the sequence has an even number of elements, the median is the average of the two middle values. The solution should be able to handle a large number of numbers in the data stream. For example, given the numbers 1, 2, and 3, the median is 2. Given the numbers 1 and 2, the median is 1.5.

## Approach
We can use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. We will maintain the property that the max heap always has one more element than the min heap if the total number of elements is odd.

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
    MedianFinder medianFinder;
    medianFinder.addNum(1);
    medianFinder.addNum(2);
    cout << medianFinder.findMedian() << endl;  // Output: 1.5
    medianFinder.addNum(3);
    cout << medianFinder.findMedian() << endl;  // Output: 2
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
- Use two heaps to store the smaller and larger halves of the numbers.
- Maintain the property that the max heap always has one more element than the min heap if the total number of elements is odd.
- Balance the heaps after adding a new number to ensure the property is maintained.