//
// Created by amahi on 9/22/2022.
//

#include "bits/stdc++.h"

#define arrayLength(array) (sizeof(array)/sizeof(array[0]))

using namespace std;

void heapify(int arr[], int n, int i) {
/*
 * the idea here is making the node max or min heap
 * this method built to make a max heap.
 */
	int l = 2 * i + 1; // left node
	int r = 2 * i + 2; //  right node
	int max = i;
	if (l < n && arr[l] > arr[max]) { // to make the method min heap change arr[l] > to arr[l]<
		max = l;
	}
	if (r < n && arr[r] > arr[max]) { // to make the method min heap change arr[l] > to arr[l]<
		max = r;
	}
	if (max != i) {
		swap(arr[i], arr[max]);
		heapify(arr, n, max);
	}
}

inline void buildHeap(int arr[], int n) { // n = arr.length
	for (int i = n / 2 - 1; i >= 0; i--) {
		heapify(arr, n, i);
	}
}

inline void heapSort(int arr[], int n) {
	buildHeap(arr, n);
	for (int i = n - 1; i >= 0; i--) {
		swap(arr[0], arr[i]);
		heapify(arr, i, 0);
	}
}

inline void print(int arr[],int n) {
	for (int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
}

int main() {
	int arr[] = {5, 4, 3, 2, 1};
	heapSort(arr, 5);
	print(arr, arrayLength(arr));

	return 0;
}