# -*- coding: cp1251 -*-
import datetime
from PIL import Image, ImageDraw, ImageFont
import numpy as np
#��� ���������, pillow � ������ �������� �� �����
#Esli kirilica ne raboet cmenite codirovku v IDE na 1251

 #1
print('����������, ������� ���� ���� ��������, ������ �������!')
day = int(input('������� ����: '))
month = int(input('�����: '))
year = int(input('���: '))
TODAY = datetime.date.today()


#2
week_days=["�����������","�������","�����","�������","�������","�������","����������"]
week_num=datetime.date(year,month,day).weekday()
print(week_days[week_num])

#3
if year % 4 != 0:
    print('��� �� ����������.')

elif year % 100 == 0:
    if year % 400 == 0:
        print('��� ����������.')
    else:
        print('��� �� ����������.')
else:
    print('��� ����������.')

 #4
print(f'��� ������� ��� - {TODAY.year - year - ((TODAY.month, TODAY.day) < (month, day))} !')

#5
day = str(day) 
month = str (month)
year = str (year)
text = (day + '  ' + month + '  ' + year)
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getbbox(text)[2:]
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','*'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print( "\n".join(strings))


