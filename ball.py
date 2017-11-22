# coding:utf-8
'''
便于理解和上手，代码没有使用Class（类），使用全局变量取而代之

编写新的pad_ai(pad_pos, ball_pos)函数，实现更好的控制球拍移动的算法

001@cosx.xyz
'''

#引入随机数库和界面库
import random
import simpleguitk as simplegui


#游戏常量
GAME_WIDTH = 610
GAME_HEIGHT = 400                                  #界面左上角坐标为（0，0）、右下角为（610，400）
SCORE_L = 0                                           #左记分牌
SCORE_R = 0
INTERVAL = 10                                           #刷新频率10MS

#球的常量
BALL_RADIUS = 10                        #球半径
BALL_SPEED = [0,0]                     #球初始速度[水平速度，垂直速度]
BALL_POS = [GAME_WIDTH/2, GAME_HEIGHT/2]    #球初始位置[水平位置，垂直位置]
ACC = 1.1                                   #球的加速度，即球拍每打一次，球加速一次

#球拍的常量
PAD_WIDTH = 10                          #球拍宽度
PAD_HEIGHT = 80                         #球拍长度
PAD_SPEED = 250*INTERVAL/1000               #球拍移动速度
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PAD_L_POS = [0, 0]                      #左右两个球拍中心初始位置坐标        
PAD_R_POS = [0, 0]


def ball_init():
    '''球的参数初始化'''
    global BALL_POS, BALL_SPEED
    direction_x = random.randrange(-1,2,2)            #随机产生-1或1表示方向
    direction_y = random.randrange(-1,2,2)            #随机产生-1或1表示方向
    BALL_POS = [GAME_WIDTH/2, GAME_HEIGHT/2]
    BALL_SPEED[0] = direction_x*1
    BALL_SPEED[1] = direction_y*1

def pad_init():
    '''球拍参数初始化'''
    global PAD_L_POS, PAD_R_POS
    #将左右两个球拍中心放置在左右边界的中间
    PAD_L_POS = [HALF_PAD_WIDTH, GAME_HEIGHT/2]
    PAD_R_POS = [GAME_WIDTH-HALF_PAD_WIDTH, GAME_HEIGHT/2]

def create_vertex(c_p, w, h):
    """根据球拍中心坐标c_p[x,y]和球拍尺寸(w,h)，生成球拍这个四边形各顶点坐标，依次为左上，左下，右下，右上"""
    w = w/2
    h = h/2
    return [[c_p[0]-w, c_p[1]-h], [c_p[0]-w, c_p[1]+h], [c_p[0]+w, c_p[1]+h], [c_p[0]+w, c_p[1]-h]]

def draw(c):
    '''
    游戏界面生成函数，将游戏边界、球、球拍、记分牌等元素画出
    draw_line(起点坐标，终点坐标，线宽，颜色)
    draw_text(文本内容，中心位置，字体大小，颜色)
    draw_circle(圆心，半径，线宽，颜色)
    draw_polygon（矩形即画球拍，参数为矩形四个顶点的坐标、线宽、颜色）
    '''
    c.draw_line([GAME_WIDTH/2, 0],[GAME_WIDTH/2, GAME_HEIGHT], 1, "White")
    c.draw_text(str(SCORE_L), (GAME_WIDTH/2 - 82, 80), 42, "White")
    c.draw_text(str(SCORE_R), (GAME_WIDTH/2 + 60, 80), 42, "White")
    c.draw_circle(BALL_POS, BALL_RADIUS, 2, "White", "White")
    c.draw_polygon(create_vertex(PAD_L_POS, PAD_WIDTH, PAD_HEIGHT), 1, "White", "White") 
    c.draw_polygon(create_vertex(PAD_R_POS, PAD_WIDTH, PAD_HEIGHT), 1, "White", "White")

def is_right_win():
    """到达左边界且左球拍没有接住球，右球拍得分，重新开始游戏"""
    global SCORE_R
    if (BALL_POS[0] <= PAD_WIDTH+BALL_RADIUS):
        if abs(BALL_POS[1]-PAD_L_POS[1]) > PAD_HEIGHT / 2:
            SCORE_R +=1
            ball_init()
            pad_init()
        else:
            #左球拍接住球，球撞击球拍后转向，反弹，并加速一次
            BALL_SPEED[0] = -BALL_SPEED[0]
            BALL_SPEED[0] = BALL_SPEED[0] * ACC
            BALL_SPEED[1] = BALL_SPEED[1]* ACC
        
def is_left_win():
    """到达左边界且右球拍没有接住球，左球拍得分，重新开始游戏"""
    global SCORE_L
    if (BALL_POS[0] >= GAME_WIDTH-PAD_WIDTH-BALL_RADIUS):
        if abs(BALL_POS[1]-PAD_R_POS[1]) > PAD_HEIGHT / 2:
            SCORE_L +=1
            ball_init()
            pad_init()
        else:
            #右球拍接住球，球撞击球拍后转向，反弹，并加速一次
            BALL_SPEED[0] = -BALL_SPEED[0]
            BALL_SPEED[0] = BALL_SPEED[0] * ACC
            BALL_SPEED[1] = BALL_SPEED[1]* ACC
         

def update_ball():
    """每个时间间隔调用此函数即可生成球的动态效果"""
    global BALL_POS, BALL_SPEED
    BALL_POS[0] +=BALL_SPEED[0]                 #球的位置每次变化Speed个像素点
    BALL_POS[1] +=BALL_SPEED[1]
    is_left_win()                                       #判断球是否撞到左右边界
    is_right_win()
    #球撞到上下边界，反弹，垂直速度反向
    if (BALL_POS[1] >= GAME_HEIGHT-BALL_RADIUS) or (BALL_POS[1] <=BALL_RADIUS):
        BALL_SPEED[1] = -BALL_SPEED[1]

def pad_ai(pad_pos, ball_pos):
    '''计算返回向上、向下还是不动状态，分别对应1 、 -1 、0'''
    if pad_pos[1] > ball_pos[1]:
        return -1
    else:
        return 1

def pad_limit(pad_pos):
    #限定球拍位置，不能超出边界
    if pad_pos[1] > GAME_HEIGHT - HALF_PAD_HEIGHT:
        pad_pos[1] = GAME_HEIGHT - HALF_PAD_HEIGHT
    if pad_pos[1] < HALF_PAD_HEIGHT:
        pad_pos[1] = HALF_PAD_HEIGHT 
    return pad_pos

def update_pad():
    """每个时间间隔调用此函数即可生成球拍的动态效果"""
    global PAD_L_POS, PAD_R_POS
    PAD_L_POS[1] += pad_ai(PAD_L_POS, BALL_POS)*PAD_SPEED
    PAD_R_POS[1] += pad_ai(PAD_R_POS, BALL_POS)*PAD_SPEED
    PAD_L_POS = pad_limit(PAD_L_POS)
    PAD_R_POS = pad_limit(PAD_R_POS)
    

def timer_handler():
    update_ball()
    update_pad()


#创建游戏界面
frame = simplegui.create_frame("PingPang2", GAME_WIDTH, GAME_HEIGHT)
frame.set_draw_handler(draw)        #初始化界面
timer = simplegui.create_timer(INTERVAL, timer_handler)         #定义刷新频率，连接刷新时执行的动作，产生动画效果

ball_init()                                 #初始化球的参数
pad_init()                                  #初始化挡板参数
timer.start()                               #开始刷新
frame.start()                               #开始绘制图形



