import gmpy2

modulo = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy ​​= 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

PG = Point(Gx,Gy)
Z = نقطة (0،0) # نقطة الصفر ، لانهائي في x الحقيقي ، y - الطائرة

# عودة (g ، x ، y) a * x + b * y = gcd (x، y)
def egcd (a، b) :
    if a == 0:
        return (b، 0، 1)
    else:
        g، x، y = egcd (b٪ a، a)
        العودة (g، y - (b // a) * x، x)

def modinv (m، n = modulo):
    بينما m <0:
        m + = n
    g، x، _ = egcd (m، n)
    if g == 1:
        إرجاع x٪ n

    else: print ('لا يوجد معكوس')

def mul2 (Pmul2، p = modulo):
    R = Point (0،0)
    #c = 3 * Pmul2.x * Pmul2.x * modinv (2 * Pmul2.y، p)٪ p
    c = 3 * Pmul2.x * Pmul2.x * gmpy2.invert (2 * Pmul2.y، p)٪ p
    Rx = (c * c-2 * Pmul2.x) ٪ p
    Ry = (c * (Pmul2.x - Rx) -Pmul2.y)٪ p
    إرجاع R

def إضافة (Padd ، Q ، p = modulo):
    إذا Padd.x == Padd.y == 0: إرجاع Q
    إذا كانت Qx == Qy == 0: قم بإرجاع Padd
    إذا كان Padd == Q: قم بإرجاع mul2 (Q)
    R = Point ()
    dx = (Qx - Padd.x)٪ p
    dy = (Qy - Padd.y)٪ p
    c = dy * gmpy2.invert (dx، p)٪ p     
    #c = dy * modinv (dx، p)٪ p
    Rx = (c * c - Padd.x - Qx)٪ p
    Ry = (c * (Padd.x - Rx) - Padd.y)٪ p
    إرجاع R # 6 sub، 3 mul، 1

inv def mulk (k، Pmulk ، p = modulo):
    إذا كان k == 0: إرجاع Z
    إذا كان k == 1: إرجاع Pmulk
    إذا (k٪ 2 == 0): إرجاع mulk (k // 2 ، mul2 (Pmulk ، p) ، p)
    إرجاع إضافة (Pmulk، mulk ((k-1) // 2، mul2 (Pmulk، p)، p)، p)

def sub (P1، P2، p = modulo): # الطرح القياسي P1-P2
    إذا كان P1 == P2 : إرجاع Z
    إذا كان P2.x == P2.y == 0: إرجاع P1
    إرجاع إضافة (P1 ، نقطة (P2.x ، modulo - P2.y))

def div (d، Pdiv، p = modulo): # القسمة العددية ، أي الضرب عن طريق العددية العكسية العكسية
    = gmpy2.invert (d ، الترتيب
    )
