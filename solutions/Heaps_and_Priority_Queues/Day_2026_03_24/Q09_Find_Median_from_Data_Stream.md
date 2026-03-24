# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, which is a continuous flow of numbers. The median is the middle value in a sorted list of numbers. If the total number of values is odd, the median is the middle value. If the total number of values is even, the median is the average of the two middle values. The data stream can contain both positive and negative numbers, and the numbers can be duplicates. The goal is to design a data structure that can efficiently calculate the median after each new number is added to the data stream.

## Approach
We can use two heaps to solve this problem: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. The max heap will be used to calculate the lower half of the median, and the min heap will be used to calculate the upper half of the median.

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
        // if the total number of values is odd, return the top of max heap
        if (maxHeap.size() > minHeap.size()) {
            return (double) maxHeap.top();
        } else {
            // if the total number of values is even, return the average of the tops of max heap and min heap
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
- Use two heaps to store the smaller and larger halves of the numbers.
- Balance the heaps to ensure the size difference is at most 1.
- Calculate the median based on the tops of the two heaps.