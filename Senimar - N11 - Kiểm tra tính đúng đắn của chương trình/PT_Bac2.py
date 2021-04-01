#giai pt bac 2 ax2+bx+c=0
'''import math
def XuLy(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                return 'VSN'
            else:
                return 'VN'
        else:
            x=-c/b
            x='{0:g}'.format(round(x,2))
            return f'{x}'
    else:
        delta=b**2-4*a*c
        if delta<0:
            return 'VN'
        elif delta==0:
            kq=-b/(2*a)
            kq='{0:g}'.format(round(kq,2))
            return f'{kq}'
        else:
            x1=(-b-math.sqrt(delta))/(2*a)
            x2=(-b+math.sqrt(delta))/(2*a)
            x1='{0:g}'.format(round(x1,2))
            x2='{0:g}'.format(round(x2,2))
            return f'{x1} {x2}'
# Python code to demonstrate working of unittest 
import unittest 

# chương trình cần kiểm tra

#chương trình test
class TestStringMethods(unittest.TestCase):
   
    # Setting up for the test
    def setUp(self):
        pass
    
    # Cleaning up after the test
    def tearDown(self):
        pass

    def test_1(self): #Kiểm tra chạy bình thường
        self.assertEqual(XuLy(1,2,1),"-1")
    def test_2(self): #Kiểm tra chạy bình thường
        self.assertEqual(XuLy(1,2,3), "VN")
    def test_3(self):
        self.assertEqual(XuLy(1,-5,6),"2 3")
    def test_4(self):
        self.assertEqual(XuLy(0,1,2), ("-2"))  
    def test_5(self):
        self.assertEqual(XuLy(0,-2,5), "2.5")
    def test_6(self):
        self.assertEqual(XuLy(1,-4.251,4.312994), "1.67 2.58") #(x-1.673)(x-2.578)
    def test_7(self):
        self.assertEqual(XuLy(1,-5.678,7.356), "2 3.68")  #(x-2)(x-3.678)
    def test_8(self):
        self.assertEqual(XuLy(1,-6.867,10.5041), "2.3 4.57")  #(x-2.3)(x-4.567)
    def test_9(self): #Kiểm tra phương trình cơ bản
        self.assertEqual(XuLy(1,-5,6),"2 3")
    def test_10(self): #Kiểm tra phương trình có nghiệm là số thực
        self.assertEqual(XuLy(1,-8,-2), "-0.24 8.24")
    def test_11(self): #Kiểm tra phương trình có nghiệm kép
        self.assertEqual(XuLy(0,1,2), ("-2"))  
    def test_12(self): #Kiểm tra phương trình có hệ số a = 0
        self.assertEqual(XuLy(0,-2,5), "2.5")
    def test_13(self): #Kiểm tra phương trình có hệ số b = 0
        self.assertEqual(XuLy(5,0,5), "1")
    def test_14(self): #Kiểm tra phương trình vô nghiệm
        self.assertEqual(XuLy(2,4,15), "VN")
    def test_15(self): #Kiểm tra phương trình vô số nghiệm
        self.assertEqual(XuLy(0,0,0), "VSN")
# if _name_ == '_main_': 
#     unittest.main() 

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)'''

import math
def XuLy():
    a,b,c=map(int,input().split())
    if a==0:
        if b==0:
            if c==0:
                return 'VSN'
            else:
                return 'VN'
        else:
            x=-c/b
            x='{0:g}'.format(round(x,2))
            return f'{x}'
    else:
        delta=b**2-4*a*c
        if delta<0:
            return 'VN'
        elif delta==0:
            kq=-b/(2*a)
            kq='{0:g}'.format(round(kq,2))
            return f'{kq}'
        else:
            x1=(-b-math.sqrt(delta))/(2*a)
            x2=(-b+math.sqrt(delta))/(2*a)
            x1='{0:g}'.format(round(x1,2))
            x2='{0:g}'.format(round(x2,2))
            return f'{x1} {x2}'
print(XuLy())




   