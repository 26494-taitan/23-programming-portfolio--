"""

เลือกโจทย์ : โปรแกรมคำนวณอายุจากปีเกิด
I : ปีเกิด (พ.ศ)
P : นำ ปีปัจจุบัน - ปีเกิด
O : แสดงอายุ
ตัวแปร : birth-year , current_year , age

"""
ใน colab
print("โปรแกรมคำนวณอายุจากปีเกิด")
print("ทำโดย นายแทนทัย ฉิมวิเชียร ม.4/4 เลขที่23")
birth_year = int(input("กรุณากรอกปีเกิด (พ.ศ)"))
current_year = 2569
age = current_year - birth_year
print("คุณมีอายุประมาณ", age, "ปี")
