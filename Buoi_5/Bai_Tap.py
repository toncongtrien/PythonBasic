print("\n\tBài tập 01: Viết chương trình nhập xuất mảng 1 chiều (List )")
print("\ta. Tính tổng của mảng 1 chiều")
print("\tMảng gồm bao nhiêu giá trị?")
a = int(input("\tNhập giá trị của mảng: "))
def tong(a):
    arr = [] 
    result = 0 
    for s in range(a):
        o = input(f"\tNhập giá trị [{s}]: ")
        arr.append(int(o))
        result += arr[s]
    return result
print("\tTổng của mảng là: ", tong(a))
print("\n\tb. Tính tích của mảng 1 chiều")
def tich(a):
    arr = [] 
    tich = 1
    for k in range(a):
        t = input(f"\tNhập giá trị [{k}]: ")
        arr.append(int(t))
        tich *= arr[k]
    return tich
print("\tTích của mảng là: ", tich(a))
print("\n\tc. Tìm giá trị lớn nhất")
def max(a):
    arr = []
    for i in range(a):
        s = input(f"\tNhập giá trị [{i}]: ")
        arr.append(int(s))
    m = arr[0]
    for i in range (1, len(arr)):
        if(arr[i] > m):
            m = arr[i]
    return m
print("\tSố lớn nhất trong mảng là: ", max(a))
print("\n\tc. Tìm giá trị nhỏ nhất")
def min(a):
    arr = [] 
    for t in range(a):
        s = input(f"\tNhập giá trị [{t}]: ")
        arr.append(int(s))
    m = arr[0]
    for i in range (1, len(arr)):
        if(arr[t] < m):
            m = arr[t]
    return m
print("\tSố nhỏ nhất trong mảng là: ", min(a))
print("\n\te. Tìm các số lẻ trong mảng")
def sole(a):
    result = []
    arr = []
    for s in range(a):
        o = input(f"\tNhập giá trị [{s}]: ")
        arr.append(int(o))
    for s in range(0,len(arr)):
        if ( arr[s] % 2 != 0 ):
            result.append(arr[s])
    return result
print("\tCác số lẻ trong mảng gồm: ", sole(a))
print("\n\tf. Tìm số chẵn trong mảng")
def sochan(a):
    result = []
    arr = []
    for s in range(a):
        y = input(f"\tNhập giá trị [{s}]: ")
        arr.append(int(y))
    for s in range(0,len(arr)):
        if ( arr[s] % 2 == 0 ):
            result.append(arr[s])
    return result
print("\tCác số chẵn trong mảng gồm: ", sochan(a))
print("\n\tBài 3_Zalo: Viết chương trình tạo ra list mới \n\tbằng cách ghép một chuỗi s vào các phần tử list cũ.")
list_s = [9,8,7]
arr = []
a = int(input("\tList gồm bao nhiêu phần tử? "))
for s in range(a):
    i = input(f"\tNhập giá trị [{s}]: ")
    arr.append(int(i))
print("\tList mới:" + str(arr))
print("\tList cũ:" + str(list_s))
print("\tKết quả:" + str(list_s) + str(arr))
print("\n\tBài 2_PDF")
a = int(input("\tNhập số lượng id bài hát: "))
def baihat(a):
    result = []
    arr = []
    count = 0
    for s in range (a):
        i = input(f"\tNhập id [{s}]: ")
        arr.append(int(i))
    for s in arr:
        if s not in result:
            result.append(s)
            count += 1
    return count,result
print("\tCác bài hát đã nghe có id là: " + str(baihat(a)))