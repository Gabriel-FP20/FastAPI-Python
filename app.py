from typing import List, Optional
from fastapi import FastAPI, Response
from pydantic import BaseModel
from graph import Graph, dijkstra


my_app = FastAPI()


g = Graph()
g.add_edge("A","B",6)
g.add_edge("A","E",4)
g.add_edge("B","A",6)
g.add_edge("B","C",2)
g.add_edge("B","D",4)
g.add_edge("C","B",3)
g.add_edge("C","D",1)
g.add_edge("C","E",7)
g.add_edge("D","B",8)
g.add_edge("E","B",5)
g.add_edge("E","D",7)


# s = "A"
# d = "C"
# print("Following are all different paths from %s to %s :" % (s, d))
# print(g.print_all_paths(s, d, 3))
# print(dijkstra(g, s)[d].build_path())
# print(g.min_distance_between(s, d))


class GraphNode(BaseModel):
    source: str
    target: str
    distance: int


class Data(BaseModel):
    data: List[GraphNode]
    id: Optional(int)


@my_app.post("/graph", status_code=201)
def put_data(response: Response, data: Data):
    data.id = 1
    return data


@my_app.get("/graph/{graph_id}", status_code=200)
def get_data(response: Response, graph_id: int):
    if graph_id < 0:
        response.status_code = 404
        return
    data = Data(data=[], id=graph_id)
    return data


@my_app.post("/routes/{graph_id}/from/{town1}/to/{town2}", status_code=200)
def distance_town(response: Response, graph_id: int, town1: str, town2: str, max_stops: int):
    res = g.print_all_paths(town1, town2, max_stops)
    return {
        "routes": [
            {
                "route": r,
                "stops": len(r) - 1,
            }
            for r in res
        ],
    }


@my_app.post("/distance/{graph_id}/from/{town1}/to/{town2}", status_code=200)
def stop_distance(response: Response, graph_id: int, town1: str, town2: str):
    res = dijkstra(g, town1)
    return {
        "distance": res[town2].distance,
        "path": res[town2].build_path(),
    }
