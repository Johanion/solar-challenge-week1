# Suppose 'cleaning_flag' is a binary column indicating cleaning
df.groupby('cleaning_flag')[['ModA', 'ModB']].mean().plot(kind='bar')
plt.title('Avg ModA & ModB Pre/Post Cleaning')
plt.show()
