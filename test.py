from py2neo import Graph
graph = Graph("http://localhost:7474/db/data/",username="neo4j", password="123")
my_node = graph.evaluate('match (x:Drug) return x')
print(my_node)