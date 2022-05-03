import graphlib
from typing import List, Optional
from fastapi import Body, FastAPI, Response
from pydantic import BaseModel
from database import get_database
from graph import Graph, dijkstra


my_app = FastAPI()
db = get_database()
id = 0

def create_graph(data):
    g = Graph()
    for item in data.data:
        g.add_edge(item.source,item.target,item.distance)
    return g

class GraphNode(BaseModel):
    source: str
    target: str
    distance: int


class Data(BaseModel):
    id: Optional[int]
    data: List[GraphNode]


@my_app.post("/graph", status_code=201)
def put_data(response: Response, data: Data):
    global id
    graphs = db["graphs"]
    id = id + 1
    data.id = id
    graphs.insert_one(data.dict())
    return data


@my_app.get("/graph/{graph_id}", status_code=200)
def get_data(response: Response, graph_id: int):
    if graph_id < 0:
        response.status_code = 404
        return
    graphs = db["graphs"]
    data = graphs.find_one({"id" : graph_id})
    del data["_id"]
    return data


@my_app.post("/routes/{graph_id}/from/{town1}/to/{town2}", status_code=200)
def distance_town(response: Response, graph_id: int, town1: str, town2: str, max_stops: int):
    graphs = db["graphs"]
    data = graphs.find_one({"id" : graph_id})
    del data["_id"]
    graph = create_graph(Data.parse_obj(data))
    res = graph.find_all_paths(town1, town2, max_stops)
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
    graphs = db["graphs"]
    data = graphs.find_one({"id" : graph_id})
    del data["_id"]
    graph = create_graph(Data.parse_obj(data))
    res = dijkstra(graph, town1)
    print(graph.graph)
    print(graph.edges)
    return {
        "distance": res[town2].distance,
        "path": res[town2].build_path(),
    }
