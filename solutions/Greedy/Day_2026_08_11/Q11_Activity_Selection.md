# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers, where the first integer is the start time and the second integer is the finish time. For example, if we have two activities (1, 4) and (3, 5), we cannot select both activities because they overlap. The goal is to find the maximum number of non-overlapping activities that can be selected.

## Approach
The algorithm sorts the activities based on their finish times and then iterates through the sorted activities, selecting the activities that do not overlap with the previously selected activity. This approach ensures that we select the maximum number of non-overlapping activities. The greedy choice is to always select the activity with the earliest finish time.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a struct to represent an activity
struct Activity {
    int start;
    int finish;
};

// Comparison function to sort activities based on finish time
bool compareActivities(const Activity& a, const Activity& b) {
    return a.finish < b.finish;
}

int activitySelection(vector<Activity>& activities) {
    // Sort the activities based on their finish times
    sort(activities.begin(), activities.end(), compareActivities);
    
    // Initialize the count of selected activities to 1 (the first activity)
    int count = 1;
    
    // Initialize the finish time of the last selected activity
    int lastFinishTime = activities[0].finish;
    
    // Iterate through the sorted activities
    for (int i = 1; i < activities.size(); i++) {
        // If the current activity does not overlap with the last selected activity, select it
        if (activities[i].start >= lastFinishTime) {
            count++;
            lastFinishTime = activities[i].finish;
        }
    }
    
    return count;
}

int main() {
    int n;
    cout << "Enter the number of activities: ";
    cin >> n;
    
    vector<Activity> activities(n);
    cout << "Enter the start and finish times of the activities:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> activities[i].start >> activities[i].finish;
    }
    
    int maxActivities = activitySelection(activities);
    cout << "Maximum number of activities that can be selected: " << maxActivities << endl;
    
    return 0;
}
```

## Test Cases
```
Input: 
Enter the number of activities: 6
Enter the start and finish times of the activities:
1 2
3 4
0 6
5 7
8 9
5 9
Output: 
Maximum number of activities that can be selected: 4
```

## Key Takeaways
- The greedy approach is used to solve the activity selection problem by selecting the activity with the earliest finish time.
- The activities are sorted based on their finish times to ensure that we select the maximum number of non-overlapping activities.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the activities.