class Homework():
    def __init__(self):
        pass

    def get_most_common_substring(self,str):
        ss = ''
        for s in str:
            ss+=s
            substring = ''
            for i in range(int(len(str)/len(ss))):
                substring+=ss
            if str == substring and len(str) != len(ss):
                return len(ss)
        return 1

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

    def get_int_array_from_inupt(self):
        return [int(x) for x in input().split(',')]



hw = Homework()

hw1 = hw.get_object_properties_without_undersocre_in_name(1)
print(hw1)

hw2 = hw.get_second_max(hw.get_int_array_from_inupt())
print(hw2)

hw3 = hw.is_parallel(hw.get_int_array_from_inupt())
print(hw3)

hw4 = hw.get_most_common_substring(input())
print(hw4)
