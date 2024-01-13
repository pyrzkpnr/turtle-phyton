import turtle as t

#nesne oluşturmak için kullanılır
nesne = t.Turtle()

#ekran oluşturmak için kullanılır
ekran = t.Screen()

#ekran arka planı rengi oluşrutmak için kullanılır
ekran.bgcolor("black")

#Kalem rengi belirlemesi
t.pencolor("red")

a = 0
b = 0

#Hizin belirlemesi
t.speed(50)

#Kalemi kaldır
t.penup()

#Turtle'ı 0'dan 200 konumuna götürür
t.goto(0, 200)

#kalemi indir
t.pendown()


while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    
    if b == 210:
        break

#çizimi bitir
t.done()