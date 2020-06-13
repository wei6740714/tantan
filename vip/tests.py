from django.test import TestCase

# Create your tests here.


import logging

from user.models import User

logger = logging.getLogger('mdjango')


# logger.setLevel(logging.INFO)，这里不需要写，因为setting.py中写过了，否则要写

class TestLogger(TestCase):
    def testDjangoLog(self):
        self.assertIn(1, [1, 2, 3])
        # logging.getLogger('mdjango').info('1 在 [1,2,3]列表中 测试成功')
        logger.info('My Info')
        logger.error('My Error')
        logger.critical('My Critical')
        logger.info('My Info2')

class TestCache(TestCase):
    def test_cache(self):
        user=User.objects.get(id=1)
