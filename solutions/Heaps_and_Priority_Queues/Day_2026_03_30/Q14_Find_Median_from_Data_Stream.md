# Find Median from Data Stream

## Problem Statement
The median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values, and the median is their average. For example, the median of `[1, 2, 3, 4]` is `(2 + 3) / 2 = 2.5`. Given a data stream as an array of integers `nums`, find the median of the data stream at each point. The data stream is an array of integers `nums` where `nums[i]` is the ith integer in the data stream. The median of the data stream after the ith integer is added is the median of the array `[nums[0], nums[1], ..., nums[i]]`. The size of the data stream is at most `10^5`, and the integers in the data stream are between `10^-4` and `10^4`.

## Approach
To solve this problem efficiently, we can use two heaps, a max heap and a min heap. The max heap stores the smaller half of the numbers, and the min heap stores the larger half. We maintain the property that the size of the max heap is either equal to the size of the min heap or one more than the size of the min heap.

## Complexity
- Time: O(n log n)
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
        // if the max heap is empty or the number is smaller than the top of the max heap, push it into the max heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            // otherwise, push it into the min heap
            minHeap.push(num);
        }
        // balance the heaps to maintain the property
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
        } else {
            // otherwise, return the average of the tops of the two heaps
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
Output: [1, 1.5, 2]
```

## Key Takeaways
- We use two heaps to store the smaller and larger halves of the numbers.
- We maintain the property that the size of the max heap is either equal to the size of the min heap or one more than the size of the min heap.
- The time complexity is O(n log n) due to the heap operations.