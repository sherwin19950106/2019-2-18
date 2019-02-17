import os
import time
from subprocess import *


class Action:
    def recording(self):
        fileName = time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.mp4'
        ret = os.system(f'E:/ffmpeg/bin/ffmpeg.exe -y -rtbufsize 100M -f gdigrab -framerate 10 -draw_mouse 1 -i desktop\
         -c:v libx264 -r 20 -crf 35 -pix_fmt yuv420p -fs 100M "{fileName}"')
        return ret

    def merge(self):
        list = []
        str =''
        resp = Popen("dir *.mp4 /b", shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()
        for i in resp:
            print(f'{resp.index(i)+1}-{i.decode().strip()}')
            list.append(i.decode().strip())
        choose_num = (input('请选择要合并视频的视频文件序号'))
        print(choose_num)
        for num in choose_num:
            if num.isdigit():
                print(num)
                str = str +'\nfile '+list[int(num)-1]
        file = open('concat.txt','w')
        file.write(str.strip())
        file.close()
        ret = os.system('E:/ffmpeg/bin/ffmpeg.exe -f concat -i concat.txt -codec copy out.mp4')
        return ret
a = Action()
choose = input(" '请选择您要做的操作：1：录制视频，2：合并视频：'")
if choose.isdigit():
    if choose == '1':
        if a.recording() == 0:
            print('录制成功')
        else:
            print('录制失败')
    elif choose =='2':
        if a.merge() == 0:
            print('合并成功')
        else:
            print('合并失败')
    else:
        print('无指令')
else:
    print('请输入数字')
