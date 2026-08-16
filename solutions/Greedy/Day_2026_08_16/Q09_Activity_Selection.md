# Activity Selection

## Problem Statement
The activity selection problem is a classic problem in greedy algorithms. Given a set of activities, each with a start and finish time, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given in the form of pairs (start, finish), where start is the start time of the activity and finish is the finish time. The goal is to select the maximum number of activities such that no two activities overlap. For example, if we have the following activities: (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14), the maximum number of activities that can be selected is 4: (1, 4), (5, 7), (8, 11), (12, 14).

## Approach
The approach to solve this problem is to sort the activities based on their finish times and then select the activities greedily. We start by selecting the activity with the earliest finish time, and then we select the next activity that does not overlap with the previously selected activity. This approach ensures that we select the maximum number of activities.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Comparison function to sort activities based on finish times
bool compare(Activity a, Activity b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of activities
int selectActivities(Activity arr[], int n) {
    // Sort the activities based on finish times
    sort(arr, arr + n, compare);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the finish time of the last selected activity
    int lastFinish = arr[0].finish;

    // Iterate through the sorted activities
    for (int i = 1; i < n; i++) {
        // Check if the current activity does not overlap with the last selected activity
        if (arr[i].start >= lastFinish) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinish = arr[i].finish;
        }
    }

    // Return the count of selected activities
    return count;
}

int main() {
    // Example usage
    Activity arr[] = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int n = sizeof(arr) / sizeof(arr[0]);

    int count = selectActivities(arr, n);

    cout << "Maximum number of activities that can be selected: " << count << endl;

    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The activity selection problem can be solved using a greedy approach by sorting the activities based on their finish times.
- The time complexity of the solution is O(n log n) due to the sorting step.
- The space complexity of the solution is O(n) for storing the activities.