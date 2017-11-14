import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import itertools

import statsmodels.api as sm


def basic(df):
    df.info()
    df.describe()
    pd.scatter_matrix(df)
    plt.show()
    df.boxplot()
    plt.show()


def residual_summary(df, dependent, exclude=[]):
    X = []
    for x in df.columns.values:
        if x==dependent or df[x].dtype == 'O' or x in exclude:
            continue
        X.append(x)

    model = sm.OLS(df[dependent], df[X])
    results = model.fit()
    print(results.summary())

    GFQ = sm.stats.diagnostic.HetGoldfeldQuandt().run(results.fittedvalues, results.outlier_test())

    print("++++++++++++++\nGoldfeld-Quandt: {}\n++++++++++++++".format(GFQ))
    sm.graphics.qqplot(results.outlier_test()['student_resid'])
    plt.show()

    plt.scatter(results.fittedvalues, results.outlier_test()['student_resid'])
    plt.xlabel('Predicted')
    plt.ylabel('Student Residual')
    plt.show()
    statsmodels.graphics.regressionplots.influence_plot(results)
    plt.show()
