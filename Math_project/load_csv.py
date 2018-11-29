from py2neo import Graph
import time

graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")

def operation_database(cypher):
    graph.run(cypher)

def main():
    cypher1 = ("load csv with headers from 'file:/concepts3.csv' as row create (n:new_concepts14) set n=row")
    cypher2 = ("load csv with headers from 'file:/core_elements3.csv' as row create (n:new_core_elements14) set n=row")
    cypher3 = ("load csv with headers from 'file:/character3.csv' as row create (n:new_character14) set n=row")
    cypher4 = ("load csv with headers from 'file:/theory3.csv' as row create (n:new_theory14) set n=row")
    cypher5 = ("load csv with headers from 'file:/exercise3.csv' as row create (n:new_exercise14) set n=row")

    cypher6 = ("create index on :new_concepts14(con_ID)")
    cypher7 = ("create index on :new_core_elements14(core_ID)")
    cypher8 = ("create index on :new_character14(ch_ID)")
    cypher9 = ("create index on :new_theory14(th_ID)")
    cypher10 = ("create index on :new_exercise14(ex_ID)")

    cypher11 = ("match (core:new_core_elements14),(con:new_concepts14) where core.con_ID=con.con_ID create (core)-[:core_element]->(con)")
    cypher12 = ("match (con:new_concepts14),(core:new_core_elements14) where con.core_ID=core.core_ID create (con)-[:pre_knowledge]->(core)")
    cypher13 = ("match (ch:new_character14),(con:new_concepts14) where ch.con_ID=con.con_ID create (ch)-[:character]->(con)")
    cypher14 = ("match (ch:new_character14),(core:new_core_elements14) where ch.core_ID=core.core_ID create (ch)-[:character]->(core)")
    cypher15 = ("match (th:new_theory14),(con:new_concepts14) where th.con_ID=con.con_ID create (th)-[:theory]->(con)")
    cypher16 = ("match (th:new_theory14),(core:new_core_elements14) where th.core_ID=core.core_ID create (th)-[:theory]->(core)")
    cypher17 = ("match (th:new_theory14),(ch:new_character14) where th.ch_ID=ch.ch_ID create (th)-[:theory]->(ch)")

    cypher18 = ("match (ex:new_exercise14),(con:new_concepts14) where ex.con_ID=con.con_ID create (ex)-[:exercise]->(con)")
    cypher19 = ("match (ex:new_exercise14),(core:new_core_elements14) where ex.core_ID=core.core_ID create (ex)-[:exercise]->(core)")
    cypher20 = ("match (ex:new_exercise14),(ch:new_character14) where ex.ch_ID=ch.ch_ID create (ex)-[:exercise]->(ch)")
    cypher21 = ("match (ex:new_exercise14),(th:new_theory14) where ex.th_ID=th.th_ID create (ex)-[:exercise]->(th)")

    data = [cypher1,cypher2,cypher3,cypher4,cypher5,cypher6,cypher7,cypher8,cypher9,cypher10,cypher11,cypher12,cypher13,cypher14,cypher15,cypher16,cypher17,cypher18,cypher19,cypher20,cypher21]
    for i in range(len(data)):
        print("开始执行第"+str(i+1)+"条指令")
        operation_database(data[i])
        time.sleep(1)

if __name__ == "__main__":
    main()