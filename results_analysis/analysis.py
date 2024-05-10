import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

results = pd.read_csv('./data/evaluation_results.csv')
results_filtered = pd.read_csv('./data/evaluation_results_filtered.csv')

sns.set(style="whitegrid")

clarity_order = ["Very unclear", "Somewhat unclear", "Neutral", "Somewhat clear", "Very clear"]
difficulty_order = ["Very difficult", "Difficult", "Just right", "Easy", "Very easy"]


def plot_ratings(data, title, filename, suffix=''):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5), dpi=300)  # Set dpi here for high resolution in the figure
    fig.suptitle(title, fontsize=16)

    sns.countplot(ax=axes[0],
                  x=data['How would you rate the overall clarity of the explanations provided in the exercises?'],
                  order=clarity_order)
    axes[0].set_title('Clarity of Explanations' + suffix)
    axes[0].set_xlabel('Rating')
    axes[0].set_ylabel('Count')
    axes[0].tick_params(axis='x', rotation=45)

    sns.countplot(ax=axes[1],
                  x=data['How would you rate the overall clarity of the instructions provided in the exercises?'],
                  order=clarity_order)
    axes[1].set_title('Clarity of Instructions' + suffix)
    axes[1].set_xlabel('Rating')
    axes[1].set_ylabel('Count')
    axes[1].tick_params(axis='x', rotation=45)

    sns.countplot(ax=axes[2], x=data['How would you rate the difficulty level of the exercises?'],
                  order=difficulty_order)
    axes[2].set_title('Difficulty Level' + suffix)
    axes[2].set_xlabel('Rating')
    axes[2].set_ylabel('Count')
    axes[2].tick_params(axis='x', rotation=45)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    plt.savefig(filename, dpi=300)


plot_ratings(results, 'Full Dataset', '../graphs/full_dataset.png')
plot_ratings(results_filtered, 'Filtered Dataset', '../graphs/filtered_dataset.png', ' (Filtered)')