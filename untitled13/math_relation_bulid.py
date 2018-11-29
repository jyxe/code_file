from py2neo import Graph

#链接数据库
graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")

#定义函数操作neo4j数据库
def operation_database(cypher):
    graph.run(cypher)

def main():
    # cypher = ("match (zhengshu:conception_relation{concept:'正数'}),(fushu:conception_relation{concept:'负数'}),"
    #           +"(youlishu:conception_relation{concept:'有理数'}),(shuzhou:conception_relation{concept:'数轴'}),"
    #           +"(xiangfanshu:conception_relation{concept:'相反数'}),(jueduizhi:conception_relation{concept:'绝对值'}),"
    #           +"(he:conception_relation{concept:'和'}),(cha:conception_relation{concept:'差'}),(ji:conception_relation{concept:'积'}),"
    #           +"(shang:conception_relation{concept:'商'}),(daishuhe:conception_relation{concept:'代数和'}),"
    #           +"(hunheyunsuan:conception_relation{concept:'混合运算'}),(daoshu:conception_relation{concept:'倒数'}),"
    #           +"(zhengshu1:defination_relation{number:'1'}),(fushu1:defination_relation{number:'2'}),"
    #           +"(youlishu1:defination_relation{number:'3'}),(shuzhou1:defination_relation{number:'4'}),"
    #           +"(xiangfanshu1:defination_relation{number:'5'}),(jueduizhi1:defination_relation{number:'6'}),"
    #           +"(he1:defination_relation{number:'7'}),(cha1:defination_relation{number:'8'}),"
    #           +"(ji1:defination_relation{number:'9'}),(shang1:defination_relation{number:'10'}),"
    #           +"(daishuhe1:defination_relation{number:'11'}),(hunheyunsuan1:defination_relation{number:'12'}),"
    #           +"(daoshu1:defination_relation{number:'13'}) create (zhengshu)-[:define]->(zhengshu1),(fushu)-[:define]->(fushu1),(youlishu)-[:define]->(youlishu1),(shuzhou)-[:define]->(shuzhou1),(xiangfanshu)-[:define]->(xiangfanshu1),(jueduizhi)-[:define]->(jueduizhi1),(he)-[:define]->(he1),(cha)-[:define]->(cha1),(ji)-[:define]->(ji1),(shang)-[:define]->(shang1),(daishuhe)-[:define]->(daishuhe1),(hunheyunsuan)-[:define]->(hunheyunsuan1),(daoshu)-[:define]->(daoshu1)")

    # cypher1 = ("match (ji:conception_relation{concept:'积'}),(chufafaze:theory_relation{define:'除法法则'}),(daoshu:conception_relation{concept:'倒数'}) create (ji)-[:related]->(daoshu)<-[:related]-(chufafaze)")
    cypher2 = ("match (daoshu:conception_relation{concept:'倒数'}),(chufafaze:theory_relation{define:'除法法则'}) create (daoshu)<-[:related]-(chufafaze)")
    operation_database(cypher2)

if __name__ == "__main__":
    main()