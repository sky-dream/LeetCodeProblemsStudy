def main():
    histogram = [2,1,5,6,2,3]  # expect is 10
    Solution_obj = Solution()
    result = Solution_obj.largestRectangleArea(histogram)
    print("result value is ",result)
    
if __name__ =='__main__':
    main() 