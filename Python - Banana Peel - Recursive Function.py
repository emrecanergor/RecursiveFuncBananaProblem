import math

def recursiveBananas(bananas,price_p):

 #ekstra muz
 more_bananas = bananas / price_p
 print('Ekstra Muz')
 print(more_bananas)
 #elde kalan kabuk (ekstra dahil)
 remainder_peels = (bananas % price_p) + more_bananas
 print('elde kalan kabuk(kalan + ekstra)')
 print(remainder_peels)
 #toplam muz
 even_more_bananas = more_bananas + bananas
 print('toplam muz')
 print(even_more_bananas)

 if(remainder_peels < price_p):
  return more_bananas
 else:
  result = recursiveBananas(remainder_peels, price_p) 
  even_more_bananas = more_bananas +  result
  return even_more_bananas
    
 
 
 
def maxBananas(money,price,price_p):
  bananas = ""
  bananas = money / price   
  totalbanana = recursiveBananas(bananas, price_p)
  totalbanana = totalbanana + bananas
  return int(totalbanana)
 


money=5
price=1
price_p = 5
print(maxBananas(money,price,price_p)) #print 6

money=15
price=1
price_p = 3
print(maxBananas(money,price,price_p)) #print 22

money=20
price=3
price_p = 5
print(maxBananas(money,price,price_p)) #print 8