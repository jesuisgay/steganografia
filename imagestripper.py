import os, sys
from PIL import Image
from testtt import yin, yan
import random
def ralen(ite):return range(ite) if type(ite)==int else range(len(ite))

class A:
        im = Image.open("/Users/jules/Desktop/arena/stegano/og.jpg")
        width, height = im.size
        pixelMap = im.load()
        msg = Image.open("/Users/jules/Desktop/arena/stegano/msg.jpg")
        msg_p_map = msg.load()
        def __init__(s,modo): getattr(s,modo)()


        @classmethod
        def rainbow(cls):
                #Rainbow colorize
                img = Image.new( cls.im.mode, cls.im.size)
                pixelsNew = img.load()
                for i in range(img.size[0]):
                        for j in range(img.size[1]):
                                # print(pixelMap[i,j])
                                if all([cls.pixelMap[i,j][c]>75 for c in range(3)]):
                                        img.putpixel( (i,j) , tuple([random.randint(0,255),random.randint(0,255),random.randint(0,255)]))
                                else:
                                        pixelsNew[i,j] = cls.pixelMap[i,j]
                img.show()
        
        
        @classmethod
        def inject(cls):
                vctr = Image.new( cls.im.mode, cls.im.size)
                pixelsNew = vctr.load()
                msg = Image.new( cls.msg.mode, cls.msg.size)
                for i in range(vctr.size[0]):
                        for j in range(vctr.size[1]):
                                vctr.putpixel((i,j), tuple([p for p in cls.pixelMap[i,j]] ))
                for i in range(msg.size[0]):
                        for j in range(msg.size[1]):
                                o_start = yin((i,j), msg.size[1])
                                tgt = []
                                for a in range(2**3):
                                        _x, _y = yan(o_start + a, cls.im.size[0], cls.im.size[1])
                                        _x -= 1
                                        _y -= 1
                                        tgt += [cls.pixelMap[_x, _y]]
                                # print(tgt)
                                for color_ix, color in enumerate(cls.msg_p_map[i,j]):
                                        # print("{}", end="")
                                        for bit_ix, bit in enumerate(bin(color)[2:]):
                                                # print(bit, end="")
                                                pixel_new = list(tgt[bit_ix])
                                                pixel_new[color_ix] = int(bin(tgt[bit_ix][color_ix])[:-1] + bit, 2)
                                                tgt[bit_ix] = tuple(pixel_new)
                                        # print(tgt)
                                for a in range(8):
                                        x, y = yan(o_start + a, cls.im.size[0], cls.im.size[1])
                                        x -= 1
                                        y -= 1
                                        cors = tgt[a]
                                        vctr.putpixel((x, y), cors)
                                # print()
                for i in range(0, vctr.size[0], 2**3):
                        for j in range(vctr.size[1]):
                                build_pixel = [""]*3
                                for ii in range(2**3):
                                        for color_ix in range(3):
                                                build_pixel[color_ix] += bin(vctr.getpixel((ii,j))[color_ix])[-1]
                                _x, _y = yan(yin((i,j), vctr.size[1]), msg.size[0], msg.size[1])
                                print(_x, _y)
                                msg.putpixel((_x, _y), tuple([int(p,2) for p in build_pixel]))
                msg.show()
        @classmethod
        def twiddlebits(cls):
                img = Image.new( cls.im.mode, cls.im.size)
                pixelsNew = img.load()
                for i in range(img.size[0]):
                        for j in range(img.size[1]):
                                # print([p for p in cls.pixelMap[i,j]])
                                # if all([self.pixelMap[i,j][c]>75 for c in range(3)]):
                                chaff  = str(bin(random.randint(0,3))).split('b',1)[1] 
                                # img.putpixel( (i,j), self.pixelMap[i,j])
                                DIRT = 1
                                CHAFF =  "".join([str(bin(random.randint(0,1))).split('b',1)[1] for _ in ralen(DIRT)])
                                prebins = [bin(p) for p in cls.pixelMap[i,j]]
                                img.putpixel( (i,j) , tuple([int(
                                                        bin(p)[0:-3] 
                                                        + bin(p)[-3:-2]
                                                        + bin(p)[-2:-1]
                                                        + CHAFF or bin(p)[-1],
                                                        2)
                                                        for p in cls.pixelMap[i,j]]))

                                # for ix, p in enumerate(cls.pixelMap[i,j]):
                                #         print(bin(p), prebins[ix][0:-2] + '1' + prebins[ix][-1])
                                # else:
                                        # pixelsNew[i,j] = self.pixelMap[i,j]
                img.show()
A("inject")
# Get the size of the image

 

# # Process every pixel
# for x in range(width):
#    for y in range(height):
#        cc = im.getpixel( (x,y) )
#        print(cc, end="")
#    print()
# for (tag,value) in Image.open(image)._getexif().iteritems():
#         print('%s = %s' % (TAGS.get(tag), value))