from unittest import main, TestCase

from requests import put
from app import put_data, get_data, distance_town, stop_distance

class TestGraph(graph)
    def test_if_put_data(self):
        result =  put_data({
        "data": [
        {
            "source": "A",
            "target": "B",
            "distance": 6
        },
        {
            "source": "A",
            "target": "E",
            "distance": 4
        },
        {
            "source": "B",
            "target": "A",
            "distance": 6
        },
        {
            "source": "B",
            "target": "C",
            "distance": 2
        },
        {
            "source": "B",
            "target": "D",
            "distance": 4
        },
        {
            "source": "C",
            "target": "B",
            "distance": 3
        },
        {
            "source": "C",
            "target": "D",
            "distance": 1
        },
        {
            "source": "C",
            "target": "E",
            "distance": 7
        },
        {
            "source": "D",
            "target": "B",
            "distance": 8
        },
        {
            "source": "E",
            "target": "B",
            "distance": 5
        },
        {
            "source": "E",
            "target": "D",
            "distance": 7
        }
        ]
        })
        expected = {
            "id": 1,
            "data": [
                {
                    "source": "A",
                    "target": "B",
                    "distance": 6
                },
                {
                    "source": "A",
                    "target": "E",
                    "distance": 4
                },
                {
                    "source": "B",
                    "target": "A",
                    "distance": 6
                },
                {
                    "source": "B",
                    "target": "C",
                    "distance": 2
                },
                {
                    "source": "B",
                    "target": "D",
                    "distance": 4
                },
                {
                    "source": "C",
                    "target": "B",
                    "distance": 3
                },
                {
                    "source": "C",
                    "target": "D",
                    "distance": 1
                },
                {
                    "source": "C",
                    "target": "E",
                    "distance": 7
                },
                {
                    "source": "D",
                    "target": "B",
                    "distance": 8
                },
                {
                    "source": "E",
                    "target": "B",
                    "distance": 5
                },
                {
                    "source": "E",
                    "target": "D",
                    "distance": 7
                }
            ]
        }
        self.assertEqual(result,expected)

if __name__ == '__main__':
    main()