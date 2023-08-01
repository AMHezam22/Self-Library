#include <bits/stdc++.h>
#include "iostream"

using namespace std;

int partition2(int arr[], int l, int h) {
	int p = arr[l]; //p for Pivot
	int i = l;
	int j = h;
	while (i < j) {
		do {
			++i;
		} while (arr[i] <= p);
		do {
			--j;
		} while (arr[j] > p);
		if (i < j) {
			swap(arr[i], arr[j]);
		}
	}
	swap(arr[l], arr[j]);
	return j;
}

int partition1(int arr[], int iBegin, int jEnd) {
	int i = iBegin;
	int j = jEnd;
	int p = i; // p for pivot
	while (true){
		while (arr[p] <= arr[j] && p != j){
			--j;
		}
		if (p == j){
			break;
		}
		else if(arr[p]>arr[j]){
			swap(arr[j],arr[p]);
			p = j;
		}
		while (arr[p] >= arr[i] && p != i){
			i++;
		}
		if (p ==i){
			break;
		}
		else if(arr[p] < arr[i]){
			swap(arr[i],arr[p]);
			p = i;
		}
	}
	return p;
}

void quickSort1(int arr[], int l,int h){
	if (l<h){
		int piv = partition2(arr,l,h);
		quickSort1(arr,l,piv);
		quickSort1(arr,piv+1,h);
	}
}
void quickSort2(int arr[], int l, int h) {
	if (l < h) {
		int piv = partition2(arr, l, h);
		quickSort2(arr, l, piv-1);
		quickSort2(arr, piv + 1, h);
	}
}

int main() {
	int arr[] = {5, 4, 3, 2, 1, 0,13};
	quickSort1(arr, 0, 7);
	for (const auto &item: arr) {
		cout << item << " ";
	}
	return 0;
}

