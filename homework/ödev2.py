d1 = {"isim:":"Fatih", "soyisim:":"Sugurlu" ,"yaş:":"19","okul:":"TOBB Üniversitesi", "gpa:":"3.8"}
d2 = {"isim:":"Furkan", "soyisim:":"Bastem" ,"yaş:":"26","okul:":"Yıldız Teknik Üniversitesi", "gpa:":"3.5"}
d3 = {"isim:":"Ali", "soyisim:":"Veli" ,"yaş:":"20","okul:":"Ankara Üniversitesi", "gpa:":"3.1"}
d4 = {"isim:":"Bebiş", "soyisim:":"Şahin" ,"yaş:":"21","okul:":"Boğaziçi Üniversitesi", "gpa:":"4"}
d5 = {"isim:":"Bahar", "soyisim:":"Küyük" ,"yaş:":"22","okul:":"Gazi Üniversitesi", "gpa:":"3.7"}


a=[d1.values(),d2.values(),d3.values(),d4.values(),d5.values()]

for i,j,k,l,m in a:
    print(i,j,k,"yaşında",l,"'nde okumakta",m,"ortalamaya sahip.")