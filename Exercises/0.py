import pandas as pd
import numpy as np
df_kommuner = pd.DataFrame({
    "Kommuner" : list(("Malmö","Stockholm", "Uppsala", "Göteborg" )),
    "Population": np.array((347949, 975551, 233839, 583056))},
    index= ["1", "2", "3", "4"])


print(df_kommuner["Kommuner"])

print(df_kommuner.loc["4"])

städer = df_kommuner[df_kommuner["Population"]]

städer_sorterad = städer.sort_values(by="Population", ascending=False)
print(städer_sorterad)