# Find Median from Data Stream

## Problem Statement
Median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values and the median is their average. Given a data stream with integers, find the median from the data stream at any point. The data stream is a sequence of integers that are coming in one by one. The median should be calculated after each new integer is inserted into the data stream. The integers in the data stream are in the range [0, 10000] and the data stream will have at most 10000 integers.

## Approach
To solve this problem, we can use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half of the numbers. We maintain the property that the max heap always has one more element than the min heap if the total number of elements is odd.

## Complexity
- Time: O(log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
private:
    priority_queue<int> maxHeap; // max heap to store the smaller half of the numbers
    priority_queue<int, vector<int>, greater<int>> minHeap; // min heap to store the larger half of the numbers

public:
    MedianFinder() {}

    // add the integer to the data stream
    void addNum(int num) {
        // if max heap is empty or num is smaller than the top of max heap, push num into max heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // balance the two heaps to maintain the property
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    // return the median of the current data stream
    double findMedian() {
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
    cout << medianFinder.findMedian() << endl; // output: 1.5
    medianFinder.addNum(3);
    cout << medianFinder.findMedian() << endl; // output: 2
    return 0;
}
```

## Test Cases
```
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
Output: [null, null, null, 1.5, null, 2]
```

## Key Takeaways
- We use two heaps to maintain the median of the data stream.
- The max heap stores the smaller half of the numbers and the min heap stores the larger half of the numbers.
- We balance the two heaps after each insertion to maintain the property that the max heap always has one more element than the min heap if the total number of elements is odd.