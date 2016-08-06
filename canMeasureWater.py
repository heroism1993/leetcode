class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if(z>x+y):
            return False
        if(x==0 and y==0):
            if(z==0):
                return True
            else:
                return False
        if(x==0):
            if(z%y==0):
                return True
            else:
                return False
        if(y==0):
            if(z%x==0):
                return True
            else:
                return False
        gcd_x_y=self.gcd(x,y)
        if(z%gcd_x_y==0):
            return True
        return False

    def gcd(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if(x>y):
            return self.gcd(y,x)
        if(x==0):
            return 0
        if(y%x==0):
            return x
        return self.gcd(y%x,x)

if(__name__=="__main__"):
    solution=Solution()
    print solution.canMeasureWater(2,6,5)