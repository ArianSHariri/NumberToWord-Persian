words=[""," یک "," دو "," سه "," چهار "," پنج "," شش "," هفت "," هشت "," نه "," ده "," یازده "," دوازده "," سیزده "," چهارده "," پانزده "," شانزده "," هفده "," هجده "," نوزده "]
tens=[""," ده"," بیست"," سی"," چهل"," پنجاه"," شصت"," هفتاد"," هشتاد"," نود"]
hundreds=[""," يکصد"," دويست"," سيصد"," چهارصد"," پانصد"," ششصد"," هفتصد"," هشتصد"," نهصد"]
thousands=[""," هزار"," میلیون"," میلیارد"," تریلیون"," کوآدریلیون"," کوینتیلیون"," سکستیلیون"," سپتیلیون"," اکتیلیون"," نانیلیون"," دسیلیون"," آندسیلیون"," دیودسیلیون"," تریدسیلیون"," کواتیوردسیلیون"," کویندسیلیون"," سکسدسیلیون"," سپتدسیلیون"," اُکتودسیلیون"," نومدسیلیون"]

def Hundred (x):
    h=x//100
    hwords=""
    if h>0:
        hwords+=hundreds[h]
    t=(x%100)
    if t>0 and h!=0:
        hwords+=" و"
    if t<20:
        hwords+=words[t]
    else:
        hwords+=tens[t//10]
        if (t%10)>0:
            hwords+=" و"+words[t%10]
    return hwords

def numToText(num):
    text = ""
    for i in range (21):
        y = (10**(60-(i*3)))
        x = num//y
        if (x) > 0:
            text+=Hundred(x)+thousands[20-i]
            if num%y>0:
                text+=" و"
        num=num%y
    return text            
    
num=int(input("\nInput a number: "))
if num < 0:
    print ("This number is negative, please enter a positive number")
if num == 0:
    print("صفر")
if num > 0:
    print (numToText(num))
