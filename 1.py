class Homework():
    def __init__(self):
        pass

    def get_most_common_substring(self,s):
        substring = {}
        max_value = 0
        for i in range(len(s)):
            count = 0
            sub_value  = s[i]
            while i+1 < len(s) and s[i] <= s[i+1]:
                count += 1
                i += 1
                sub_value += s[i]
            substring[count] = substring.get(count, sub_value)
            max_value = max(substring.keys())
        return s.count(substring[max_value])

    def _angle_k(self,x1,y1,x2,y2):
        return (y2-y1)/(x2-x1)

    def is_parallel(self, arr):
        if len(arr) > 8 or len(arr) < 8:
            return 'Shuld be exactly 8 values!'
        return 'YES' if self._angle_k(arr[0],arr[1],arr[2],arr[3]) == self._angle_k(arr[4], arr[5], arr[6], arr[7]) else 'NO'


    def get_object_properties_without_undersocre_in_name(self,obj): 
        for p in dir(obj):
            if not p.startswith('_'):
                print(p)
        return True

    def get_second_max(self,arr):
        try:
            return max(a for a in arr if a!=max(arr))
        except:
            return 'NO'


hw = Homework()

hw1 = hw.get_object_properties_without_undersocre_in_name(1)
print(hw1)

hw2_arr = [int(x) for x in input().split(',')]
hw2 = hw.get_second_max(hw2_arr)
print(hw2)

hw3_arr = [int(x) for x in input().split(',')]
hw3 = hw.is_parallel(hw3_arr)
print(hw3)

hw4 = hw.get_most_common_substring(input())
print(hw4)
