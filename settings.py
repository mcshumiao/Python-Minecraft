import math

TICKS_PER_SEC = 120

SECTOR_SIZE = 16

GTIME = 0  # 当前世界时间
GDAY = 0.0005
GNIGHT = 0.0015

WALKING_SPEED = 5  # 走路速度
RUNNING_SPEED = 7  # 跑步速度
FLYING_SPEED = 17  # 飞行速度
SWIMMING_SPEED = 4

GRAVITY = 29.0  # 重力
MAX_JUMP_HEIGHT = 1.252  # 最大跳跃速度
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
TERMINAL_VELOCITY = 29999  # 终端速度

PLAYER_HEIGHT = 2 # 玩家高度

WORLDLEN = 21  # 世界长度
BASELEN = 12

TEXTURE_PATH = 'texture0.png'  # 纹理文件

NRC = []
DNRC = []


def getlen(x, y):
    return math.sqrt(x * x + y * y)


for x in range(-4, 5):
    for y in range(-4, 5):
        if getlen(x * BASELEN, y * BASELEN) <= 32:
            NRC.append((x * BASELEN, y * BASELEN))
for x in range(-1, 2):
    for y in range(-1, 2):
        DNRC.append((x * 64, y * 64))
