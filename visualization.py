import matplotlib.pyplot as plt


def visualize_jobs(job_requirements, x_label, y_label, title):
    field = job_requirements.keys()
    counts = job_requirements.values()

    plt.bar(field, counts)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Rotate x-axis labels if needed
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.show()


