# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...](si < ei), determine if a person could attend all meetings. If the person can attend all meetings, return 0. Otherwise, return the minimum number of rooms required. The meeting intervals are non-overlapping and are given in the form of [start, end]. For example, given the intervals [[0,30],[5,10],[15,20]], the minimum number of rooms required is 2 because the meeting [5,10] and [15,20] can't be held at the same time.

## Approach
We will use a priority queue to store the end times of the meetings. The idea is to always try to assign a meeting to an existing room before allocating a new room. If a meeting starts after the earliest end time, we can reuse the room; otherwise, we need a new room.

## Complexity
- Time: O(N log N)
- Space: O(N)

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
    
    // Initialize a priority queue to store the end times
    priority_queue<int, vector<int>, greater<int>> endTimes;
    
    // Add the end time of the first meeting
    endTimes.push(intervals[0][1]);
    
    // Iterate over the rest of the meetings
    for (int i = 1; i < intervals.size(); i++) {
        // If the current meeting starts after the earliest end time, reuse the room
        if (intervals[i][0] >= endTimes.top()) {
            endTimes.pop();
        }
        // Add the end time of the current meeting
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
- Use a priority queue to efficiently manage the end times of the meetings.
- Always try to reuse an existing room before allocating a new one.
- The size of the priority queue represents the minimum number of rooms required.