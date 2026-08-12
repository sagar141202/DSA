# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...](si < ei), determine if a person could attend all meetings. If the person can attend all meetings, return 0. If the person cannot attend all meetings, return the minimum number of rooms required to hold all meetings. Assume that all meetings are non-overlapping when they are given, and the start time is always less than the end time. The constraint is that we have a large number of meetings, so the space complexity should be as small as possible.

## Approach
We will use a priority queue to keep track of the end times of the meetings. The idea is to always try to assign a meeting to an existing room before opening a new room. We will sort the meetings based on their start times and then iterate through them, assigning each meeting to a room and updating the end time of that room.

## Complexity
- Time: O(N log N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.size() == 0) return 0;
    
    // Sort the meetings based on their start times
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    // Initialize a priority queue to store the end times of the meetings
    priority_queue<int, vector<int>, greater<int>> endTimes;
    
    // Initialize the minimum number of rooms required
    int minRooms = 0;
    
    // Iterate through the meetings
    for (const auto& interval : intervals) {
        // If the meeting starts after the earliest end time, update the earliest end time
        if (!endTimes.empty() && interval[0] >= endTimes.top()) {
            endTimes.pop();
        }
        
        // Add the end time of the current meeting to the priority queue
        endTimes.push(interval[1]);
        
        // Update the minimum number of rooms required
        minRooms = max(minRooms, (int)endTimes.size());
    }
    
    return minRooms;
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
- We use a priority queue to efficiently keep track of the end times of the meetings.
- We sort the meetings based on their start times to ensure that we are always trying to assign a meeting to an existing room before opening a new room.
- The time complexity is O(N log N) due to the sorting, and the space complexity is O(N) due to the priority queue.