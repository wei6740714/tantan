from lib.redis import rds
from user.models import User


def get_age_rec_list(user,age_delta):
    '''匹配相差年龄的对象'''
    max_birth_year=user.birth_year+age_delta
    min_birth_year=user.birth_year-age_delta
    users=User.objects.filter(birth_year__in=(min_birth_year,max_birth_year))

    sex='男性' if user.sex=='男性' else '女性'
    users=users.filter(sex=sex)
    return users


LIKE_STYLE={
    'like':1,
    'dislike':-1,
    'superlike':2
}

def change_rand_list(like_style,orange_id):
    score=LIKE_STYLE[like_style]
    rds.hincrby('rank',orange_id,score)

def get_rand_list(num):
    '''获取排行榜'''
    rand_dict=rds.hgetall('rank')
    top=sorted(rand_dict,key=lambda k:-rand_dict[k])[:num]
    rand_dict={key:rand_dict[key] for key in top}

    users = User.objects.filter(id__in=top)
    users=sorted(users,key=lambda user:top.index(user.id))

    it=iter(rand_dict)
    data=[]
    for user in users:
        d={}
        d['nickname']=user.nickname
        d['scores']=rand_dict[next(it)]
        data.append(d)


    return data
