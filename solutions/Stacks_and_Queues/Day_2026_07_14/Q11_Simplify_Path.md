# Simplify Path

## Problem Statement
Given an absolute path to a file in a Unix-style file system, simplify the path by resolving the '.' and '..' directories. The '.' directory refers to the current directory, and the '..' directory refers to the parent directory. The path is guaranteed to start with a '/' and may end with a '/'. There will be no multiple consecutive '/' characters. For example, "/home/" and "/../" are not valid inputs, but "/home//foo/" is. The function should return the simplified path.

## Approach
The algorithm uses a stack to store the directories in the path. It iterates over each directory in the path, pushing the directory onto the stack if it's not '.' or '..'. If the directory is '..', it pops the last directory from the stack if it's not empty. The simplified path is then constructed by joining the directories in the stack with '/'.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        // Split the path into directories
        stringstream ss(path);
        string dir;
        vector<string> dirs;
        while (getline(ss, dir, '/')) {
            if (dir != "" && dir != ".") {
                dirs.push_back(dir);
            }
        }
        
        // Use a stack to store the directories
        stack<string> st;
        for (string dir : dirs) {
            if (dir == "..") {
                if (!st.empty()) {
                    st.pop();
                }
            } else {
                st.push(dir);
            }
        }
        
        // Construct the simplified path
        string simplifiedPath;
        while (!st.empty()) {
            simplifiedPath = "/" + st.top() + simplifiedPath;
            st.pop();
        }
        
        return simplifiedPath;
    }
};
```

## Test Cases
```
Input: "/home/"
Output: "/home"
Input: "/../"
Output: "/"
Input: "/home//foo/"
Output: "/home/foo"
```

## Key Takeaways
- Use a stack to store the directories in the path.
- Handle the '.' and '..' directories separately.
- Construct the simplified path by joining the directories in the stack with '/'.