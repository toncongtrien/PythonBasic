print("\n\tBài 2_PDF")
a = int(input("\tNhập a: "))
def baihat(a):
    result = []
    arr = []
    count = 0
    for s in range (a):
        i = input(f"\tNhập giá trị [{s}]: ")
        arr.append(int(i))
    for s in arr:
        if s not in result:
            result.append(s)
            count += 1
    return count,result
print("\t"+str(baihat(a)))