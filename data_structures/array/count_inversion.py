class Solution:
    def merge(self, arr, low, mid, high):
        """
        sorts the array in descending order
        change left_half[i] <= right_half[j] to left_half[i] >= right_half[j] for sorting in descending order
        """
        left = low  # starting index of left half
        right = mid + 1  # starting index of right half
        temp = []
        inversion_count = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
                inversion_count += (mid - left + 1)

        # copy the remaining elements of left, if there are any
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # copy the remaining elements of right, if there are any
        while right <= high:
            temp.append(arr[right])
            right += 1

        # transferring elements from temp to array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return inversion_count

    def merge_sort(self, arr, low, high):
        """
        :param arr: array of numbers
        :param left_index:left index
        :param right_index:right index
        """
        count = 0
        if low >= high:
            return count

        mid = (low + high) // 2

        # sort first and second halves
        count += self.merge_sort(arr, low, mid)
        count += self.merge_sort(arr, mid + 1, high)
        count += self.merge(arr, low, mid, high)

        return count

    def getInversions(self, arr, n):
        count = self.merge_sort(arr, 0, n - 1)

        return count


s = Solution()
input_1 = [2, 5, 1, 3, 4]
print("output:", s.getInversions(input_1, 5))
