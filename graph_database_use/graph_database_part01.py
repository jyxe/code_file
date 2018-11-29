from py2neo import Graph

#链接数据库
graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")

#定义函数开始执行代码
def operation_graph_database(cypher):
    graph.run(cypher)

def main():
    cypher = ("create (P1:User{name:'Billy'}),(P2:User{name:'Harry'}),(P3:User{name:'Ruth'}),(P1)-[:FOLLOWS]->(P2),"
              +"(P2)-[:FOLLOWS]->(P1),(P2)-[:FOLLOWS]->(P3),(P3)-[:FOLLOWS]->(P2),(P3)-[:FOLLOWS]->(P1)")

    operation_graph_database(cypher)

if __name__ == "__main__":
    main()