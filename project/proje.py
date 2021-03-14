i=0
Soru1=print("1) Dinamiti İcat Eden Ünlü Bilim İnsanı Kimdir?")
    
print("A)Albert Einstein")
print("B)Alfred Nobel")
print("C)Thomas Edison")
print("D)Marie Curie ")
S1=input(" ")
if S1 == "B":
   i=i+10
else:  
     i=i
    
Soru2=print("2) İlk Fizik Nobel Ödülünü Kazanan Bilim İnsanı Kimdir? ")

print("A) Wilhelm Röntgen")
print("B) Isaac Newton")
print("C) Nikola Tesla")
print("D) Arşimet")
S2=input(" ")
if S2 == "A" :
  i=i+10
else:
    i=i

Soru3=print("3) Mikroskobu Bularak İlk Mikrobiyolojik İncelemeyi Yapan Bilim İnsanı Kimdir?")   
print("A) Antonie van Leeuwenhoek")
print("B) İbn-i Sina")
print("C) Aristoteles")
print("D) Leopold Fitzinger")
S3=input(" ")
if S3 == "A" :
  i=i+10
else:
  i=i

Soru4=print("4) Televizyonu Kim İcat Etti?")
print("A) Hans Geiger ")
print("B) Dennis Gabor ")
print("C) Ivar Giaever")
print("D) John Logie Baird")
S4=input(" ")
if S4 == "D" :
  i=i+10
else:
     i=i

Soru5=print("5) Katlı oranlar kanunu bulmuş İngiliz kimyacı kimdir?")
print("A) Dmitri Ivanovich Mendeleev")
print("B) Johann Joachim Becher")
print("C) John Dalton")
print("D) Henri Louis le Chatelier")
S5=input(" ")
if S5 == "C" :
  i=i+10
else:
 i=i

Soru6=print("6) Havanın cisimlere uyguladığı kaldırma kuvvetini ölçen alete ne isim verilir?")
print("A) Barometre")
print("B) Altimetre")
print("C) Batimetre")
print("D) Termometre")
S6=input(" ")
if S6 == "A" :
  i=i+10
else:
 i=i

Soru7=print("7) Fizikte bir ışığın kaynağının verdiği ışık şiddetini ölçmeye yarayan araca ne isim verilir? ")
print("A) Pozometre")
print("B) Fotometre")
print("C) Galvanometre")
print("D) Voltmetre")
S7=input(" ")
if S7 == "B" :
  i=i+10
else:
   i=i

Soru8=print("8)'Dünyanın En Genç Profesörü' Unvanını Kazanan Türk Bilim İnsanı Aşşağıdakilerden Hangisidir?")
print("A) Cahit Arf")
print("B) Hulusi Behçet")
print("C) Galvanometre")
print("D) Oktay Sinanoğlu")
S8=input(" ")
if S8 == "D" :
 i=i+10
else:
 i=i

Soru9=print("9)Dalga Özelliği Gösteren Herhangi Bir Fiziksel Varlığın Frekans ve Dalga Boyu'nun Hareketli Bir Gözlemci Tarafından Farklı Zaman Veya Konumlarda Farklı Algılanması Olayına Ne Ad Verilir?")
print("A) Accordion etkisi ")
print("B) Bohr etkisi ")
print("C) Doppler etkisi")
print("D) Mikrodalga işitme etkisi ")
S9=input(" ")
if S9 == "C" :
  i=i+10
else:
 i=i

Soru10=print("10)İlk Başarılı Kornea Nakli Hangi Ünlü Doktor Tarafından Gerçekleştirilmiştir")
print("A) Eduard Zirm ")
print("B) Joel Cooper ")
print("C) David Sutherlandi")
print("D) Louis Kavoussi")
S10=input(" ")
if S10 == "A" :
 i=i+10
else:
  i=i


if i>=50:
    print("Başarılı,Puan=",i)
else:
    print("Başarısız,Tekrar deneyiniz.")