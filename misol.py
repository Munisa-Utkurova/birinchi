from turtle import color
import matplotlib.pyplot as plt

alifbo=['A','B','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','Oʻ','Gʻ','Sh','Ch','Ng']

names=[ 'Abdujabborova Dinora',
        'Abdumalikova Gulshoda',
        'Aytbayeva Asal',
        'Bobojonov G‘olibjon',
        'Haydarova Barchinoy',
        'Ibragimova Mohitob',
        'Jumanova Feruza',
        'Mirzaxmedova Parizoda',
        'Muhammadyakubva Mo‘minaxon',
        'Muhammadiyeva Dilafruz',
        'Nizomova Fotima',
        'Normurova Kamola',
        'Odilov Bekzod',
        'Qodirov Kamoliddin',
        'Rasulberdiyeva Nazokat',
        'Saidmamatova Durdona'
        'Toshkanboueva Shaxzoda',
        'Tursunboyeva Dinora',
        'To‘xtasinova Gulnoza',
        'Utkurova Munisa',
        'Xamdamova Iroda',
        'Xidirbayeva Muxlisa',
        'Xushmuratova Madina',
        'Ziyodullayeva Maftuna',
        'O‘ralova Charos' 
]

dict={} 
count=0    
for i in alifbo: 
    for j in names:
        if len(i)==2:
            if i[0]==j[0] and i[1]==j[1]:
                count+=1
        elif j[0]==i:
            count+=1
    dict[i]=count
    count=0
print(dict)


plt.bar(dict.keys(), dict.values(), color='coral',width=0.6)
plt.show() 
