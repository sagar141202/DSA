# Simplify Path

## Problem Statement
Given an absolute path in a file system, simplify it by resolving '..' and '.' in the path. The path is guaranteed to start with a '/' and may end with a '/'. Also, the path only contains letters, digits, and the special characters '.', and '/'. The function should return the simplified path. For example, "/home/" should return "/home", "/../" should return "/", and "/home//foo/" should return "/home/foo".

## Approach
The algorithm uses a stack to store the directories in the path. It iterates over each directory in the path, and if the directory is '..', it pops the last directory from the stack if it is not empty. If the directory is not '.' or '', it pushes the directory to the stack. Finally, it constructs the simplified path from the directories in the stack.

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
        stack<string> st;
        string dir = "";
        for (char c : path) {
            if (c == '/') {
                if (dir == "..") {
                    if (!st.empty()) st.pop();
                } else if (dir != "" && dir != ".") {
                    st.push(dir);
                }
                dir = "";
            } else {
                dir += c;
            }
        }
        if (dir == "..") {
            if (!st.empty()) st.pop();
        } else if (dir != "" && dir != ".") {
            st.push(dir);
        }
        string res = "";
        while (!st.empty()) {
            res = "/" + st.top() + res;
            st.pop();
        }
        if (res == "") return "/";
        return res;
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
- Handle '..' and '.' separately to correctly simplify the path.
- Construct the simplified path from the directories in the stack.