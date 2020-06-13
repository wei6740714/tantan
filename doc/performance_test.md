### 性能测试

- 使用timeit.timeit:

  - timeit.timeit(stmt='pass', setup='pass', timer=, number=1000000, globals=None)

  - 参数解释：	

    - stmt 语句，要执行的表达式，多个语句可以使用;分开
    - setup 语句，只在第一次初始化时执行的表达式，在之后会跳过
    - timer 计时器，默认是time.perf_counter()
    - 
      number 执行次数
      

    