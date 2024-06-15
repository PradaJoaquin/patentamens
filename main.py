import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_number_found(df: pd.DataFrame):
    # Plot the number of times each person found a patent ordered by the number of times they found a patent in descending order
    found_by = df.groupby("encontradaPor").size().sort_values(ascending=False)

    # Add Facu to the list of people :)
    found_by["Facu"] = 0

    found_by.plot(kind="bar")

    # Remove the x label
    plt.xlabel("")

    # Rotate the x labels
    plt.xticks(rotation=0)

    # Put the number of times found on top of the bars
    for i in range(len(found_by)):
        plt.text(
            i,
            found_by.values[i] + 0.3,
            found_by.values[i],
            ha="center",
        )

    plt.title("Número de patentes encontradas por persona")
    plt.show()


def plot_estadisticas(df: pd.DataFrame):
    plot_number_found(df)


def read_data():
    # Read the data from the csv file
    data = pd.read_csv("data.csv")

    # convert the data to a dataframe
    df = pd.DataFrame(data)

    # convert fecha to datetime
    df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True)

    return df


def main():
    df = read_data()

    plot_estadisticas(df)


if __name__ == "__main__":
    main()
