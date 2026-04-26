# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. If not, find the minimum number of rooms required to hold all meetings. Each meeting is represented as an interval [start, end), and the intervals are not necessarily disjoint. The input array is not sorted, and the start and end times are non-negative integers. For example, if the input is [[0,30],[5,10],[15,20]], the minimum number of rooms required is 2 because the meeting [5,10] overlaps with [0,30], and [15,20] also overlaps with [0,30] but not with [5,10].

## Approach
We use a priority queue to keep track of the end times of the meetings. We sort the meetings by their start times and then iterate through them, adding each meeting to the priority queue. If the earliest end time in the queue is earlier than the current meeting's start time, we remove it from the queue. The size of the queue at any point represents the minimum number of rooms required so far.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    
    // Sort the meetings by start time
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    // Initialize a priority queue to store the end times
    priority_queue<int, vector<int>, greater<int>> endTimes;
    
    // Add the first meeting to the queue
    endTimes.push(intervals[0][1]);
    
    // Iterate through the rest of the meetings
    for (int i = 1; i < intervals.size(); i++) {
        // If the earliest end time is earlier than the current meeting's start time, remove it
        if (endTimes.top() <= intervals[i][0]) {
            endTimes.pop();
        }
        
        // Add the current meeting to the queue
        endTimes.push(intervals[i][1]);
    }
    
    // The size of the queue represents the minimum number of rooms required
    return endTimes.size();
}
```

## Test Cases
```
Input: [[0,30],[5,10],[15,20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
```

## Key Takeaways
- Sort the meetings by start time to ensure we process them in the correct order.
- Use a priority queue to efficiently keep track of the end times and find the earliest end time.
- The size of the priority queue represents the minimum number of rooms required at any point.