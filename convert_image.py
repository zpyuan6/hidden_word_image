from PIL import Image,ImageDraw,ImageFont
import numpy as np

def main():
    img=np.array(Image.open('source.jpg'))

    blank = Image.new("RGB",[len(img[0])*5,len(img)*5],"white")

    draw=ImageDraw.Draw(blank)

    font=ImageFont.truetype('msyhbd.ttc',size=9)

    s="我喜欢你"

    for i in range(0,len(img),2):
        for j in range(0,len(img[0]),2):
            draw.ink=img[i][j][0]+img[i][j][1]*256+img[i][j][2]*256*256
            draw.text([j*5,i*5],s[int(j/2)%len(s)],font=font)      
        print(i/len(img))
    
    blank.save('targer.jpg')


if __name__ == '__main__':
    main()
