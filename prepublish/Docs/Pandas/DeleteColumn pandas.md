The best way to do this in Pandas is to use drop:
```
df = df.drop('column_name', 1)
```
where 1 is the axis number *(0 for rows and 1 for columns.)*



To delete the column without having to reassign df you can do:
```
df.drop('column_name', axis=1, inplace=True)
```



Finally, to drop by column number instead of by column label, try this to delete, e.g. the 1st, 2nd and 4th columns:
```
df = df.drop(df.columns[[0, 1, 3]], axis=1)  # df.columns is zero-based pd.Index



```
Also working with "text" syntax for the columns:
```
df.drop(['column_nameA', 'column_nameB'], axis=1, inplace=True)
```