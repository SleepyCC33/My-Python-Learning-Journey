"""
题目背景：我们宿舍每个月都要交电费，但是大家在宿舍的时间不一样，
因此本程序致力于通过估算每人在宿舍情况，分配每个人需要a的电费
深大电费：0.7元/度，1度=1千瓦时
"""
i = 0
UsageTime = 0
SumTime = 0
namelist = []
"完成变量初始化"

dorm = int(input("请输入您宿舍的人数"))
Usage = float(input("请输入您宿舍本月电费"))
while i < dorm:
    i =  i+1
    name = input(f"情输入你舍友{i}的名字")
    time = float(input(f"请输入舍友{i}的在宿舍时长"))
    dict1 = {"name": name, "time": time}
    namelist.append(dict1)
"获得宿舍信息"

for a in namelist:
    SumTime = a["time"] + SumTime

for a in namelist:
    print(f"{a["name"]}在宿舍时长为{a["time"]},需缴纳{a["time"] * Usage / SumTime}")
"计算与输出电费"
