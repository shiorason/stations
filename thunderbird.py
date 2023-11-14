import random as r
l = ['新大阪','高槻','京都','堅田','近江今津','敦賀','武生','鯖江','福井','芦原温泉','大聖寺','加賀温泉','小松','松任']
k = ''
for i in l:
  ran = r.randrange(0,2)
  if ran == 0:
    k = k + i + ','
print('大阪,'+k+'金沢')
