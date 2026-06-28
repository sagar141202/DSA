# Find Median from Data Stream

## Problem Statement
The problem requires finding the median of a data stream as the numbers are added to it. The data stream is a sequence of numbers that are added one by one, and after each addition, the median of the current sequence needs to be calculated. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle numbers. For example, given the sequence [1, 2, 3, 4], the median is (2 + 3) / 2 = 2.5.

## Approach
To solve this problem efficiently, we can use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap will store the smaller half of the numbers, and the min heap will store the larger half. We ensure that the size difference between the two heaps is at most 1.

## Complexity
- Time: O(log n)
- Space: O(n)

## C++ Solution
```cpp
#include <queue>
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
        // calculate the median based on the sizes of the heaps
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double) maxHeap.top();
        }
    }
};

int main() {
    MedianFinder mf;
    mf.addNum(1);
    mf.addNum(2);
    printf("%f\n", mf.findMedian());  // Output: 1.500000
    mf.addNum(3);
    printf("%f\n", mf.findMedian());  // Output: 2.000000
    return 0;
}
```

## Test Cases
```
Input: 
addNum(1)
addNum(2)
findMedian()
addNum(3)
findMedian()
Output: 
1.5
2.0
```

## Key Takeaways
- Using two heaps (max heap and min heap) allows for efficient calculation of the median as numbers are added to the data stream.
- Balancing the heaps ensures that the size difference between them is at most 1, which is crucial for calculating the median correctly.
- The time complexity of O(log n) is achieved due to the use of heaps for storing and retrieving numbers.