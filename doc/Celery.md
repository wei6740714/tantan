Celery

- 安装

  - pip install celery[redis] ==3.1

  - 启动

    - celery -A module_name worker --loglevel=info

  - 示例

    import time
    from celery import Celery
    celery = Celery('tasks', broker='redis://localhost:6379/0')
    @celery.task
    def sendmail():
        time.sleep(5)
        print('mail sent.')

  - ![img](https://ooo.0o0.ooo/2016/12/10/584bbf78e1783.png)

  

  ```
  
  ```

  

  ```
  
  ```

