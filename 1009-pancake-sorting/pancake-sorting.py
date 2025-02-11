class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        maxim = max(arr)
        answer = []
        i = len(arr)
        while arr != sorted_arr:
            # if arr[0] == maxim:
            #     answer.append(indx+1)
            # print(i, answer, arr)
            maxim = max(arr[:i])
            indx = arr.index(maxim)
            arr[:indx+1] = arr[indx::-1]
            arr[:i] = arr[i-1::-1]
            answer.append(indx+1)
            answer.append(i)
            i -= 1
        return answer
