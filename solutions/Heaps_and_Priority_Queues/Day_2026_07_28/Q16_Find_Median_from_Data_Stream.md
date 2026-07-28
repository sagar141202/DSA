# Find Median from Data Stream

## Problem Statement
The median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values, and the median is their average. For example, the median of the list [1, 2, 3, 4] is (2 + 3) / 2 = 2.5. You are given a data stream, and you need to find the median of the stream at any given time. The data stream is a sequence of integers, and you can receive the integers one by one. After receiving each integer, you need to calculate the median of the integers received so far.

## Approach
To solve this problem, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain the balance between the two heaps to ensure that the max heap always has one more element than the min heap if the total number of elements is odd. The median is then the top element of the max heap if the total number of elements is odd, or the average of the top elements of the two heaps if the total number of elements is even.

## Complexity
- Time: O(log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max heap to store the smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min heap to store the larger half

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
    cout << mf.findMedian() << endl; // output: 1.5
    mf.addNum(3);
    cout << mf.findMedian() << endl; // output: 2
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: [1.0, 1.5, 2.0]
```

## Key Takeaways
- Use two heaps to maintain the balance between the smaller and larger halves of the numbers.
- The max heap should always have one more element than the min heap if the total number of elements is odd.
- The median is the top element of the max heap if the total number of elements is odd, or the average of the top elements of the two heaps if the total number of elements is even.