# 需求
# 用户
    #登录
        # 账号，密码
    #注册
        # 账号，密码+密码确认
# 书籍
    # 查询所有书籍
    # 根据类别查询书籍
    # 根据价格查询书籍
    # 根据书名查询一本书
    # 修改一本书的信息
        # 获取书名信息
        # 修改书籍的内容
    # 删除一本书
        # 获取书籍信息
        # 确认
    # 添加一本书
        # 输入书籍信息

###################################################
# 创建数据库
userDB=[['admin','123'],['zhang3','123'],['li4','123']]

bookDB=[['《Python丛书》','计算机','guido',9.99,'看不懂'],
        ['《天龙八部》','武侠小说','金庸',19.99,'很好看'],
        ['《西游记》','古典小说','吴承恩',99.99,'很好看'],
        ['《三少爷的剑》','武侠小说','古龙',9.99,'很好看'],
        ['《鬼吹灯》','悬疑小说','不详',19.99,'看不懂'],
        ['《高等数学(上)》','大学教材','贾鹂',49.99,'完全看不懂'],
        ['《风云》','漫画','马荣成',9.99,'看不懂'],
        ['《盗墓笔记》','悬疑小说','南派三叔',9.99,'看不懂'],
        ['《儒林外史》','纪录历史','司马光',9.99,'看不懂'],
        ['《史记》','纪录历史','司马迁',9.99,'看不懂'] ]

# 欢迎页面
print('#################欢迎使用图书管理系统####################')
while 1:
    r1=input('登录请选择1、注册请选择2：\n')

    # 定义登录标志
    flag1=0
    # 用户
    if r1=='1':
        # 登录
        while 1:
            name=input('请输入账号：')
            pwd=input('请输入密码：')
            # 判断是否登录成功
            for i in userDB:  #i:每一个用户列表
                if i[0]==name and i[1]==pwd:
                    flag1=1
            if flag1==1:
                print('登录成功')
                # 进入图书操作界面
                # 作业
            else:
                print('账号或密码错误，请重新登录')

    elif r1=='2':
        # 注册
        while 1:
            name=input('请输入账号：')
            flag2=0
            for i in userDB:
                if i[0]==name:
                    flag2=1
            if flag2==1:
                print('账号已存在，请重新注册')
            else:
                break
                
        flag3=0
        while 1:
            pwd1=input('请输入密码：')
            pwd2=input('请再次输入密码：')
            if pwd1==pwd2:
                # 验证成功
                # 向数据库添加一个用户
                userDB.append([name,pwd1])
                print('注册成功')
                flag3=1
            else:
                print('两次密码不一致，请重新输入')
            if flag3==1:
                # 成功注册，跳出循环
                break
        
        
    else:
        print('输入有误，请重新登录')
