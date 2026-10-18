Merge Sort: Divide and Sort

https://www.youtube.com/watch?v=ogjf7ORKfd8&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=8&pp=iAQB
---




Quick Sort: Divide and Conquer (slightly better than merge sort because it doesn't use a temporary array)

https://www.youtube.com/watch?v=WIrA4YexLRQ&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=9
```
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int get_partition(vector<int>& v, int low, int high) {
	int pivot = low;
	int i = low, j = high;
	
	while (i < j) {
		while (v[i] <= v[pivot] && i <= high) i++;
		while (v[j] > v[pivot] && j >= low) j--;
		if (i < j) swap(v[i], v[j]);
	}
	
	swap(v[pivot], v[j]);
	return j;
}

void qs(vector<int>& v, int low, int high) {
	if (low >= high) return;
	
	int partition = get_partition(v, low, high);
	qs(v, 0, partition-1);
	qs(v, partition+1, high);
	
}

int main() {
	vector<int> v = {5, 2, 7, 5, 3, 2, 3, 4, 7, 9, 4, 3};
	qs(v, 0, v.size() - 1);
	for (const auto& i: v) {
		cout << i << ' ';
	}
}
```
