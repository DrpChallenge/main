import xml.etree.ElementTree as ET
from xml.dom import minidom
from pathlib import Path
import pandas as pd


def save_map_xml(map_path: Path, output_xml_path: Path) -> None:
    node_df = pd.read_csv(map_path / "node.csv")
    edge_df = pd.read_csv(map_path / "edge.csv")

    node_id_to_pos = {row["ID(ignored)"]: (row["x"], row["y"]) for _, row in node_df.iterrows()}

    graphml = ET.Element("graphml")
    key0 = ET.SubElement(graphml, "key", id="key0")
    key0.set("for", "node")
    key0.set("attr.name", "coords")
    key0.set("attr.type", "string")

    key1 = ET.SubElement(graphml, "key", id="key1")
    key1.set("for", "node")
    key1.set("attr.name", "weight")
    key1.set("attr.type", "double")

    graph = ET.SubElement(
        graphml,
        "graph",
        id="G",
        edgedefault="directed",
        parse_nodeids="free",
        parse_edgeids="canonical",
        parse_order="nodesfirst",
    )

    for _, row in node_df.iterrows():
        id = int(row["ID(ignored)"])
        node = ET.SubElement(graph, "node", id=f"n{id}")
        data = ET.SubElement(node, "data", key="key0")
        data.text = f"{row['x']},{row['y']}"

    for id, row in edge_df.iterrows():
        edge = ET.SubElement(
            graph,
            "edge",
            id=f"e{id}",
            source=f"n{row['from']}",
            target=f"n{row['to']}",
        )
        data = ET.SubElement(edge, "data", key="key1")

        x_diff = node_id_to_pos[row["from"]][0] - node_id_to_pos[row["to"]][0]
        y_diff = node_id_to_pos[row["from"]][1] - node_id_to_pos[row["to"]][1]

        weight = (x_diff**2 + y_diff**2) ** 0.5

        data.text = str(weight)

        edge_reversed = ET.SubElement(
            graph,
            "edge",
            id=f"e{id}_reversed",
            source=f"n{row['to']}",
            target=f"n{row['from']}",
        )
        data_reversed = ET.SubElement(edge_reversed, "data", key="key1")
        data_reversed.text = str(weight)

    doc = minidom.parseString(ET.tostring(graphml, "utf-8"))
    with open(output_xml_path / "map.xml", "w") as f:
        doc.writexml(f, encoding="utf-8", newl="\n", indent="", addindent="  ")


if __name__ == "__main__":
    maps_path = Path.cwd().parent.parent / "drp_env" / "map"

    for map_path in maps_path.glob("*/"):
        # map_path の最後のディレクトリ名を取得
        map_name = map_path.name
        output_path = Path.cwd() / "maps" / map_name
        output_path.mkdir(parents=True, exist_ok=True)  

        save_map_xml(map_path, output_path)
