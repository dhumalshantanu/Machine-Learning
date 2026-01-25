import pandas as pd

data = {
    "Name" : ["Shantanu", "Shardul", "Ananya", "Amey"],
    "Standard" : [15, 4, 8, 3],
    "City" : ["Kolhapur", "Kolhapur", "Pune", "Pune"]
}

df = pd.DataFrame(data)

df.to_json("Output.json", index = False)