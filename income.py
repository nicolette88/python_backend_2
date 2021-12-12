import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from flask import Flask
from flask import send_file

app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')


@app.route('/')
def hello_world():
    # data_source = np.random.randint(1, 6, 40).reshape(10, 4)
    # your code goes here....
    file = open('income.txt', 'r')
    lines = file.readlines()
    data_source = []
    data_title = []

    for lineIndex, lineItem in enumerate(lines):
        tmpLine = lineItem.strip("\n")

        if (lineIndex != 0):
            tmpLine = tmpLine.replace(" ", "")
            tmpList = []
            for item in tmpLine.split(","):
                tmpList.append(int(item))
            data_source.append(tmpList)
        else:
            data_title = tmpLine.split(",")
    # my code ends
    df = pd.DataFrame(data_source)
    # df.columns = ['Class A', 'Class B', 'Class C', 'Class D']
    df.columns = data_title
    sns_plot = sns.barplot(palette="ch:.25", data=df, ci=None)
    sns_plot.figure.savefig("output.png")
    plt.close()
    return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# Teszt kód
# file = open('income.txt', 'r')
# lines = file.readlines()
# newLines = []

# for lineIndex, lineItem in enumerate(lines):
#     tmpLine = lineItem.strip("\n")
#     tmpLine = tmpLine.replace(" ", "")
#     tmpList = []
#     if (lineIndex != 0):
#         for item in tmpLine.split(","):
#             tmpList.append(int(item))
#     else:
#         tmpList = tmpLine.split(",")
#     newLines.append(tmpList)
# print(newLines)
