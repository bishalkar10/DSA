"""
Formula : factorial (n) // factorial (r) * factorial (n-r)
So n has to be greater than r each time or 
n-r <=  0 will not work 

Link : https://practice.geeksforgeeks.org/problems/ncr1019/1?page=3&sortBy=submissions
"""

def nCr(self, n, r):

        if n<r:
            return 0
        # a helper function for calculating factorial 
        def fact(n):
            if n==0 or n==1:
                return 1 
            return n*fact(n-1)
        return (fact(n)//(fact(r)*fact(n-r)))%(10**9+7)