# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...](si < ei), determine if a person could attend all meetings. If the person can attend all meetings, return 0, otherwise return the minimum number of rooms required. The meeting intervals are non-overlapping when [s1, e1] and [s2, e2] do not overlap if s1 >= e2 or s2 >= e1. For example, if we have intervals [[0,30],[5,10],[15,20]], we need 2 rooms because [0,30] and [5,10] overlap and [15,20] overlaps with [5,10] and [0,30]. 

## Approach
We can solve this problem using a priority queue to store the end times of the meetings. The idea is to always try to assign a meeting to an existing room before assigning it to a new room. We sort the meetings by their start times and iterate over them, assigning each meeting to the room that becomes available the earliest.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    
    // Sort the intervals by start time
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    // Priority queue to store the end times of the meetings
    priority_queue<int, vector<int>, greater<int>> endTimes;
    
    // Initialize the priority queue with the end time of the first meeting
    endTimes.push(intervals[0][1]);
    
    // Iterate over the rest of the meetings
    for (int i = 1; i < intervals.size(); i++) {
        // If the current meeting starts after the earliest end time, update the earliest end time
        if (intervals[i][0] >= endTimes.top()) {
            endTimes.pop();
        }
        // Add the end time of the current meeting to the priority queue
        endTimes.push(intervals[i][1]);
    }
    
    // The size of the priority queue is the minimum number of rooms required
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
- Use a priority queue to store the end times of the meetings to efficiently find the earliest available room.
- Sort the meetings by their start times to ensure that we consider the meetings in the correct order.
- The size of the priority queue at the end of the algorithm is the minimum number of rooms required.