# coding = utf-8

class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """存储《外星人入侵》的所有设置的类"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船的设置
        self.ship_speed_factor = 3
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 30
        self.bullet_width = 1200
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 30

        # 外星人设置
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = -1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction 为1表示向右，为-1表示向左
        self.fleet_direction = 1

        # 计分
        self.alien_points = 500

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
