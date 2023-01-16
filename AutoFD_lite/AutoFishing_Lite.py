import cv2
import pyautogui
import time
import numpy as np

# 如果运行程序无论如何打印参数都为1.00需要自行截图替换文件夹中的template.png文件

# ---配置---
RESOLUTION = (1920, 1080) # 电脑分辨率
STD = 0.28 # 识别的方差
TEMPLATE_PATH = r'template.png' # 模板图片
SHOT_SCALE = 1.25 # 截图区域占屏幕的区域 2为一半 1.5为1/4 1为无
RUN_SPEED = 0.05 # 每次循环的间隔 程序占用过高可调低
PRINT_INTERVAL = 5 # 每次打印参数的间隔(间隔几次循环) 程序占用过高可调低
# ----------



shot_ = np.array(pyautogui.screenshot(region=(RESOLUTION[0]//SHOT_SCALE, RESOLUTION[1]//SHOT_SCALE, RESOLUTION[0]-RESOLUTION[0]//SHOT_SCALE, RESOLUTION[1]-RESOLUTION[1]//SHOT_SCALE)))
cv2.namedWindow('如果该窗口中无法看见右下角提示 请修改配置', cv2.WINDOW_FREERATIO)
cv2.imshow('如果该窗口中无法看见右下角提示 请修改配置', cv2.cvtColor(shot_, cv2.COLOR_BGR2RGB)) # 测试分辨率
cv2.waitKey(8000)
cv2.destroyAllWindows()
i=0
t=0 # 钓上鱼数
start_time = time.time()
while 1:
    
    i += 1
    time.sleep(RUN_SPEED)
    shot_ = np.array(pyautogui.screenshot(region=(RESOLUTION[0]//SHOT_SCALE, RESOLUTION[1]//SHOT_SCALE, RESOLUTION[0]-RESOLUTION[0]//SHOT_SCALE, RESOLUTION[1]-RESOLUTION[1]//SHOT_SCALE)))
    shot_ = cv2.cvtColor(shot_ ,code=cv2.COLOR_BGR2RGB)
    mu_ban = cv2.imread(TEMPLATE_PATH)

    # shot_ = cv2.imread('./buffer/shot_2.png')
    res = cv2.matchTemplate(shot_,mu_ban,cv2.TM_SQDIFF_NORMED)
    upper_ = cv2.minMaxLoc(res)[0] # 获取列表中最大值
    if upper_ < STD:
        print(f'\n状态:发现鱼[{format(upper_, ".2f")}] 已运行时间: {time.strftime("%H:%M:%S", time.gmtime(time.time()-start_time))} 已钓上{t+1}条鱼')
        t += 1
        pyautogui.click(button='right')
        time.sleep(0.7)
        pyautogui.click(button='right')
        time.sleep(2)
    elif i % PRINT_INTERVAL == 0:
        print(f'\r状态:未发现鱼[{format(upper_, ".2f")}] 已运行时间: {time.strftime("%H:%M:%S", time.gmtime(time.time()-start_time))} 已钓上{t}条鱼', end='')
