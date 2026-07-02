# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream, which is a sequence of numbers that are received one by one. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. For example, given the data stream [1, 2, 3, 4, 5], the median is 3. If the data stream is [1, 2, 3, 4], the median is (2 + 3) / 2 = 2.5. The solution should be able to handle a large number of inputs and find the median in real-time.

## Approach
To find the median from a data stream, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. This way, the max heap will always have one more element than the min heap if the total number of elements is odd.

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
        // if max heap is empty or num is smaller than the top of max heap, push it into max heap
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
        // if the total number of elements is odd, return the top of max heap
        if (maxHeap.size() > minHeap.size()) {
            return (double)maxHeap.top();
        }
        // if the total number of elements is even, return the mean of the tops of max heap and min heap
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
Input: [1, 2, 3, 4, 5]
Output: [1, 1.5, 2, 2.5, 3]
Input: [1, 2, 3, 4]
Output: [1, 1.5, 2, 2.5]
```

## Key Takeaways
- Use two heaps to store the smaller and larger halves of the numbers.
- Balance the heaps after each insertion to ensure the max heap has at most one more element than the min heap.
- The median can be found by looking at the tops of the two heaps.