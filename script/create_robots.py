import os, sys
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tantan.settings")
import django

django.setup()
from user.models import User

PRE_NAME = (
    '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈',
    '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
    '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏',
    '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
    '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦',
    '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
    '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺',
    '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
    '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余',
    '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
    '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝',
    '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',)

LAST_NAME = ("一", "乙", "二", "十", "丁", "厂", "七", "卜", "人", "入", "八", "九", "几", "儿", "了", "力", "乃", "刀", "又",
             "三", "于", "干", "亏", "士", "工", "土", "才", "寸", "下", "大", "丈", "与", "万", "上", "小", "口", "巾", "山",
             "千", "乞", "川", "亿", "个", "勺", "久", "凡", "及", "夕", "丸", "么", "广", "亡", "门", "义", "之", "尸", "弓",
             "己", "已", "子", "卫", "也", "女", "飞", "刃", "习", "叉", "马", "乡", "丰", "王", "井", "开", "夫", "天", "无",
             "元", "专", "云", "扎", "艺", "木", "五", "支", "厅", "不", "太", "犬", "区", "历", "尤", "友", "匹", "车", "巨",)


def generate_full_name():
    '''generate full_name '''
    last_name_len = len(LAST_NAME)
    pre_name_len = len(PRE_NAME)
    pre_name = PRE_NAME[random.randrange(pre_name_len)]
    first_name = LAST_NAME[random.randrange(last_name_len)]
    second_name = LAST_NAME[random.randrange(last_name_len)]
    full_name = ''.join((pre_name, first_name,second_name))
    return full_name


def create_robots(num: int):

    for i in range(num):
        full_name = generate_full_name()
        nickname = full_name
        phonenum = random.randint(20000000000, 30000000000)
        sex = '男性' if random.choice((False, True)) else '女性'
        birth_year = random.randrange(1970, 2000)
        location = '北京'
        try:
            User.objects.create(
                nickname=nickname,
                phonenum=phonenum,
                sex=sex,
                birth_year=birth_year,
                location=location,
            )
        except:
            pass


if __name__ == '__main__':
    create_robots(100)

