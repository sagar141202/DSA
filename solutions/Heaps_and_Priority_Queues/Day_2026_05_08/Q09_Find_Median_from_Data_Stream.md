# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, which is a sequence of numbers that are received one by one. The median is the middle value in the sorted sequence. If the sequence has an even number of elements, the median is the average of the two middle values. The data stream can contain duplicate numbers and the numbers can be positive, negative, or zero. The solution should be able to handle a large number of elements in the data stream.

## Approach
To find the median from a data stream, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. We will balance the heaps to ensure that the max heap always has one more element than the min heap if the total number of elements is odd.

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
        // if max heap is empty or num is smaller than the top of max heap, push num into max heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            // otherwise, push num into min heap
            minHeap.push(num);
        }

        // balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            // if max heap has more than one more element than min heap, pop the top of max heap and push it into min heap
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            // if min heap has more elements than max heap, pop the top of min heap and push it into max heap
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // if the total number of elements is odd, the median is the top of the max heap
        if (maxHeap.size() > minHeap.size()) {
            return (double)maxHeap.top();
        } else {
            // if the total number of elements is even, the median is the average of the tops of the max heap and the min heap
            return (maxHeap.top() + minHeap.top()) / 2.0;
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
Output: [1.0, 1.5, 2.0]
Input: [1, -1]
Output: [1.0, 0.0]
```

## Key Takeaways
- Use two heaps to store the smaller and larger halves of the numbers to efficiently find the median.
- Balance the heaps to ensure that the max heap always has one more element than the min heap if the total number of elements is odd.
- The time complexity of adding a number and finding the median is O(log n), where n is the number of elements in the data stream.