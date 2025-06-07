# plotter.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_expense_pie(by_category):
    fig, ax = plt.subplots()
    ax.pie(by_category["Amount"], labels=by_category["Category"], autopct='%1.1f%%')
    ax.set_title("Expense Breakdown by Category")
    return fig

def plot_bar_chart(by_category):
    fig, ax = plt.subplots()
    sns.barplot(x="Category", y="Amount", data=by_category, ax=ax)
    ax.set_title("Total Amount per Category")
    ax.bar_label(ax.containers[0])
    return fig
