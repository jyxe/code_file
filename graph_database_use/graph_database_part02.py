from py2neo import Graph

graph = Graph("bolt://localhost:7687",username = "neo4j",password="13820541017")

def operation_neo4j_database(cypher):
    graph.run(cypher)

def main():
    cypher=("create (P1:User1{name:'Alice'}),(P2:User1{name:'Bob'}),(P3:User1{name:'Zach'}),(P4:User1{name:'Helen'}),"
            +"(P5:User1{name:'Ingrid'}),(P6:User1{name:'Jim'}),(P7:User1{name:'Grace'}),(P8:User1{name:'Frad'}),"
            +"(P9:User1{name:'Chad'}),(P10:User1{name:'Dvae'}),(P11:User1{name:'Ed'}),(P1)-[:FRIEND_OF]->(P2),"
            +"(P2)-[:FRIEND_OF]->(P1),(P2)-[:FRIEND_OF]->(P3),(P2)-[:FRIEND_OF]->(P6),(P6)-[:FRIEND_OF]->(P2),(P3)-[:FRIEND_OF]->(P6)"
            +",(P6)-[:FRIEND_OF]->(P3),(P3)-[:FRIEND_OF]->(P1),(P6)-[:BOSS_OF]->(P3),(P3)-[:LOVES]->(P4),(P4)-[:LOVES]->(P3)"
            +",(P5)-[:LOVES]->(P3),(P5)-[:DISLIKES]->(P4),(P6)-[:FRIEND_OF]->(P9),(P9)-[:FRIEND_OF]->(P6),(P6)-[:COLLEAGUE_OF]->(P9),"
            +"(P9)-[:COLLEAGUE_OF]->(P6),(P6)-[:COLLEAGUE_OF]->(P10),(P10)-[:COLLEAGUE_OF]->(P6),(P6)-[:FRIEND_OF]->(P7),"
            +"(P7)-[:MARRIED_TO]->(P8),(P8)-[:MARRIED_TO]->(P7),(P8)-[:FRIEND_OF]->(P11),(P11)-[:FRIEND_OF]->(P8),"
            +"(P10)-[:FRIEND_OF]->(P11),(P11)-[:FRIEND_OF]->(P10)")

    operation_neo4j_database(cypher)

if __name__ == "__main__":
    main()