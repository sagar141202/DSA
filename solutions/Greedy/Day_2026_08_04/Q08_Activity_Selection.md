# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of integers, where the first integer represents the start time and the second integer represents the finish time. The goal is to find the maximum number of non-conflicting activities that can be selected.

## Approach
The algorithm sorts the activities based on their finish times and then iterates through the sorted list, selecting the activities that do not conflict with the previously selected activity. This approach ensures that the maximum number of non-conflicting activities are selected. The key insight is to always select the activity with the earliest finish time.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Comparison function to sort activities based on finish time
bool compareActivities(const Activity& a, const Activity& b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of non-conflicting activities
int activitySelection(vector<Activity>& activities) {
    // Sort the activities based on finish time
    sort(activities.begin(), activities.end(), compareActivities);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the finish time of the last selected activity
    int lastFinish = activities[0].finish;

    // Iterate through the sorted list of activities
    for (int i = 1; i < activities.size(); i++) {
        // Check if the current activity does not conflict with the last selected activity
        if (activities[i].start >= lastFinish) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinish = activities[i].finish;
        }
    }

    // Return the maximum number of non-conflicting activities
    return count;
}

int main() {
    // Example usage
    vector<Activity> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int maxActivities = activitySelection(activities);
    cout << "Maximum number of non-conflicting activities: " << maxActivities << endl;
    return 0;
}
```

## Test Cases
```
Input: [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
Output: 4
```

## Key Takeaways
- The greedy approach can be used to solve the activity selection problem by sorting the activities based on their finish times and selecting the activities that do not conflict with the previously selected activity.
- The time complexity of the algorithm is O(n log n) due to the sorting step, where n is the number of activities.
- The space complexity of the algorithm is O(n) for storing the activities.