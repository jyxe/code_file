from py2neo import Graph

#链接数据库
graph = Graph("bolt://localhost:7687",username = "neo4j",password="13820541017")

#运行cypher语句从而来操作数据库
cypher = ("create (zhengshu:concept{name:'正数'}),(fushu:concept{name:'负数'}),(youlishu:concept{name:'有理数'}),"
          +"(shuzhou:concept{name:'数轴'}),(xiangfanshu:concept{name:'相反数'}),(jueduizhi:concept{name:'绝对值'}),"
          +"(zhengshu:define{content:'大于0的数叫做正数'}),(fushu:define{content:'正数前面加“-”（负号）的数叫做负数'}),(youlishu:define{content:'正数和负数统称为有理数'}),"
          +"(shuzhou:define{content:'用一条直线上的点表示数，这条直线叫做数轴，且满足三个条件：1.表示0的点叫做原点;2.从原点向右/向上为正方向。从原点向左/向下为负方向;3.选取单位长度'}),"
          +"(xiangfanshu:define{content:'只有符号不同的两个数叫做相反数'}),(zhengshu:define{content:'我们把数轴上表示数a的点到原点的距离叫做数a 的绝对值。记做|a|'}),"
          +"(core_youlishu:core_element{content:'有理数的分类：1.正数，负数与0,2.整数与分数'}),"
          +"(core_shuzhou:core_element{content:'1.点的位置;2.数轴上数的关系'}),"
          +"(character_xiangfanshu:character{content:'和为0'}),(character_jueduizhi:character{content:'非负性'}),"
          +"(character_youlishujia:character{content:'和：加法操作的结果'}),(character_youlishujian:character{content:'减:减法操作的结果'}),"
          +"(character_daishuhe:character{content:'代数和：我们把省略了加号的几个有理数的和的式子叫做这几个数的代数和'}),"
          +"(character_ji:character{content:'积：乘法操作的结果'}),(character_shang:character{content:'商：除法操作的结果'}),"
          +"(theroy_zhengshu1:theory{content:'1.正数可直接用数值表示，例如1,$\frac{1}{2}$等。'}),(theroy_zhengshu2:theory{content:'2.正数也可以在前面加”+”表示'}),"
          +"(theroy_zhengshu3:theory{content:'3.正数的含义:如果一个问题中出现了意义相反的两个量，可以用正数来表示其中的一方面'}),"
          +"(theroy_fushu:theory{content:'负数在正数前面加”-”号'}),(theroy_youlishu1:theory{content:'1.	有理数的表示：数轴'}),"
          +"(theroy_youlishu1:theory{content:'有理数比较大小'}),(theroy_youlishu1:theory{content:'1.	有理数的表示：数轴'}),(theroy_youlishu1:theory{content:'1.	有理数的表示：数轴'}),"
          +"")