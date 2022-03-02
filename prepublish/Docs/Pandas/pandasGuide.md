# PANDAS Cookbook
[![logo](https://pandas.pydata.org/pandas-docs/stable/_static/pandas.svg)](https://pandas.pydata.org/pandas-docs/stable/index.html)

-   [Getting started](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)
-   [User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
-   [API reference](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)
-   [Development](https://pandas.pydata.org/pandas-docs/stable/development/index.html)
-   [Release notes](https://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html)

1.4.0 

-   [GitHub](https://github.com/pandas-dev/pandas "GitHub")
-   [Twitter](https://twitter.com/pandas_dev "Twitter")

-   [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
-   [Intro to data structures](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html)
-   [Essential basic functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html)
-   [IO tools (text, CSV, HDF5, ...)](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)
-   [Indexing and selecting data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)
-   [MultiIndex / advanced indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)
-   [Merge, join, concatenate and compare](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)
-   [Reshaping and pivot tables](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html)
-   [Working with text data](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)
-   [Working with missing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)
-   [Duplicate Labels](https://pandas.pydata.org/pandas-docs/stable/user_guide/duplicates.html)
-   [Categorical data](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html)
-   [Nullable integer data type](https://pandas.pydata.org/pandas-docs/stable/user_guide/integer_na.html)
-   [Nullable Boolean data type](https://pandas.pydata.org/pandas-docs/stable/user_guide/boolean.html)
-   [Chart Visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
-   [Table Visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)
-   [Computational tools](https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html)
-   [Group by: split-apply-combine](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
-   [Windowing Operations](https://pandas.pydata.org/pandas-docs/stable/user_guide/window.html)
-   [Time series / date functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
-   [Time deltas](https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html)
-   [Options and settings](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html)
-   [Enhancing performance](https://pandas.pydata.org/pandas-docs/stable/user_guide/enhancingperf.html)
-   [Scaling to large datasets](https://pandas.pydata.org/pandas-docs/stable/user_guide/scale.html)
-   [Sparse data structures](https://pandas.pydata.org/pandas-docs/stable/user_guide/sparse.html)
-   [Frequently Asked Questions (FAQ)](https://pandas.pydata.org/pandas-docs/stable/user_guide/gotchas.html)
-   [Cookbook](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#)

 On this page

-   [Idioms](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#idioms)
-   [Selection](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#selection)
-   [Multiindexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#multiindexing)
    -   [Arithmetic](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#arithmetic)
    -   [Slicing](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#slicing)
    -   [Sorting](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#sorting)
    -   [Levels](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#levels)
-   [Missing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#missing-data)
-   [Grouping](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#grouping)
-   [Timeseries](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#timeseries)
-   [Merge](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#merge)
-   [Plotting](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#plotting)
-   [Data in/out](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#data-in-out)
-   [Computation](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#computation)
-   [Timedeltas](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#timedeltas)
-   [Creating example data](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#creating-example-data)

Cookbook[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#cookbook "Permalink to this headline")
=======================================================================================================================

This is a repository for *short and sweet* examples and links for useful pandas recipes. We encourage users to add to this documentation.

Adding interesting links and/or inline examples to this section is a great *First Pull Request*.

Simplified, condensed, new-user friendly, in-line examples have been inserted where possible to augment the Stack-Overflow and GitHub links. Many of the links contain expanded information, above what the in-line examples offer.

pandas (pd) and NumPy (np) are the only two abbreviated imported modules. The rest are kept explicitly imported for newer users.

Idioms[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#idioms "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------

These are some neat pandas `idioms`

[if-then/if-then-else on one column, and assignment to another one or more columns:](https://stackoverflow.com/questions/17128302/python-pandas-idiom-for-if-then-else)
```
In [1]: df = pd.DataFrame(
 ...:    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
 ...: )
 ...:
```
```
In [2]: df
Out[2]:
 AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50
```
### if-then...[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#if-then "Permalink to this headline")

An if-then on one column
```
In [3]: df.loc[df.AAA >= 5, "BBB"] = -1
```
```
In [4]: df
Out[4]:
 AAA  BBB  CCC
0    4   10  100
1    5   -1   50
2    6   -1  -30
3    7   -1  -50
```
An if-then with assignment to 2 columns:
```
In [5]: df.loc[df.AAA >= 5, ["BBB", "CCC"]] = 555

In [6]: df
Out[6]:
 AAA  BBB  CCC
0    4   10  100
1    5  555  555
2    6  555  555
3    7  555  555
```
Add another line with different logic, to do the -else
```
In [7]: df.loc[df.AAA < 5, ["BBB", "CCC"]] = 2000

In [8]: df
Out[8]:
 AAA   BBB   CCC
0    4  2000  2000
1    5   555   555
2    6   555   555
3    7   555   555
```
Or use pandas where after you've set up a mask
```
In [9]: df_mask = pd.DataFrame(
 ...:    {"AAA": [True] * 4, "BBB": [False] * 4, "CCC": [True, False] * 2}
 ...: )
 ...:
```
```
In [10]: df.where(df_mask, -1000)
Out[10]:
 AAA   BBB   CCC
0    4 -1000  2000
1    5 -1000 -1000
2    6 -1000   555
3    7 -1000 -1000
```
[if-then-else using NumPy's where()](https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column)
```
In [11]: df = pd.DataFrame(
 ....:    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
 ....: )
 ....:
```
```
In [12]: df
Out[12]:
 AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50
```
```
In [13]: df["logic"] = np.where(df["AAA"] > 5, "high", "low")

In [14]: df
Out[14]:
 AAA  BBB  CCC logic
0    4   10  100   low
1    5   20   50   low
2    6   30  -30  high
3    7   40  -50  high
```
### Splitting[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#splitting "Permalink to this headline")

[Split a frame with a boolean criterion](https://stackoverflow.com/questions/14957116/how-to-split-a-dataframe-according-to-a-boolean-criterion)
```
In [15]: df = pd.DataFrame(
 ....:    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
 ....: )
 ....:
```
```
In [16]: df
Out[16]:
 AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50
```
```
In [17]: df[df.AAA <= 5]
Out[17]:
 AAA  BBB  CCC
0    4   10  100
1    5   20   50
```
In [18]: df[df.AAA > 5]
Out[18]:
 AAA  BBB  CCC
2    6   30  -30
3    7   40  -50

### Building criteria[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#building-criteria "Permalink to this headline")

[Select with multi-column criteria](https://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe)
```
In [19]: df = pd.DataFrame(
 ....:    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
 ....: )
 ....:
```
```
In [20]: df
Out[20]:
 AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50
```
...and (without assignment returns a Series)

In [21]: df.loc[(df["BBB"] < 25) & (df["CCC"] >= -40), "AAA"]
Out[21]:
0    4
1    5
Name: AAA, dtype: int64

...or (without assignment returns a Series)

In [22]: df.loc[(df["BBB"] > 25) | (df["CCC"] >= -40), "AAA"]
Out[22]:
0    4
1    5
2    6
3    7
Name: AAA, dtype: int64

...or (with assignment modifies the DataFrame.)

In [23]: df.loc[(df["BBB"] > 25) | (df["CCC"] >= 75), "AAA"] = 0.1

In [24]: df
Out[24]:
 AAA  BBB  CCC
0  0.1   10  100
1  5.0   20   50
2  0.1   30  -30
3  0.1   40  -50

[Select rows with data closest to certain value using argsort](https://stackoverflow.com/questions/17758023/return-rows-in-a-dataframe-closest-to-a-user-defined-number)

In [25]: df = pd.DataFrame(
 ....:    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
 ....: )
 ....:

In [26]: df
Out[26]:
 AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In [27]: aValue = 43.0

In [28]: df.loc[(df.CCC - aValue).abs().argsort()]
Out[28]:
 AAA  BBB  CCC
1    5   20   50
0    4   10  100
2    6   30  -30
3    7   40  -50

[Dynamically reduce a list of criteria using a binary operators](https://stackoverflow.com/questions/21058254/pandas-boolean-operation-in-a-python-list/21058331)

In [29]: df = pd.DataFrame(
 ....:    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
 ....: )
 ....:

In [30]: df
Out[30]:
 AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In [31]: Crit1 = df.AAA <= 5.5

In [32]: Crit2 = df.BBB == 10.0

In [33]: Crit3 = df.CCC > -40.0

One could hard code:

In [34]: AllCrit = Crit1 & Crit2 & Crit3

...Or it can be done with a list of dynamically built criteria

In [35]: import functools

In [36]: CritList = [Crit1, Crit2, Crit3]

In [37]: AllCrit = functools.reduce(lambda x, y: x & y, CritList)

In [38]: df[AllCrit]
Out[38]:
 AAA  BBB  CCC
0    4   10  100

Selection[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#selection "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

### Dataframes[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#dataframes "Permalink to this headline")

The [indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing) docs.

[Using both row labels and value conditionals](https://stackoverflow.com/questions/14725068/pandas-using-row-labels-in-boolean-indexing)

In [39]: df = pd.DataFrame(
 ....:    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
 ....: )
 ....:

In [40]: df
Out[40]:
 AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In [41]: df[(df.AAA <= 6) & (df.index.isin([0, 2, 4]))]
Out[41]:
 AAA  BBB  CCC
0    4   10  100
2    6   30  -30

Use loc for label-oriented slicing and iloc positional slicing [GH2904](https://github.com/pandas-dev/pandas/issues/2904)

In [42]: df = pd.DataFrame(
 ....:    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]},
 ....:    index=["foo", "bar", "boo", "kar"],
 ....: )
 ....:

There are 2 explicit slicing methods, with a third general case

1.  Positional-oriented (Python slicing style : exclusive of end)

2.  Label-oriented (Non-Python slicing style : inclusive of end)

3.  General (Either slicing style : depends on if the slice contains labels or positions)

In [43]: df.loc["bar":"kar"]  # Label
Out[43]:
 AAA  BBB  CCC
bar    5   20   50
boo    6   30  -30
kar    7   40  -50

# Generic
In [44]: df[0:3]
Out[44]:
 AAA  BBB  CCC
foo    4   10  100
bar    5   20   50
boo    6   30  -30

In [45]: df["bar":"kar"]
Out[45]:
 AAA  BBB  CCC
bar    5   20   50
boo    6   30  -30
kar    7   40  -50

Ambiguity arises when an index consists of integers with a non-zero start or non-unit increment.

In [46]: data = {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}

In [47]: df2 = pd.DataFrame(data=data, index=[1, 2, 3, 4])  # Note index starts at 1.

In [48]: df2.iloc[1:3]  # Position-oriented
Out[48]:
 AAA  BBB  CCC
2    5   20   50
3    6   30  -30

In [49]: df2.loc[1:3]  # Label-oriented
Out[49]:
 AAA  BBB  CCC
1    4   10  100
2    5   20   50
3    6   30  -30

[Using inverse operator (~) to take the complement of a mask](https://stackoverflow.com/q/14986510)

In [50]: df = pd.DataFrame(
 ....:    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
 ....: )
 ....:

In [51]: df
Out[51]:
 AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50

In [52]: df[~((df.AAA <= 6) & (df.index.isin([0, 2, 4])))]
Out[52]:
 AAA  BBB  CCC
1    5   20   50
3    7   40  -50

### New columns[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#new-columns "Permalink to this headline")

[Efficiently and dynamically creating new columns using applymap](https://stackoverflow.com/questions/16575868/efficiently-creating-additional-columns-in-a-pandas-dataframe-using-map)

In [53]: df = pd.DataFrame({"AAA": [1, 2, 1, 3], "BBB": [1, 1, 2, 2], "CCC": [2, 1, 3, 1]})

In [54]: df
Out[54]:
 AAA  BBB  CCC
0    1    1    2
1    2    1    1
2    1    2    3
3    3    2    1

In [55]: source_cols = df.columns  # Or some subset would work too

In [56]: new_cols = [str(x) + "_cat" for x in source_cols]

In [57]: categories = {1: "Alpha", 2: "Beta", 3: "Charlie"}

In [58]: df[new_cols] = df[source_cols].applymap(categories.get)

In [59]: df
Out[59]:
 AAA  BBB  CCC  AAA_cat BBB_cat  CCC_cat
0    1    1    2    Alpha   Alpha     Beta
1    2    1    1     Beta   Alpha    Alpha
2    1    2    3    Alpha    Beta  Charlie
3    3    2    1  Charlie    Beta    Alpha

[Keep other columns when using min() with groupby](https://stackoverflow.com/q/23394476)

In [60]: df = pd.DataFrame(
 ....:    {"AAA": [1, 1, 1, 2, 2, 2, 3, 3], "BBB": [2, 1, 3, 4, 5, 1, 2, 3]}
 ....: )
 ....:

In [61]: df
Out[61]:
 AAA  BBB
0    1    2
1    1    1
2    1    3
3    2    4
4    2    5
5    2    1
6    3    2
7    3    3

Method 1 : idxmin() to get the index of the minimums

In [62]: df.loc[df.groupby("AAA")["BBB"].idxmin()]
Out[62]:
 AAA  BBB
1    1    1
5    2    1
6    3    2

Method 2 : sort then take first of each

In [63]: df.sort_values(by="BBB").groupby("AAA", as_index=False).first()
Out[63]:
 AAA  BBB
0    1    1
1    2    1
2    3    2

Notice the same results, with the exception of the index.

Multiindexing[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#multiindexing "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------

The [multindexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced-hierarchical) docs.

[Creating a MultiIndex from a labeled frame](https://stackoverflow.com/questions/14916358/reshaping-dataframes-in-pandas-based-on-column-labels)

In [64]: df = pd.DataFrame(
 ....:    {
 ....:        "row": [0, 1, 2],
 ....:        "One_X": [1.1, 1.1, 1.1],
 ....:        "One_Y": [1.2, 1.2, 1.2],
 ....:        "Two_X": [1.11, 1.11, 1.11],
 ....:        "Two_Y": [1.22, 1.22, 1.22],
 ....:    }
 ....: )
 ....:

In [65]: df
Out[65]:
 row  One_X  One_Y  Two_X  Two_Y
0    0    1.1    1.2   1.11   1.22
1    1    1.1    1.2   1.11   1.22
2    2    1.1    1.2   1.11   1.22

# As Labelled Index
In [66]: df = df.set_index("row")

In [67]: df
Out[67]:
 One_X  One_Y  Two_X  Two_Y
row
0      1.1    1.2   1.11   1.22
1      1.1    1.2   1.11   1.22
2      1.1    1.2   1.11   1.22

# With Hierarchical Columns
In [68]: df.columns = pd.MultiIndex.from_tuples([tuple(c.split("_")) for c in df.columns])

In [69]: df
Out[69]:
 One        Two
 X    Y     X     Y
row
0    1.1  1.2  1.11  1.22
1    1.1  1.2  1.11  1.22
2    1.1  1.2  1.11  1.22

# Now stack & Reset
In [70]: df = df.stack(0).reset_index(1)

In [71]: df
Out[71]:
 level_1     X     Y
row
0       One  1.10  1.20
0       Two  1.11  1.22
1       One  1.10  1.20
1       Two  1.11  1.22
2       One  1.10  1.20
2       Two  1.11  1.22

# And fix the labels (Notice the label 'level_1' got added automatically)
In [72]: df.columns = ["Sample", "All_X", "All_Y"]

In [73]: df
Out[73]:
 Sample  All_X  All_Y
row
0      One   1.10   1.20
0      Two   1.11   1.22
1      One   1.10   1.20
1      Two   1.11   1.22
2      One   1.10   1.20
2      Two   1.11   1.22

### Arithmetic[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#arithmetic "Permalink to this headline")

[Performing arithmetic with a MultiIndex that needs broadcasting](https://stackoverflow.com/questions/19501510/divide-entire-pandas-multiindex-dataframe-by-dataframe-variable/19502176#19502176)

In [74]: cols = pd.MultiIndex.from_tuples(
 ....:    [(x, y) for x in ["A", "B", "C"] for y in ["O", "I"]]
 ....: )
 ....:

In [75]: df = pd.DataFrame(np.random.randn(2, 6), index=["n", "m"], columns=cols)

In [76]: df
Out[76]:
 A                   B                   C
 O         I         O         I         O         I
n  0.469112 -0.282863 -1.509059 -1.135632  1.212112 -0.173215
m  0.119209 -1.044236 -0.861849 -2.104569 -0.494929  1.071804

In [77]: df = df.div(df["C"], level=1)

In [78]: df
Out[78]:
 A                   B              C
 O         I         O         I    O    I
n  0.387021  1.633022 -1.244983  6.556214  1.0  1.0
m -0.240860 -0.974279  1.741358 -1.963577  1.0  1.0

### Slicing[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#slicing "Permalink to this headline")

[Slicing a MultiIndex with xs](https://stackoverflow.com/questions/12590131/how-to-slice-multindex-columns-in-pandas-dataframes)

In [79]: coords = [("AA", "one"), ("AA", "six"), ("BB", "one"), ("BB", "two"), ("BB", "six")]

In [80]: index = pd.MultiIndex.from_tuples(coords)

In [81]: df = pd.DataFrame([11, 22, 33, 44, 55], index, ["MyData"])

In [82]: df
Out[82]:
 MyData
AA one      11
 six      22
BB one      33
 two      44
 six      55

To take the cross section of the 1st level and 1st axis the index:

# Note : level and axis are optional, and default to zero
In [83]: df.xs("BB", level=0, axis=0)
Out[83]:
 MyData
one      33
two      44
six      55

...and now the 2nd level of the 1st axis.

In [84]: df.xs("six", level=1, axis=0)
Out[84]:
 MyData
AA      22
BB      55

[Slicing a MultiIndex with xs, method #2](https://stackoverflow.com/questions/14964493/multiindex-based-indexing-in-pandas)

In [85]: import itertools

In [86]: index = list(itertools.product(["Ada", "Quinn", "Violet"], ["Comp", "Math", "Sci"]))

In [87]: headr = list(itertools.product(["Exams", "Labs"], ["I", "II"]))

In [88]: indx = pd.MultiIndex.from_tuples(index, names=["Student", "Course"])

In [89]: cols = pd.MultiIndex.from_tuples(headr)  # Notice these are un-named

In [90]: data = [[70 + x + y + (x * y) % 3 for x in range(4)] for y in range(9)]

In [91]: df = pd.DataFrame(data, indx, cols)

In [92]: df
Out[92]:
 Exams     Labs
 I  II    I  II
Student Course
Ada     Comp      70  71   72  73
 Math      71  73   75  74
 Sci       72  75   75  75
Quinn   Comp      73  74   75  76
 Math      74  76   78  77
 Sci       75  78   78  78
Violet  Comp      76  77   78  79
 Math      77  79   81  80
 Sci       78  81   81  81

In [93]: All = slice(None)

In [94]: df.loc["Violet"]
Out[94]:
 Exams     Labs
 I  II    I  II
Course
Comp      76  77   78  79
Math      77  79   81  80
Sci       78  81   81  81

In [95]: df.loc[(All, "Math"), All]
Out[95]:
 Exams     Labs
 I  II    I  II
Student Course
Ada     Math      71  73   75  74
Quinn   Math      74  76   78  77
Violet  Math      77  79   81  80

In [96]: df.loc[(slice("Ada", "Quinn"), "Math"), All]
Out[96]:
 Exams     Labs
 I  II    I  II
Student Course
Ada     Math      71  73   75  74
Quinn   Math      74  76   78  77

In [97]: df.loc[(All, "Math"), ("Exams")]
Out[97]:
 I  II
Student Course
Ada     Math    71  73
Quinn   Math    74  76
Violet  Math    77  79

In [98]: df.loc[(All, "Math"), (All, "II")]
Out[98]:
 Exams Labs
 II   II
Student Course
Ada     Math      73   74
Quinn   Math      76   77
Violet  Math      79   80

[Setting portions of a MultiIndex with xs](https://stackoverflow.com/questions/19319432/pandas-selecting-a-lower-level-in-a-dataframe-to-do-a-ffill)

### Sorting[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#sorting "Permalink to this headline")

[Sort by specific column or an ordered list of columns, with a MultiIndex](https://stackoverflow.com/q/14733871)

In [99]: df.sort_values(by=("Labs", "II"), ascending=False)
Out[99]:
 Exams     Labs
 I  II    I  II
Student Course
Violet  Sci       78  81   81  81
 Math      77  79   81  80
 Comp      76  77   78  79
Quinn   Sci       75  78   78  78
 Math      74  76   78  77
 Comp      73  74   75  76
Ada     Sci       72  75   75  75
 Math      71  73   75  74
 Comp      70  71   72  73

Partial selection, the need for sortedness [GH2995](https://github.com/pandas-dev/pandas/issues/2995)

### Levels[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#levels "Permalink to this headline")

[Prepending a level to a multiindex](https://stackoverflow.com/questions/14744068/prepend-a-level-to-a-pandas-multiindex)

[Flatten Hierarchical columns](https://stackoverflow.com/q/14507794)

Missing data[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#missing-data "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------

The [missing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#missing-data) docs.

Fill forward a reversed timeseries

In [100]: df = pd.DataFrame(
 .....:    np.random.randn(6, 1),
 .....:    index=pd.date_range("2013-08-01", periods=6, freq="B"),
 .....:    columns=list("A"),
 .....: )
 .....:

In [101]: df.loc[df.index[3], "A"] = np.nan

In [102]: df
Out[102]:
 A
2013-08-01  0.721555
2013-08-02 -0.706771
2013-08-05 -1.039575
2013-08-06       NaN
2013-08-07 -0.424972
2013-08-08  0.567020

In [103]: df.reindex(df.index[::-1]).ffill()
Out[103]:
 A
2013-08-08  0.567020
2013-08-07 -0.424972
2013-08-06 -0.424972
2013-08-05 -1.039575
2013-08-02 -0.706771
2013-08-01  0.721555

[cumsum reset at NaN values](https://stackoverflow.com/questions/18196811/cumsum-reset-at-nan)

### Replace[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#replace "Permalink to this headline")

[Using replace with backrefs](https://stackoverflow.com/questions/16818871/extracting-value-and-creating-new-column-out-of-it)

Grouping[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#grouping "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------

The [grouping](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby) docs.

[Basic grouping with apply](https://stackoverflow.com/questions/15322632/python-pandas-df-groupy-agg-column-reference-in-agg)

Unlike agg, apply's callable is passed a sub-DataFrame which gives you access to all the columns

In [104]: df = pd.DataFrame(
 .....:    {
 .....:        "animal": "cat dog cat fish dog cat cat".split(),
 .....:        "size": list("SSMMMLL"),
 .....:        "weight": [8, 10, 11, 1, 20, 12, 12],
 .....:        "adult": [False] * 5 + [True] * 2,
 .....:    }
 .....: )
 .....:

In [105]: df
Out[105]:
 animal size  weight  adult
0    cat    S       8  False
1    dog    S      10  False
2    cat    M      11  False
3   fish    M       1  False
4    dog    M      20  False
5    cat    L      12   True
6    cat    L      12   True

# List the size of the animals with the highest weight.
In [106]: df.groupby("animal").apply(lambda subf: subf["size"][subf["weight"].idxmax()])
Out[106]:
animal
cat     L
dog     M
fish    M
dtype: object

[Using get_group](https://stackoverflow.com/questions/14734533/how-to-access-pandas-groupby-dataframe-by-key)

In [107]: gb = df.groupby(["animal"])

In [108]: gb.get_group("cat")
Out[108]:
 animal size  weight  adult
0    cat    S       8  False
2    cat    M      11  False
5    cat    L      12   True
6    cat    L      12   True

[Apply to different items in a group](https://stackoverflow.com/questions/15262134/apply-different-functions-to-different-items-in-group-object-python-pandas)

In [109]: def GrowUp(x):
 .....:    avg_weight = sum(x[x["size"] == "S"].weight * 1.5)
 .....:    avg_weight += sum(x[x["size"] == "M"].weight * 1.25)
 .....:    avg_weight += sum(x[x["size"] == "L"].weight)
 .....:    avg_weight /= len(x)
 .....:    return pd.Series(["L", avg_weight, True], index=["size", "weight", "adult"])
 .....:

In [110]: expected_df = gb.apply(GrowUp)

In [111]: expected_df
Out[111]:
 size   weight  adult
animal
cat       L  12.4375   True
dog       L  20.0000   True
fish      L   1.2500   True

[Expanding apply](https://stackoverflow.com/questions/14542145/reductions-down-a-column-in-pandas)

In [112]: S = pd.Series([i / 100.0 for i in range(1, 11)])

In [113]: def cum_ret(x, y):
 .....:    return x * (1 + y)
 .....:

In [114]: def red(x):
 .....:    return functools.reduce(cum_ret, x, 1.0)
 .....:

In [115]: S.expanding().apply(red, raw=True)
Out[115]:
0    1.010000
1    1.030200
2    1.061106
3    1.103550
4    1.158728
5    1.228251
6    1.314229
7    1.419367
8    1.547110
9    1.701821
dtype: float64

[Replacing some values with mean of the rest of a group](https://stackoverflow.com/questions/14760757/replacing-values-with-groupby-means)

In [116]: df = pd.DataFrame({"A": [1, 1, 2, 2], "B": [1, -1, 1, 2]})

In [117]: gb = df.groupby("A")

In [118]: def replace(g):
 .....:    mask = g < 0
 .....:    return g.where(mask, g[~mask].mean())
 .....:

In [119]: gb.transform(replace)
Out[119]:
 B
0  1.0
1 -1.0
2  1.5
3  1.5

[Sort groups by aggregated data](https://stackoverflow.com/questions/14941366/pandas-sort-by-group-aggregate-and-column)

In [120]: df = pd.DataFrame(
 .....:    {
 .....:        "code": ["foo", "bar", "baz"] * 2,
 .....:        "data": [0.16, -0.21, 0.33, 0.45, -0.59, 0.62],
 .....:        "flag": [False, True] * 3,
 .....:    }
 .....: )
 .....:

In [121]: code_groups = df.groupby("code")

In [122]: agg_n_sort_order = code_groups[["data"]].transform(sum).sort_values(by="data")

In [123]: sorted_df = df.loc[agg_n_sort_order.index]

In [124]: sorted_df
Out[124]:
 code  data   flag
1  bar -0.21   True
4  bar -0.59  False
0  foo  0.16  False
3  foo  0.45   True
2  baz  0.33  False
5  baz  0.62   True

[Create multiple aggregated columns](https://stackoverflow.com/questions/14897100/create-multiple-columns-in-pandas-aggregation-function)

In [125]: rng = pd.date_range(start="2014-10-07", periods=10, freq="2min")

In [126]: ts = pd.Series(data=list(range(10)), index=rng)

In [127]: def MyCust(x):
 .....:    if len(x) > 2:
 .....:        return x[1] * 1.234
 .....:    return pd.NaT
 .....:

In [128]: mhc = {"Mean": np.mean, "Max": np.max, "Custom": MyCust}

In [129]: ts.resample("5min").apply(mhc)
Out[129]:
 Mean  Max Custom
2014-10-07 00:00:00   1.0    2  1.234
2014-10-07 00:05:00   3.5    4    NaT
2014-10-07 00:10:00   6.0    7  7.404
2014-10-07 00:15:00   8.5    9    NaT

In [130]: ts
Out[130]:
2014-10-07 00:00:00    0
2014-10-07 00:02:00    1
2014-10-07 00:04:00    2
2014-10-07 00:06:00    3
2014-10-07 00:08:00    4
2014-10-07 00:10:00    5
2014-10-07 00:12:00    6
2014-10-07 00:14:00    7
2014-10-07 00:16:00    8
2014-10-07 00:18:00    9
Freq: 2T, dtype: int64

[Create a value counts column and reassign back to the DataFrame](https://stackoverflow.com/q/17709270)

In [131]: df = pd.DataFrame(
 .....:    {"Color": "Red Red Red Blue".split(), "Value": [100, 150, 50, 50]}
 .....: )
 .....:

In [132]: df
Out[132]:
 Color  Value
0   Red    100
1   Red    150
2   Red     50
3  Blue     50

In [133]: df["Counts"] = df.groupby(["Color"]).transform(len)

In [134]: df
Out[134]:
 Color  Value  Counts
0   Red    100       3
1   Red    150       3
2   Red     50       3
3  Blue     50       1

[Shift groups of the values in a column based on the index](https://stackoverflow.com/q/23198053/190597)

In [135]: df = pd.DataFrame(
 .....:    {"line_race": [10, 10, 8, 10, 10, 8], "beyer": [99, 102, 103, 103, 88, 100]},
 .....:    index=[
 .....:        "Last Gunfighter",
 .....:        "Last Gunfighter",
 .....:        "Last Gunfighter",
 .....:        "Paynter",
 .....:        "Paynter",
 .....:        "Paynter",
 .....:    ],
 .....: )
 .....:

In [136]: df
Out[136]:
 line_race  beyer
Last Gunfighter         10     99
Last Gunfighter         10    102
Last Gunfighter          8    103
Paynter                 10    103
Paynter                 10     88
Paynter                  8    100

In [137]: df["beyer_shifted"] = df.groupby(level=0)["beyer"].shift(1)

In [138]: df
Out[138]:
 line_race  beyer  beyer_shifted
Last Gunfighter         10     99            NaN
Last Gunfighter         10    102           99.0
Last Gunfighter          8    103          102.0
Paynter                 10    103            NaN
Paynter                 10     88          103.0
Paynter                  8    100           88.0

[Select row with maximum value from each group](https://stackoverflow.com/q/26701849/190597)

In [139]: df = pd.DataFrame(
 .....:    {
 .....:        "host": ["other", "other", "that", "this", "this"],
 .....:        "service": ["mail", "web", "mail", "mail", "web"],
 .....:        "no": [1, 2, 1, 2, 1],
 .....:    }
 .....: ).set_index(["host", "service"])
 .....:

In [140]: mask = df.groupby(level=0).agg("idxmax")

In [141]: df_count = df.loc[mask["no"]].reset_index()

In [142]: df_count
Out[142]:
 host service  no
0  other     web   2
1   that    mail   1
2   this    mail   2

[Grouping like Python's itertools.groupby](https://stackoverflow.com/q/29142487/846892)

In [143]: df = pd.DataFrame([0, 1, 0, 1, 1, 1, 0, 1, 1], columns=["A"])

In [144]: df["A"].groupby((df["A"] != df["A"].shift()).cumsum()).groups
Out[144]: {1: [0], 2: [1], 3: [2], 4: [3, 4, 5], 5: [6], 6: [7, 8]}

In [145]: df["A"].groupby((df["A"] != df["A"].shift()).cumsum()).cumsum()
Out[145]:
0    0
1    1
2    0
3    1
4    2
5    3
6    0
7    1
8    2
Name: A, dtype: int64

### Expanding data[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#expanding-data "Permalink to this headline")

[Alignment and to-date](https://stackoverflow.com/questions/15489011/python-time-series-alignment-and-to-date-functions)

[Rolling Computation window based on values instead of counts](https://stackoverflow.com/questions/14300768/pandas-rolling-computation-with-window-based-on-values-instead-of-counts)

[Rolling Mean by Time Interval](https://stackoverflow.com/questions/15771472/pandas-rolling-mean-by-time-interval)

### Splitting[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#id2 "Permalink to this headline")

[Splitting a frame](https://stackoverflow.com/questions/13353233/best-way-to-split-a-dataframe-given-an-edge/15449992#15449992)

Create a list of dataframes, split using a delineation based on logic included in rows.

In [146]: df = pd.DataFrame(
 .....:    data={
 .....:        "Case": ["A", "A", "A", "B", "A", "A", "B", "A", "A"],
 .....:        "Data": np.random.randn(9),
 .....:    }
 .....: )
 .....:

In [147]: dfs = list(
 .....:    zip(
 .....:        *df.groupby(
 .....:            (1 * (df["Case"] == "B"))
 .....:            .cumsum()
 .....:            .rolling(window=3, min_periods=1)
 .....:            .median()
 .....:        )
 .....:    )
 .....: )[-1]
 .....:

In [148]: dfs[0]
Out[148]:
 Case      Data
0    A  0.276232
1    A -1.087401
2    A -0.673690
3    B  0.113648

In [149]: dfs[1]
Out[149]:
 Case      Data
4    A -1.478427
5    A  0.524988
6    B  0.404705

In [150]: dfs[2]
Out[150]:
 Case      Data
7    A  0.577046
8    A -1.715002

### Pivot[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#pivot "Permalink to this headline")

The [Pivot](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-pivot) docs.

[Partial sums and subtotals](https://stackoverflow.com/a/15574875)

In [151]: df = pd.DataFrame(
 .....:    data={
 .....:        "Province": ["ON", "QC", "BC", "AL", "AL", "MN", "ON"],
 .....:        "City": [
 .....:            "Toronto",
 .....:            "Montreal",
 .....:            "Vancouver",
 .....:            "Calgary",
 .....:            "Edmonton",
 .....:            "Winnipeg",
 .....:            "Windsor",
 .....:        ],
 .....:        "Sales": [13, 6, 16, 8, 4, 3, 1],
 .....:    }
 .....: )
 .....:

In [152]: table = pd.pivot_table(
 .....:    df,
 .....:    values=["Sales"],
 .....:    index=["Province"],
 .....:    columns=["City"],
 .....:    aggfunc=np.sum,
 .....:    margins=True,
 .....: )
 .....:

In [153]: table.stack("City")
Out[153]:
 Sales
Province City
AL       All         12.0
 Calgary      8.0
 Edmonton     4.0
BC       All         16.0
 Vancouver   16.0
...                   ...
All      Montreal     6.0
 Toronto     13.0
 Vancouver   16.0
 Windsor      1.0
 Winnipeg     3.0

[20 rows x 1 columns]

[Frequency table like plyr in R](https://stackoverflow.com/questions/15589354/frequency-tables-in-pandas-like-plyr-in-r)

In [154]: grades = [48, 99, 75, 80, 42, 80, 72, 68, 36, 78]

In [155]: df = pd.DataFrame(
 .....:    {
 .....:        "ID": ["x%d" % r for r in range(10)],
 .....:        "Gender": ["F", "M", "F", "M", "F", "M", "F", "M", "M", "M"],
 .....:        "ExamYear": [
 .....:            "2007",
 .....:            "2007",
 .....:            "2007",
 .....:            "2008",
 .....:            "2008",
 .....:            "2008",
 .....:            "2008",
 .....:            "2009",
 .....:            "2009",
 .....:            "2009",
 .....:        ],
 .....:        "Class": [
 .....:            "algebra",
 .....:            "stats",
 .....:            "bio",
 .....:            "algebra",
 .....:            "algebra",
 .....:            "stats",
 .....:            "stats",
 .....:            "algebra",
 .....:            "bio",
 .....:            "bio",
 .....:        ],
 .....:        "Participated": [
 .....:            "yes",
 .....:            "yes",
 .....:            "yes",
 .....:            "yes",
 .....:            "no",
 .....:            "yes",
 .....:            "yes",
 .....:            "yes",
 .....:            "yes",
 .....:            "yes",
 .....:        ],
 .....:        "Passed": ["yes" if x > 50 else "no" for x in grades],
 .....:        "Employed": [
 .....:            True,
 .....:            True,
 .....:            True,
 .....:            False,
 .....:            False,
 .....:            False,
 .....:            False,
 .....:            True,
 .....:            True,
 .....:            False,
 .....:        ],
 .....:        "Grade": grades,
 .....:    }
 .....: )
 .....:

In [156]: df.groupby("ExamYear").agg(
 .....:    {
 .....:        "Participated": lambda x: x.value_counts()["yes"],
 .....:        "Passed": lambda x: sum(x == "yes"),
 .....:        "Employed": lambda x: sum(x),
 .....:        "Grade": lambda x: sum(x) / len(x),
 .....:    }
 .....: )
 .....:
Out[156]:
 Participated  Passed  Employed      Grade
ExamYear
2007                 3       2         3  74.000000
2008                 3       3         0  68.500000
2009                 3       2         2  60.666667

[Plot pandas DataFrame with year over year data](https://stackoverflow.com/questions/30379789/plot-pandas-data-frame-with-year-over-year-data)

To create year and month cross tabulation:

In [157]: df = pd.DataFrame(
 .....:    {"value": np.random.randn(36)},
 .....:    index=pd.date_range("2011-01-01", freq="M", periods=36),
 .....: )
 .....:

In [158]: pd.pivot_table(
 .....:    df, index=df.index.month, columns=df.index.year, values="value", aggfunc="sum"
 .....: )
 .....:
Out[158]:
 2011      2012      2013
1  -1.039268 -0.968914  2.565646
2  -0.370647 -1.294524  1.431256
3  -1.157892  0.413738  1.340309
4  -1.344312  0.276662 -1.170299
5   0.844885 -0.472035 -0.226169
6   1.075770 -0.013960  0.410835
7  -0.109050 -0.362543  0.813850
8   1.643563 -0.006154  0.132003
9  -1.469388 -0.923061 -0.827317
10  0.357021  0.895717 -0.076467
11 -0.674600  0.805244 -1.187678
12 -1.776904 -1.206412  1.130127

### Apply[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#apply "Permalink to this headline")

[Rolling apply to organize - Turning embedded lists into a MultiIndex frame](https://stackoverflow.com/questions/17349981/converting-pandas-dataframe-with-categorical-values-into-binary-values)

In [159]: df = pd.DataFrame(
 .....:    data={
 .....:        "A": [[2, 4, 8, 16], [100, 200], [10, 20, 30]],
 .....:        "B": [["a", "b", "c"], ["jj", "kk"], ["ccc"]],
 .....:    },
 .....:    index=["I", "II", "III"],
 .....: )
 .....:

In [160]: def SeriesFromSubList(aList):
 .....:    return pd.Series(aList)
 .....:

In [161]: df_orgz = pd.concat(
 .....:    {ind: row.apply(SeriesFromSubList) for ind, row in df.iterrows()}
 .....: )
 .....:

In [162]: df_orgz
Out[162]:
 0     1     2     3
I   A    2     4     8  16.0
 B    a     b     c   NaN
II  A  100   200   NaN   NaN
 B   jj    kk   NaN   NaN
III A   10  20.0  30.0   NaN
 B  ccc   NaN   NaN   NaN

[Rolling apply with a DataFrame returning a Series](https://stackoverflow.com/questions/19121854/using-rolling-apply-on-a-dataframe-object)

Rolling Apply to multiple columns where function calculates a Series before a Scalar from the Series is returned

In [163]: df = pd.DataFrame(
 .....:    data=np.random.randn(2000, 2) / 10000,
 .....:    index=pd.date_range("2001-01-01", periods=2000),
 .....:    columns=["A", "B"],
 .....: )
 .....:

In [164]: df
Out[164]:
 A         B
2001-01-01 -0.000144 -0.000141
2001-01-02  0.000161  0.000102
2001-01-03  0.000057  0.000088
2001-01-04 -0.000221  0.000097
2001-01-05 -0.000201 -0.000041
...              ...       ...
2006-06-19  0.000040 -0.000235
2006-06-20 -0.000123 -0.000021
2006-06-21 -0.000113  0.000114
2006-06-22  0.000136  0.000109
2006-06-23  0.000027  0.000030

[2000 rows x 2 columns]

In [165]: def gm(df, const):
 .....:    v = ((((df["A"] + df["B"]) + 1).cumprod()) - 1) * const
 .....:    return v.iloc[-1]
 .....:

In [166]: s = pd.Series(
 .....:    {
 .....:        df.index[i]: gm(df.iloc[i: min(i + 51, len(df) - 1)], 5)
 .....:        for i in range(len(df) - 50)
 .....:    }
 .....: )
 .....:

In [167]: s
Out[167]:
2001-01-01    0.000930
2001-01-02    0.002615
2001-01-03    0.001281
2001-01-04    0.001117
2001-01-05    0.002772
 ...
2006-04-30    0.003296
2006-05-01    0.002629
2006-05-02    0.002081
2006-05-03    0.004247
2006-05-04    0.003928
Length: 1950, dtype: float64

[Rolling apply with a DataFrame returning a Scalar](https://stackoverflow.com/questions/21040766/python-pandas-rolling-apply-two-column-input-into-function/21045831#21045831)

Rolling Apply to multiple columns where function returns a Scalar (Volume Weighted Average Price)

In [168]: rng = pd.date_range(start="2014-01-01", periods=100)

In [169]: df = pd.DataFrame(
 .....:    {
 .....:        "Open": np.random.randn(len(rng)),
 .....:        "Close": np.random.randn(len(rng)),
 .....:        "Volume": np.random.randint(100, 2000, len(rng)),
 .....:    },
 .....:    index=rng,
 .....: )
 .....:

In [170]: df
Out[170]:
 Open     Close  Volume
2014-01-01 -1.611353 -0.492885    1219
2014-01-02 -3.000951  0.445794    1054
2014-01-03 -0.138359 -0.076081    1381
2014-01-04  0.301568  1.198259    1253
2014-01-05  0.276381 -0.669831    1728
...              ...       ...     ...
2014-04-06 -0.040338  0.937843    1188
2014-04-07  0.359661 -0.285908    1864
2014-04-08  0.060978  1.714814     941
2014-04-09  1.759055 -0.455942    1065
2014-04-10  0.138185 -1.147008    1453

[100 rows x 3 columns]

In [171]: def vwap(bars):
 .....:    return (bars.Close * bars.Volume).sum() / bars.Volume.sum()
 .....:

In [172]: window = 5

In [173]: s = pd.concat(
 .....:    [
 .....:        (pd.Series(vwap(df.iloc[i: i + window]), index=[df.index[i + window]]))
 .....:        for i in range(len(df) - window)
 .....:    ]
 .....: )
 .....:

In [174]: s.round(2)
Out[174]:
2014-01-06    0.02
2014-01-07    0.11
2014-01-08    0.10
2014-01-09    0.07
2014-01-10   -0.29
 ...
2014-04-06   -0.63
2014-04-07   -0.02
2014-04-08   -0.03
2014-04-09    0.34
2014-04-10    0.29
Length: 95, dtype: float64

Timeseries[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#timeseries "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------

[Between times](https://stackoverflow.com/questions/14539992/pandas-drop-rows-outside-of-time-range)

[Using indexer between time](https://stackoverflow.com/questions/17559885/pandas-dataframe-mask-based-on-index)

[Constructing a datetime range that excludes weekends and includes only certain times](https://stackoverflow.com/a/24014440)

[Vectorized Lookup](https://stackoverflow.com/questions/13893227/vectorized-look-up-of-values-in-pandas-dataframe)

[Aggregation and plotting time series](https://nipunbatra.github.io/blog/visualisation/2013/05/01/aggregation-timeseries.html)

Turn a matrix with hours in columns and days in rows into a continuous row sequence in the form of a time series. [How to rearrange a Python pandas DataFrame?](https://stackoverflow.com/questions/15432659/how-to-rearrange-a-python-pandas-dataframe)

[Dealing with duplicates when reindexing a timeseries to a specified frequency](https://stackoverflow.com/questions/22244383/pandas-df-refill-adding-two-columns-of-different-shape)

Calculate the first day of the month for each entry in a DatetimeIndex

In [175]: dates = pd.date_range("2000-01-01", periods=5)

In [176]: dates.to_period(freq="M").to_timestamp()
Out[176]:
DatetimeIndex(['2000-01-01', '2000-01-01', '2000-01-01', '2000-01-01',
 '2000-01-01'],
 dtype='datetime64[ns]', freq=None)

### Resampling[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#resampling "Permalink to this headline")

The [Resample](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-resampling) docs.

[Using Grouper instead of TimeGrouper for time grouping of values](https://stackoverflow.com/questions/15297053/how-can-i-divide-single-values-of-a-dataframe-by-monthly-averages)

[Time grouping with some missing values](https://stackoverflow.com/questions/33637312/pandas-grouper-by-frequency-with-completeness-requirement)

Valid frequency arguments to Grouper [Timeseries](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases)

[Grouping using a MultiIndex](https://stackoverflow.com/questions/41483763/pandas-timegrouper-on-multiindex)

Using TimeGrouper and another grouping to create subgroups, then apply a custom function [GH3791](https://github.com/pandas-dev/pandas/issues/3791)

[Resampling with custom periods](https://stackoverflow.com/questions/15408156/resampling-with-custom-periods)

[Resample intraday frame without adding new days](https://stackoverflow.com/questions/14898574/resample-intrday-pandas-dataframe-without-add-new-days)

[Resample minute data](https://stackoverflow.com/questions/14861023/resampling-minute-data)

[Resample with groupby](https://stackoverflow.com/q/18677271/564538)

Merge[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#merge "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------

The [Join](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merging-join) docs.

[Concatenate two dataframes with overlapping index (emulate R rbind)](https://stackoverflow.com/questions/14988480/pandas-version-of-rbind)

In [177]: rng = pd.date_range("2000-01-01", periods=6)

In [178]: df1 = pd.DataFrame(np.random.randn(6, 3), index=rng, columns=["A", "B", "C"])

In [179]: df2 = df1.copy()

Depending on df construction, `ignore_index` may be needed

In [180]: df = pd.concat([df1, df2], ignore_index=True)

In [181]: df
Out[181]:
 A         B         C
0  -0.870117 -0.479265 -0.790855
1   0.144817  1.726395 -0.464535
2  -0.821906  1.597605  0.187307
3  -0.128342 -1.511638 -0.289858
4   0.399194 -1.430030 -0.639760
5   1.115116 -2.012600  1.810662
6  -0.870117 -0.479265 -0.790855
7   0.144817  1.726395 -0.464535
8  -0.821906  1.597605  0.187307
9  -0.128342 -1.511638 -0.289858
10  0.399194 -1.430030 -0.639760
11  1.115116 -2.012600  1.810662

Self Join of a DataFrame [GH2996](https://github.com/pandas-dev/pandas/issues/2996)

In [182]: df = pd.DataFrame(
 .....:    data={
 .....:        "Area": ["A"] * 5 + ["C"] * 2,
 .....:        "Bins": [110] * 2 + [160] * 3 + [40] * 2,
 .....:        "Test_0": [0, 1, 0, 1, 2, 0, 1],
 .....:        "Data": np.random.randn(7),
 .....:    }
 .....: )
 .....:

In [183]: df
Out[183]:
 Area  Bins  Test_0      Data
0    A   110       0 -0.433937
1    A   110       1 -0.160552
2    A   160       0  0.744434
3    A   160       1  1.754213
4    A   160       2  0.000850
5    C    40       0  0.342243
6    C    40       1  1.070599

In [184]: df["Test_1"] = df["Test_0"] - 1

In [185]: pd.merge(
 .....:    df,
 .....:    df,
 .....:    left_on=["Bins", "Area", "Test_0"],
 .....:    right_on=["Bins", "Area", "Test_1"],
 .....:    suffixes=("_L", "_R"),
 .....: )
 .....:
Out[185]:
 Area  Bins  Test_0_L    Data_L  Test_1_L  Test_0_R    Data_R  Test_1_R
0    A   110         0 -0.433937        -1         1 -0.160552         0
1    A   160         0  0.744434        -1         1  1.754213         0
2    A   160         1  1.754213         0         2  0.000850         1
3    C    40         0  0.342243        -1         1  1.070599         0

[How to set the index and join](https://stackoverflow.com/questions/14341805/pandas-merge-pd-merge-how-to-set-the-index-and-join)

[KDB like asof join](https://stackoverflow.com/questions/12322289/kdb-like-asof-join-for-timeseries-data-in-pandas/12336039#12336039)

[Join with a criteria based on the values](https://stackoverflow.com/questions/15581829/how-to-perform-an-inner-or-outer-join-of-dataframes-with-pandas-on-non-simplisti)

[Using searchsorted to merge based on values inside a range](https://stackoverflow.com/questions/25125626/pandas-merge-with-logic/2512764)

Plotting[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#plotting "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------

The [Plotting](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#visualization) docs.

[Make Matplotlib look like R](https://stackoverflow.com/questions/14349055/making-matplotlib-graphs-look-like-r-by-default)

[Setting x-axis major and minor labels](https://stackoverflow.com/questions/12945971/pandas-timeseries-plot-setting-x-axis-major-and-minor-ticks-and-labels)

[Plotting multiple charts in an IPython Jupyter notebook](https://stackoverflow.com/questions/16392921/make-more-than-one-chart-in-same-ipython-notebook-cell)

[Creating a multi-line plot](https://stackoverflow.com/questions/16568964/make-a-multiline-plot-from-csv-file-in-matplotlib)

[Plotting a heatmap](https://stackoverflow.com/questions/17050202/plot-timeseries-of-histograms-in-python)

[Annotate a time-series plot](https://stackoverflow.com/questions/11067368/annotate-time-series-plot-in-matplotlib)

[Annotate a time-series plot #2](https://stackoverflow.com/questions/17891493/annotating-points-from-a-pandas-dataframe-in-matplotlib-plot)

[Generate Embedded plots in excel files using Pandas, Vincent and xlsxwriter](https://pandas-xlsxwriter-charts.readthedocs.io/)

[Boxplot for each quartile of a stratifying variable](https://stackoverflow.com/questions/23232989/boxplot-stratified-by-column-in-python-pandas)

In [186]: df = pd.DataFrame(
 .....:    {
 .....:        "stratifying_var": np.random.uniform(0, 100, 20),
 .....:        "price": np.random.normal(100, 5, 20),
 .....:    }
 .....: )
 .....:

In [187]: df["quartiles"] = pd.qcut(
 .....:    df["stratifying_var"], 4, labels=["0-25%", "25-50%", "50-75%", "75-100%"]
 .....: )
 .....:

In [188]: df.boxplot(column="price", by="quartiles")
Out[188]: <AxesSubplot:title={'center':'price'}, xlabel='quartiles'>

![../_images/quartile_boxplot.png](https://pandas.pydata.org/pandas-docs/stable/_images/quartile_boxplot.png)

Data in/out[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#data-in-out "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

[Performance comparison of SQL vs HDF5](https://stackoverflow.com/q/16628329)

### CSV[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#csv "Permalink to this headline")

The [CSV](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table) docs

[read_csv in action](https://wesmckinney.com/blog/update-on-upcoming-pandas-v0-10-new-file-parser-other-performance-wins/)

[appending to a csv](https://stackoverflow.com/questions/17134942/pandas-dataframe-output-end-of-csv)

[Reading a csv chunk-by-chunk](https://stackoverflow.com/questions/11622652/large-persistent-dataframe-in-pandas/12193309#12193309)

[Reading only certain rows of a csv chunk-by-chunk](https://stackoverflow.com/questions/19674212/pandas-data-frame-select-rows-and-clear-memory)

[Reading the first few lines of a frame](https://stackoverflow.com/questions/15008970/way-to-read-first-few-lines-for-pandas-dataframe)

Reading a file that is compressed but not by `gzip/bz2` (the native compressed formats which `read_csv`understands). This example shows a `WinZipped` file, but is a general application of opening the file within a context manager and using that handle to read. [See here](https://stackoverflow.com/questions/17789907/pandas-convert-winzipped-csv-file-to-data-frame)

[Inferring dtypes from a file](https://stackoverflow.com/questions/15555005/get-inferred-dataframe-types-iteratively-using-chunksize)

Dealing with bad lines [GH2886](https://github.com/pandas-dev/pandas/issues/2886)

[Write a multi-row index CSV without writing duplicates](https://stackoverflow.com/questions/17349574/pandas-write-multiindex-rows-with-to-csv)

#### Reading multiple files to create a single DataFrame[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#reading-multiple-files-to-create-a-single-dataframe "Permalink to this headline")

The best way to combine multiple files into a single DataFrame is to read the individual frames one by one, put all of the individual frames into a list, and then combine the frames in the list using `pd.concat()`:

In [189]: for i in range(3):
 .....:    data = pd.DataFrame(np.random.randn(10, 4))
 .....:    data.to_csv("file_{}.csv".format(i))
 .....:

In [190]: files = ["file_0.csv", "file_1.csv", "file_2.csv"]

In [191]: result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

You can use the same approach to read all files matching a pattern. Here is an example using `glob`:

In [192]: import glob

In [193]: import os

In [194]: files = glob.glob("file_*.csv")

In [195]: result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

Finally, this strategy will work with the other `pd.read_*(...)` functions described in the [io docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io).

#### Parsing date components in multi-columns[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#parsing-date-components-in-multi-columns "Permalink to this headline")

Parsing date components in multi-columns is faster with a format

In [196]: i = pd.date_range("20000101", periods=10000)

In [197]: df = pd.DataFrame({"year": i.year, "month": i.month, "day": i.day})

In [198]: df.head()
Out[198]:
 year  month  day
0  2000      1    1
1  2000      1    2
2  2000      1    3
3  2000      1    4
4  2000      1    5

In [199]: %timeit pd.to_datetime(df.year * 10000 + df.month * 100 + df.day, format='%Y%m%d')
 .....: ds = df.apply(lambda x: "%04d%02d%02d" % (x["year"], x["month"], x["day"]), axis=1)
 .....: ds.head()
 .....: %timeit pd.to_datetime(ds)
 .....:
8.7 ms +- 765 us per loop (mean +- std. dev. of 7 runs, 100 loops each)
2.1 ms +- 419 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

#### Skip row between header and data[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#skip-row-between-header-and-data "Permalink to this headline")

In [200]: data = """;;;;
 .....: ;;;;
 .....: ;;;;
 .....: ;;;;
 .....: ;;;;
 .....: ;;;;
 .....: ;;;;
 .....: ;;;;
 .....: ;;;;
 .....: ;;;;
 .....: date;Param1;Param2;Param4;Param5
 .....:    ;m²;°C;m²;m
 .....: ;;;;
 .....: 01.01.1990 00:00;1;1;2;3
 .....: 01.01.1990 01:00;5;3;4;5
 .....: 01.01.1990 02:00;9;5;6;7
 .....: 01.01.1990 03:00;13;7;8;9
 .....: 01.01.1990 04:00;17;9;10;11
 .....: 01.01.1990 05:00;21;11;12;13
 .....: """
 .....:

##### Option 1: pass rows explicitly to skip rows[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#option-1-pass-rows-explicitly-to-skip-rows "Permalink to this headline")

In [201]: from io import StringIO

In [202]: pd.read_csv(
 .....:    StringIO(data),
 .....:    sep=";",
 .....:    skiprows=[11, 12],
 .....:    index_col=0,
 .....:    parse_dates=True,
 .....:    header=10,
 .....: )
 .....:
Out[202]:
 Param1  Param2  Param4  Param5
date
1990-01-01 00:00:00       1       1       2       3
1990-01-01 01:00:00       5       3       4       5
1990-01-01 02:00:00       9       5       6       7
1990-01-01 03:00:00      13       7       8       9
1990-01-01 04:00:00      17       9      10      11
1990-01-01 05:00:00      21      11      12      13

##### Option 2: read column names and then data[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#option-2-read-column-names-and-then-data "Permalink to this headline")

In [203]: pd.read_csv(StringIO(data), sep=";", header=10, nrows=10).columns
Out[203]: Index(['date', 'Param1', 'Param2', 'Param4', 'Param5'], dtype='object')

In [204]: columns = pd.read_csv(StringIO(data), sep=";", header=10, nrows=10).columns

In [205]: pd.read_csv(
 .....:    StringIO(data), sep=";", index_col=0, header=12, parse_dates=True, names=columns
 .....: )
 .....:
Out[205]:
 Param1  Param2  Param4  Param5
date
1990-01-01 00:00:00       1       1       2       3
1990-01-01 01:00:00       5       3       4       5
1990-01-01 02:00:00       9       5       6       7
1990-01-01 03:00:00      13       7       8       9
1990-01-01 04:00:00      17       9      10      11
1990-01-01 05:00:00      21      11      12      13

### SQL[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#sql "Permalink to this headline")

The [SQL](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-sql) docs

[Reading from databases with SQL](https://stackoverflow.com/questions/10065051/python-pandas-and-databases-like-mysql)

### Excel[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#excel "Permalink to this headline")

The [Excel](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-excel) docs

[Reading from a filelike handle](https://stackoverflow.com/questions/15588713/sheets-of-excel-workbook-from-a-url-into-a-pandas-dataframe)

[Modifying formatting in XlsxWriter output](https://pbpython.com/improve-pandas-excel-output.html)

Loading only visible sheets [GH19842#issuecomment-892150745](https://github.com/pandas-dev/pandas/issues/19842#issuecomment-892150745)

### HTML[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#html "Permalink to this headline")

[Reading HTML tables from a server that cannot handle the default request header](https://stackoverflow.com/a/18939272/564538)

### HDFStore[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#hdfstore "Permalink to this headline")

The [HDFStores](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-hdf5) docs

[Simple queries with a Timestamp Index](https://stackoverflow.com/questions/13926089/selecting-columns-from-pandas-hdfstore-table)

Managing heterogeneous data using a linked multiple table hierarchy [GH3032](https://github.com/pandas-dev/pandas/issues/3032)

[Merging on-disk tables with millions of rows](https://stackoverflow.com/questions/14614512/merging-two-tables-with-millions-of-rows-in-python/14617925#14617925)

[Avoiding inconsistencies when writing to a store from multiple processes/threads](https://stackoverflow.com/a/29014295/2858145)

De-duplicating a large store by chunks, essentially a recursive reduction operation. Shows a function for taking in data from csv file and creating a store by chunks, with date parsing as well. [See here](https://stackoverflow.com/questions/16110252/need-to-compare-very-large-files-around-1-5gb-in-python/16110391#16110391)

[Creating a store chunk-by-chunk from a csv file](https://stackoverflow.com/questions/20428355/appending-column-to-frame-of-hdf-file-in-pandas/20428786#20428786)

[Appending to a store, while creating a unique index](https://stackoverflow.com/questions/16997048/how-does-one-append-large-amounts-of-data-to-a-pandas-hdfstore-and-get-a-natural/16999397#16999397)

[Large Data work flows](https://stackoverflow.com/q/14262433)

[Reading in a sequence of files, then providing a global unique index to a store while appending](https://stackoverflow.com/questions/16997048/how-does-one-append-large-amounts-of-data-to-a-pandas-hdfstore-and-get-a-natural)

[Groupby on a HDFStore with low group density](https://stackoverflow.com/questions/15798209/pandas-group-by-query-on-large-data-in-hdfstore)

[Groupby on a HDFStore with high group density](https://stackoverflow.com/questions/25459982/trouble-with-grouby-on-millions-of-keys-on-a-chunked-file-in-python-pandas/25471765#25471765)

[Hierarchical queries on a HDFStore](https://stackoverflow.com/questions/22777284/improve-query-performance-from-a-large-hdfstore-table-with-pandas/22820780#22820780)

[Counting with a HDFStore](https://stackoverflow.com/questions/20497897/converting-dict-of-dicts-into-pandas-dataframe-memory-issues)

[Troubleshoot HDFStore exceptions](https://stackoverflow.com/questions/15488809/how-to-trouble-shoot-hdfstore-exception-cannot-find-the-correct-atom-type)

[Setting min_itemsize with strings](https://stackoverflow.com/questions/15988871/hdfstore-appendstring-dataframe-fails-when-string-column-contents-are-longer)

[Using ptrepack to create a completely-sorted-index on a store](https://stackoverflow.com/questions/17893370/ptrepack-sortby-needs-full-index)

Storing Attributes to a group node

In [206]: df = pd.DataFrame(np.random.randn(8, 3))

In [207]: store = pd.HDFStore("test.h5")

In [208]: store.put("df", df)

# you can store an arbitrary Python object via pickle
In [209]: store.get_storer("df").attrs.my_attribute = {"A": 10}

In [210]: store.get_storer("df").attrs.my_attribute
Out[210]: {'A': 10}

You can create or load a HDFStore in-memory by passing the `driver` parameter to PyTables. Changes are only written to disk when the HDFStore is closed.

In [211]: store = pd.HDFStore("test.h5", "w", driver="H5FD_CORE")

In [212]: df = pd.DataFrame(np.random.randn(8, 3))

In [213]: store["test"] = df

# only after closing the store, data is written to disk:
In [214]: store.close()

### Binary files[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#binary-files "Permalink to this headline")

pandas readily accepts NumPy record arrays, if you need to read in a binary file consisting of an array of C structs. For example, given this C program in a file called `main.c` compiled with `gcc main.c-std=gnu99` on a 64-bit machine,

#include  <stdio.h>
#include  <stdint.h>

typedef  struct  _Data
{
  int32_t  count;
  double  avg;
  float  scale;
}  Data;

int  main(int  argc,  const  char  *argv[])
{
  size_t  n  =  10;
  Data  d[n];

  for  (int  i  =  0;  i  <  n;  ++i)
  {
  d[i].count  =  i;
  d[i].avg  =  i  +  1.0;
  d[i].scale  =  (float)  i  +  2.0f;
  }

  FILE  *file  =  fopen("binary.dat",  "wb");
  fwrite(&d,  sizeof(Data),  n,  file);
  fclose(file);

  return  0;
}

the following Python code will read the binary file `'binary.dat'` into a pandas `DataFrame`, where each element of the struct corresponds to a column in the frame:

names = "count", "avg", "scale"

# note that the offsets are larger than the size of the type because of
# struct padding
offsets = 0, 8, 16
formats = "i4", "f8", "f4"
dt = np.dtype({"names": names, "offsets": offsets, "formats": formats}, align=True)
df = pd.DataFrame(np.fromfile("binary.dat", dt))

Note

The offsets of the structure elements may be different depending on the architecture of the machine on which the file was created. Using a raw binary file format like this for general data storage is not recommended, as it is not cross platform. We recommended either HDF5 or parquet, both of which are supported by pandas' IO facilities.

Computation[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#computation "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

[Numerical integration (sample-based) of a time series](https://nbviewer.ipython.org/gist/metakermit/5720498)

### Correlation[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#correlation "Permalink to this headline")

Often it's useful to obtain the lower (or upper) triangular form of a correlation matrix calculated from [`DataFrame.corr()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr "pandas.DataFrame.corr"). This can be achieved by passing a boolean mask to `where` as follows:

In [215]: df = pd.DataFrame(np.random.random(size=(100, 5)))

In [216]: corr_mat = df.corr()

In [217]: mask = np.tril(np.ones_like(corr_mat, dtype=np.bool_), k=-1)

In [218]: corr_mat.where(mask)
Out[218]:
 0         1         2        3   4
0       NaN       NaN       NaN      NaN NaN
1 -0.079861       NaN       NaN      NaN NaN
2 -0.236573  0.183801       NaN      NaN NaN
3 -0.013795 -0.051975  0.037235      NaN NaN
4 -0.031974  0.118342 -0.073499 -0.02063 NaN

The `method` argument within `DataFrame.corr` can accept a callable in addition to the named correlation types. Here we compute the [distance correlation](https://en.wikipedia.org/wiki/Distance_correlation) matrix for a `DataFrame` object.

In [219]: def distcorr(x, y):
 .....:    n = len(x)
 .....:    a = np.zeros(shape=(n, n))
 .....:    b = np.zeros(shape=(n, n))
 .....:    for i in range(n):
 .....:        for j in range(i + 1, n):
 .....:            a[i, j] = abs(x[i] - x[j])
 .....:            b[i, j] = abs(y[i] - y[j])
 .....:    a += a.T
 .....:    b += b.T
 .....:    a_bar = np.vstack([np.nanmean(a, axis=0)] * n)
 .....:    b_bar = np.vstack([np.nanmean(b, axis=0)] * n)
 .....:    A = a - a_bar - a_bar.T + np.full(shape=(n, n), fill_value=a_bar.mean())
 .....:    B = b - b_bar - b_bar.T + np.full(shape=(n, n), fill_value=b_bar.mean())
 .....:    cov_ab = np.sqrt(np.nansum(A * B)) / n
 .....:    std_a = np.sqrt(np.sqrt(np.nansum(A ** 2)) / n)
 .....:    std_b = np.sqrt(np.sqrt(np.nansum(B ** 2)) / n)
 .....:    return cov_ab / std_a / std_b
 .....:

In [220]: df = pd.DataFrame(np.random.normal(size=(100, 3)))

In [221]: df.corr(method=distcorr)
Out[221]:
 0         1         2
0  1.000000  0.197613  0.216328
1  0.197613  1.000000  0.208749
2  0.216328  0.208749  1.000000

Timedeltas[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#timedeltas "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------

The [Timedeltas](https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html#timedeltas-timedeltas) docs.

[Using timedeltas](https://github.com/pandas-dev/pandas/pull/2899)

In [222]: import datetime

In [223]: s = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))

In [224]: s - s.max()
Out[224]:
0   -2 days
1   -1 days
2    0 days
dtype: timedelta64[ns]

In [225]: s.max() - s
Out[225]:
0   2 days
1   1 days
2   0 days
dtype: timedelta64[ns]

In [226]: s - datetime.datetime(2011, 1, 1, 3, 5)
Out[226]:
0   364 days 20:55:00
1   365 days 20:55:00
2   366 days 20:55:00
dtype: timedelta64[ns]

In [227]: s + datetime.timedelta(minutes=5)
Out[227]:
0   2012-01-01 00:05:00
1   2012-01-02 00:05:00
2   2012-01-03 00:05:00
dtype: datetime64[ns]

In [228]: datetime.datetime(2011, 1, 1, 3, 5) - s
Out[228]:
0   -365 days +03:05:00
1   -366 days +03:05:00
2   -367 days +03:05:00
dtype: timedelta64[ns]

In [229]: datetime.timedelta(minutes=5) + s
Out[229]:
0   2012-01-01 00:05:00
1   2012-01-02 00:05:00
2   2012-01-03 00:05:00
dtype: datetime64[ns]

[Adding and subtracting deltas and dates](https://stackoverflow.com/questions/16385785/add-days-to-dates-in-dataframe)

In [230]: deltas = pd.Series([datetime.timedelta(days=i) for i in range(3)])

In [231]: df = pd.DataFrame({"A": s, "B": deltas})

In [232]: df
Out[232]:
 A      B
0 2012-01-01 0 days
1 2012-01-02 1 days
2 2012-01-03 2 days

In [233]: df["New Dates"] = df["A"] + df["B"]

In [234]: df["Delta"] = df["A"] - df["New Dates"]

In [235]: df
Out[235]:
 A      B  New Dates   Delta
0 2012-01-01 0 days 2012-01-01  0 days
1 2012-01-02 1 days 2012-01-03 -1 days
2 2012-01-03 2 days 2012-01-05 -2 days

In [236]: df.dtypes
Out[236]:
A             datetime64[ns]
B            timedelta64[ns]
New Dates     datetime64[ns]
Delta        timedelta64[ns]
dtype: object

[Another example](https://stackoverflow.com/questions/15683588/iterating-through-a-pandas-dataframe)

Values can be set to NaT using np.nan, similar to datetime

In [237]: y = s - s.shift()

In [238]: y
Out[238]:
0      NaT
1   1 days
2   1 days
dtype: timedelta64[ns]

In [239]: y[1] = np.nan

In [240]: y
Out[240]:
0      NaT
1      NaT
2   1 days
dtype: timedelta64[ns]

Creating example data[](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#creating-example-data "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------

To create a dataframe from every combination of some given values, like R's `expand.grid()` function, we can create a dict where the keys are column names and the values are lists of the data values:

In [241]: def expand_grid(data_dict):
 .....:    rows = itertools.product(*data_dict.values())
 .....:    return pd.DataFrame.from_records(rows, columns=data_dict.keys())
 .....:

In [242]: df = expand_grid(
 .....:    {"height": [60, 70], "weight": [100, 140, 180], "sex": ["Male", "Female"]}
 .....: )
 .....:

In [243]: df
Out[243]:
 height  weight     sex
0       60     100    Male
1       60     100  Female
2       60     140    Male
3       60     140  Female
4       60     180    Male
5       60     180  Female
6       70     100    Male
7       70     100  Female
8       70     140    Male
9       70     140  Female
10      70     180    Male
11      70     180  Female

[

Previous

Frequently Asked Questions (FAQ)

](https://pandas.pydata.org/pandas-docs/stable/user_guide/gotchas.html "previous page")[

Next

API reference

](https://pandas.pydata.org/pandas-docs/stable/reference/index.html "next page")

© Copyright 2008-2022, the pandas development team.

Created using [Sphinx](http://sphinx-doc.org/) 4.4.0.