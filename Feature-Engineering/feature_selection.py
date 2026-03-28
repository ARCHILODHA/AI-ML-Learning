from sklearn.feature_selection import SelectKBest, chi2

selector = SelectKBest(score_func=chi2, k=2)
X_new = selector.fit_transform(X, y)
