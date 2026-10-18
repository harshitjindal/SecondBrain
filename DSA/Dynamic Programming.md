
Steps:
1. Come up with recursive solution
2. Use memoization to optimize recursion and get a DP solution (called top-down approach)
3. Reverse the memoization approach to get bottom-up approach, called Tabulation. This removes recursive calls, and is done with iteration
4. Check for optimizations to the tabulation solution. Eg: if dp[i-1] is being used, see if entire DP array is required or just one element at a time.

Notes:
1. Space optimization of tabulation form will always reduce dimensionality by 1, ie: 1D DP will use a few variables, 2D DP problems will use 1D for space optimization, 3D DP will use 2D for space optimization.
2. DP on subsequences always boils down to the "take/not take" approach, and the representation is usually  like f(idx, target) ie: 2D DP.
3. Try to keep indices positive in the memoization solution, otherwise it can complicate problems when converting memoization to tabulation
4. Avoid negative indices for base cases, if completely unavoidable, see if going from 0 -> n -1 might be a better approach instead of n-1 -> 0
5. For memoization, it is recommended to go from n-1->0, if feasible.
6. For pattern of 'count ways', base case returns 0 or 1, and we return sum of all possibilities:
       base(return 0 or 1)
       return f(something) + f(something else)
7. For pattern of longest / shortest length, base case returns 0, and we return max or min of (1 + next recursive all):
       base(return 0)
       pick = 1 + f(i - 1)
       notpick = f(i - 1)
       return max(pick, notpick)
8. Whenever we have to provide maximum / minimum of something, try to assume the take scenario to be INT_MIN at the beginning (or -1e8) in case of finding maximum. Eg: 0/1 knapsack
9. For questions with 0 based indexing where base case indices are going into negative, first try to convert it into 1 based indexing using memoization and then convert to tabulation. This was chances of errors are reduced.
10. When converting to tabulation, pay attention to if (...) return (...) conditions, because in tabulation this will need to be handled appropriately.
11. DP on strings:
	1. LCS
	2. String Matching
	3. 