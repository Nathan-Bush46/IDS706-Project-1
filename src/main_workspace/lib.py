import pandas as pd
import matplotlib.pyplot as plt


def calculate(file_path, path_of_image=None):
    raw_training = pd.read_csv(file_path)
    df_train_x = raw_training.iloc[:, :-1]
    mean = ("mean\n", df_train_x[["stem-height", "stem-width"]].mean())
    median = ("median\n", df_train_x[["stem-height", "stem-width"]].median())
    std = ("std\n", df_train_x[["stem-height", "stem-width"]].std())
    df_train_x.plot.scatter("stem-width", "stem-height")
    if path_of_image:
        plt.savefig(path_of_image + "scatter_plot.png")
        plt.close(path_of_image + "scatter_plot.png")
    return [mean, median, std]
