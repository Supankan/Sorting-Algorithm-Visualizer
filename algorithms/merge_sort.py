# algorithms/merge_sort.py
def merge_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i, j, k = 0, 0, left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            yield arr

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            yield arr

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            yield arr

    if left < right:
        mid = (left + right) // 2
        yield from merge_sort(arr, left, mid)
        yield from merge_sort(arr, mid + 1, right)
        yield from merge(arr, left, mid, right)
