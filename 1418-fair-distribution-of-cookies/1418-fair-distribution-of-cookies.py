class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0]*k
        curr_min = float("inf")
        def solver(indx, max_):
            nonlocal curr_min
            if indx == len(cookies):
                curr_min = min(curr_min, max_)
                return
            if max_ >= curr_min:
                return
            curr_cookie = cookies[indx]
            for j in range(k):
                child[j] += curr_cookie
                solver(indx+1, max(child[j], max_))
                child[j] -= curr_cookie
                if child[j] == 0:
                    break
        solver(0, 0)
        return curr_min