//
// Created by amahi on 9/22/2022.
//
#include "bits/stdc++.h"

#define arrayLength(array) (sizeof(array)/sizeof(array[0]))
using namespace std;


int binarySearch(int arr[], int low, int high, int num){
	if (high >= low){
		int mid = (high+low)/2;
		if(arr[mid] == num){
			return mid;
		}
		else if(arr[mid] < num){
			binarySearch(arr,mid+1,high,num);
		}
		else{
			binarySearch(arr,low,mid-1,num);
		}
	}else{
		return -1;
	}
}

int main() {
	int arr[] = {1,2,3,4,5,6,7,8,9,10};
	cout<<binarySearch(arr,0,10,10);
	return 0;
}

