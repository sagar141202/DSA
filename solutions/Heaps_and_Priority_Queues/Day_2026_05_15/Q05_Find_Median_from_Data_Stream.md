# Find Median from Data Stream

## Problem Statement
Median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values and the median is their average. For example, for arr = [1, 2, 3, 4], the median is (2 + 3) / 2 = 2.5. You are given a data stream and you need to find the median of the data stream at any point in time. The data stream is a sequence of integers and the median is calculated after each integer is added to the stream.

## Approach
We will use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers and the min heap will store the larger half. We will balance the heaps to ensure the size difference is at most 1.

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
        // add to the correct heap
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
        // if the total number of elements is odd, return the top of the max heap
        if (maxHeap.size() > minHeap.size()) {
            return (double)maxHeap.top();
        }
        // if the total number of elements is even, return the average of the tops of the two heaps
        return (maxHeap.top() + minHeap.top()) / 2.0;
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
- We use two heaps, a max heap and a min heap, to store the smaller and larger halves of the numbers respectively.
- We balance the heaps to ensure the size difference is at most 1.
- The median is calculated based on the sizes of the two heaps.