print ("chao mung quy khach")
w = int(input("ban nang bao nhieu kg",))
print("so kg cua ban la", w, end="" )
print(" kg", end="")

h = int(input("ban cao bao nhieu cm"))
m = h/100
print("chieu cao cua ban la",m, end="")
print("m", end="")

BM I= w/(m*m)
print (" bmi cua ban la",BMI)

if BMI < 16:
     print ("ban qua gay, ban nen kiem nguoi yeu de cham ban cho beo")
elif BMI < 18.5:
     print("ban hoi gay, nen an nhieu mot chut")
elif BMI < 25:
     print("ban tieu chuan vua roi, co gang giu dang nhe")
else:
     print("ban hoi beo roi day, ban nen giam can thoi")
