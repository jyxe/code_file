from py2neo import Graph

#链接数据库
graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")

#定义函数操作数据库
def operation_neo4j_database(cypher):
    graph.run(cypher)

def main():
    cypher1=("load csv with headers from 'file:/theory.csv' as row create (n:theory444) set n=row")
    cypher2 = ("load csv with headers from 'file:/exercise.csv' as row create (n:exercise444) set n=row")
    cypher3 = ("load csv with headers from 'file:/core_elements.csv' as row create (n:core_elements666) set n=row")
    cypher4 = ("load csv with headers from 'file:/concepts.csv' as row create (n:concepts444) set n=row")
    cypher5 = ("load csv with headers from 'file:/character.csv' as row create (n:character444) set n=row")

    cypher6 = ("create index on :theory444(th_ID)")
    cypher7 = ("create index on :exercise444(ex_ID)")
    cypher8 = ("create index on :core_elements666(core_ID)")
    cypher9 = ("create index on :concepts444(con_ID)")
    cypher10 = ("create index on :character444(ch_ID)")

    cypher11 = ("match (th:theory444),(e:exercise444) where th.th_ID=e.th_ID create (th)-[:related]->(e)")
    cypher12 = ("match (th:theory444),(core:core_elements666) where th.th_ID=core.th_ID create (th)-[:related]->(core)")
    cypher13 = ("match (th:theory444),(co:concepts444) where th.th_ID=co.th_ID create (th)-[:related]->(co)")
    cypher14 = ("match (th:theory444),(ch:character444) where th.th_ID=ch.th_ID create (th)-[:related]->(ch)")

    cypher15 = ("match (e:exercise444),(th:theory444) where e.ex_ID=th.ex_ID create (e)-[:related]->(th)")
    cypher16 = ("match (e:exercise444),(core:core_elements666) where e.ex_ID=core.th_ID create (e)-[:related]->(core)")
    cypher17 = ("match (e:exercise444),(co:concepts444) where e.ex_ID=co.ex_ID create (e)-[:related]->(co)")
    cypher18 = ("match (e:exercise444),(ch:character444) where e.ex_ID=ch.ex_ID create (e)-[:related]->(ch)")

    cypher19 = ("match (con:concepts444),(e:exercise444) where con.con_ID=e.con_ID create (con)-[:related]->(e)")
    cypher20 = ("match (con:concepts444),(core:core_elements666) where con.con_ID=core.th_ID create (con)-[:related]->(core)")
    cypher21 = ("match (con:concepts444),(th:theory444) where con.con_ID=th.con_ID create (con)-[:related]->(th)")
    cypher22 = ("match (con:concepts444),(ch:character444) where con.con_ID=ch.con_ID create (con)-[:related]->(ch)")

    cypher23 = ("match (core:core_elements666),(th:theory444) where core.core_ID=th.core_ID create (core)-[:related]->(th)")
    cypher24 = ("match (core:core_elements666),(e:exercise444) where core.core_ID=e.core_ID create (core)-[:related]->(e)")
    cypher25 = ("match (core:core_elements666),(co:concepts444) where core.core_ID=co.core_ID create (core)-[:related]->(co)")
    cypher26 = ("match (core:core_elements666),(ch:character444) where core.core_ID=ch.core_ID create (core)-[:related]->(ch)")

    cypher27 = ("match (ch:character444),(th:theory444) where ch.ch_ID=th.ch_ID create (ch)-[:related]->(th)")
    cypher28 = ("match (ch:character444),(core:core_elements666) where core.ch_ID=core.th_ID create (ch)-[:related]->(core)")
    cypher29 = ("match (ch:character444),(co:concepts444) where ch.ch_ID=co.ch_ID create (ch)-[:related]->(co)")
    cypher30 = ("match (ch:character444),(e:exercise444) where ch.ch_ID=e.ex_ID create (ch)-[:related]->(e)")

    cypherlist = (cypher1,cypher2,cypher3,cypher4,cypher5,cypher6,cypher7,cypher8,cypher9,cypher10,cypher11,cypher12,cypher13,cypher14,cypher15,cypher16,cypher17,cypher18,cypher19,cypher20,cypher21,cypher22,cypher23,cypher24,cypher25,cypher26,cypher27,cypher28,cypher29,cypher30)
    for i in range(len(cypherlist)):
        operation_neo4j_database(cypherlist[i])

if __name__ == "__main__":
    main()