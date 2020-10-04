'''
Bài 08: Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
      Viết hàm
        def bmi_information(m, h)
    để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
'''
print()
print("Bài 8: Tính chỉ số BMI")

x = float(input('Nhập vào cân nặng của bạn (Kí-lô-gam): '))
y = float(input('Nhập vào chiều cao của bạn (Mét): '))

def BMI(cannang,chieucao):
    return cannang/(chieucao**2)

def PhanLoai(BMI):
    if BMI < 18.5:
        return 'Bạn quá gầy'
    elif BMI <= 24.9:
        return  'Bạn bình thường'
    elif BMI <= 29.9:
        return 'Bạn hơi béo'
    elif BMI <= 34.9:
        return 'Bạn béo phì cấp độ 1'
    elif BMI <= 39.9:
        return 'Bạn béo phì cấp độ 2'
    else:
        return 'Bạn béo phì cấp độ 3'

def NguyCoBenh(BMI):
    if BMI < 18.5:
        return 'Nguy cơ thấp'
    elif BMI <= 24.9:
        return  'Nguy cơ trung bình'
    elif BMI <= 29.9:
        return 'Nguy cơ cao'
    elif BMI <= 34.9:
        return 'Nguy cơ cao'
    elif BMI <= 39.9:
        return 'Nguy cơ rất cao'
    else:
        return 'Nguy hiểm'

bmi = BMI(x, y)
print('BMI của bạn = ', bmi)
print(PhanLoai(bmi))
print(NguyCoBenh(bmi))