from user.models import User


def get_age_rec_list(user,age_delta):
    '''匹配相差年龄的对象'''
    max_birth_year=user.birth_year+age_delta
    min_birth_year=user.birth_year-age_delta
    users=User.objects.filter(birth_year__in=(min_birth_year,max_birth_year))

    sex='男性' if user.sex=='男性' else '女性'
    users=users.filter(sex=sex)
    return users
