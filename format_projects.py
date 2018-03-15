import pandas as pd
import os

df = pd.read_excel(os.path.expanduser("~/Downloads/Brainhack Zurich 2018 - Projects (Responses).xlsx"))
s = "# List of Projects\n"


for r in df.iterrows():
    tmp = """
## {n}
*{na} ({em})*

{p}


    """.format(n = r[1]['Project name'],
               na = r[1]['Your name(s)'],
               em = r[1]['Your email'],
               p = r[1]['Project description'],
               )

    s += tmp

with open("projects.md", "w") as fi:
    fi.write(s)