import matplotlib.pyplot as plt
import seaborn as sns


def main():
    print("Plot titanic dataset")

    df = sns.load_dataset("titanic")
    sns.pairplot(data=df, hue="alive")
    plt.show()


if __name__ == "__main__":
    main()
