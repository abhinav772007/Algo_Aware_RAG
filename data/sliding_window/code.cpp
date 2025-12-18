int maxSumSubarray(vector<int>& arr, int k) {
    int windowSum = 0, maxSum = 0;
    for (int i = 0; i < arr.size(); i++) {
        windowSum += arr[i];
        if (i >= k - 1) {
            maxSum = max(maxSum, windowSum);
            windowSum -= arr[i - k + 1];
        }
    }
    return maxSum;
}
