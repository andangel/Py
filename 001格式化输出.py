name=input("姓名:")
age=int(input("年龄:"))
job=input("职位:")
salary=input("薪资:")

label=int(input("你想用第几种格式化输出?"))

if label!=0 and label<=3:
    if label==1:
        info = '''
        ----- 格式1 信息表 -----
        姓名:{_name}
        年龄:{_age}
        职位:{_job}
        薪资:{_salary}
        '''.format(_name=name,
                   _age=age,
                   _job=job,
                   _salary=salary)
        print(info)

    elif label==2:
        info = '''
        ----- 格式2 信息表 -----
        姓名:%s
        年龄:%d
        职位:%s
        薪资:%s
        '''%(name,
             age,
             job,
             salary)
        print(info)

    elif label==3:
        info = '''
        ----- 格式3 信息表 -----
        姓名:{0}
        年龄:{1}
        职位:{2}
        薪资:{3}
        '''.format(name,
                   age,
                   job,
                   salary)
        print(info)

else:
    print("输入选项必须是1-3")
