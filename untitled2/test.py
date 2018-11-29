from py2neo import Graph
graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")

cypher = ("MATCH (n:exercise6) RETURN n.content")
data = graph.run(cypher)

data = data.to_data_frame()
data = data.values.tolist()

if len(data)!=0:
    graph.run("match (n:exercise6) detach delete n")

else:
    graph.run("create (n:exercise9)")