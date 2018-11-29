from py2neo import Graph

graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")

cypher=("create (n:persoonn{name:'wuqingfeng'})")
graph.run(cypher)
