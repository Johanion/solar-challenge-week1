from scipy.stats import zscore

cols_to_check = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
z_scores = df[cols_to_check].apply(zscore)

# Flag outliers (Z > 3 or Z < -3)
outliers = (z_scores.abs() > 3)
print(outliers.sum())
