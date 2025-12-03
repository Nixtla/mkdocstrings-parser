def test_make_future_dataframe(setup_parser):
    fn = """::: hierarchicalforecast.utils.make_future_dataframe"""
    output = setup_parser.process_markdown(fn)
    assert output == """### `make_future_dataframe`

```python
make_future_dataframe(df, freq, h, id_col='unique_id', time_col='ds')
```

Create future dataframe for forecasting.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`df` | <code>[Frame](#narwhals.typing.Frame)</code> | Dataframe with ids, times and values for the exogenous regressors. | *required*
`freq` | <code>[Union](#typing.Union)\[[str](#str), [int](#int)\]</code> | Frequency of the data. Must be a valid pandas or polars offset alias, or an integer. | *required*
`h` | <code>[int](#int)</code> | Forecast horizon. | *required*
`id_col` | <code>[str](#str)</code> | Column that identifies each serie. Default is 'unique_id'. | <code>'unique_id'</code>
`time_col` | <code>[str](#str)</code> | Column that identifies each timestep, its values can be timestamps or integers. Default is 'ds'. | <code>'ds'</code>

**Returns:**

Name | Type | Description
---- | ---- | -----------
`FrameT` | <code>[FrameT](#narwhals.typing.FrameT)</code> | DataFrame with future values.
"""

def test_evaluate(setup_parser):
    fn = "::: hierarchicalforecast.evaluation.evaluate"
    output = setup_parser.process_markdown(fn)
    assert output == """### `evaluate`

```python
evaluate(df, metrics, tags, models=None, train_df=None, level=None, id_col='unique_id', time_col='ds', target_col='y', agg_fn='mean', benchmark=None)
```

Evaluate hierarchical forecast using different metrics.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`df` | <code>pandas, polars, dask or spark DataFrame</code> | Forecasts to evaluate. Must have `id_col`, `time_col`, `target_col` and models' predictions. | *required*
`metrics` | <code>list of callable</code> | Functions with arguments `df`, `models`, `id_col`, `target_col` and optionally `train_df`. | *required*
`tags` | <code>[dict](#dict)</code> | Each key is a level in the hierarchy and its value contains tags associated to that level. Each key is a level in the hierarchy and its value contains tags associated to that level. | *required*
`models` | <code>list of str</code> | Names of the models to evaluate. If `None` will use every column in the dataframe after removing id, time and target. | <code>None</code>
`train_df` | <code>pandas, polars, dask or spark DataFrame</code> | Training set. Used to evaluate metrics such as `mase`. | <code>None</code>
`level` | <code>list of int</code> | Prediction interval levels. Used to compute losses that rely on quantiles. | <code>None</code>
`id_col` | <code>[str](#str)</code> | Column that identifies each serie. | <code>'unique_id'</code>
`time_col` | <code>[str](#str)</code> | Column that identifies each timestep, its values can be timestamps or integers. | <code>'ds'</code>
`target_col` | <code>[str](#str)</code> | Column that contains the target. | <code>'y'</code>
`agg_fn` | <code>[str](#str)</code> | Statistic to compute on the scores by id to reduce them to a single number. | <code>'mean'</code>
`benchmark` | <code>[str](#str)</code> | If passed, evaluators are scaled by the error of this benchmark model. | <code>None</code>

**Returns:**

Type | Description
---- | -----------
<code>[FrameT](#narwhals.typing.FrameT)</code> | pandas, polars DataFrame: Metrics with one row per (id, metric) combination and one column per model. If `agg_fn` is not `None`, there is only one row per metric.
"""

def test_permbu(setup_parser):
    fn = """::: hierarchicalforecast.probabilistic_methods.PERMBU
    handler: python
    options:
      docstring_style: google
      members:
        - get_samples
      heading_level: 3
      show_root_heading: true
      show_source: true
"""
    output = setup_parser.process_markdown(fn)
    assert output == """### `PERMBU`

```python
PERMBU(S, tags, y_hat, y_insample, y_hat_insample, sigmah, num_samples=None, seed=0, P=None)
```

PERMBU Probabilistic Reconciliation Class.

The PERMBU method leverages empirical bottom-level marginal distributions
with empirical copula functions (describing bottom-level dependencies) to
generate the distribution of aggregate-level distributions using BottomUp
reconciliation. The sample reordering technique in the PERMBU method reinjects
multivariate dependencies into independent bottom-level samples.

```
Algorithm:
1.   For all series compute conditional marginals distributions.
2.   Compute residuals $\hat{\epsilon}_{i,t}$ and obtain rank permutations.
2.   Obtain K-sample from the bottom-level series predictions.
3.   Apply recursively through the hierarchical structure:<br>
    3.1.   For a given aggregate series $i$ and its children series:<br>
    3.2.   Obtain children's empirical joint using sample reordering copula.<br>
    3.2.   From the children's joint obtain the aggregate series's samples.
```

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`S` | <code>[Union](#typing.Union)\[[ndarray](#numpy.ndarray), [spmatrix](#scipy.sparse.spmatrix)\]</code> | np.array, summing matrix of size (`base`, `bottom`). | *required*
`tags` | <code>[dict](#dict)\[[str](#str), [ndarray](#numpy.ndarray)\]</code> | Each key is a level and each value its `S` indices. | *required*
`y_insample` | <code>[ndarray](#numpy.ndarray)</code> | Insample values of size (`base`, `insample_size`). | *required*
`y_hat_insample` | <code>[ndarray](#numpy.ndarray)</code> | Insample point forecasts of size (`base`, `insample_size`). | *required*
`sigmah` | <code>[ndarray](#numpy.ndarray)</code> | np.array, forecast standard dev. of size (`base`, `horizon`). | *required*
`num_samples` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | int, number of normal prediction samples generated. | <code>None</code>
`seed` | <code>[int](#int)</code> | int, random seed for numpy generator's replicability. | <code>0</code>

<details class="references" open markdown="1">
<summary>References</summary>

- [Taieb, Souhaib Ben and Taylor, James W and Hyndman, Rob J. (2017). "Coherent probabilistic forecasts for hierarchical time series. International conference on machine learning ICML."](https://proceedings.mlr.press/v70/taieb17a.html)

</details>

#### `PERMBU.get_samples`

```python
get_samples(num_samples=None)
```

PERMBU Sample Reconciliation Method.

Applies PERMBU reconciliation method as defined by Taieb et. al 2017.
Generating independent base prediction samples, restoring its multivariate
dependence using estimated copula with reordering and applying the BottomUp
aggregation to the new samples.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`num_samples` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | int, number of samples generated from coherent distribution. | <code>None</code>

**Returns:**

Name | Type | Description
---- | ---- | -----------
`samples` | | Coherent samples of size (`base`, `horizon`, `num_samples`).
"""

def test_bottomup(setup_parser):
    fn = """::: hierarchicalforecast.methods.BottomUp
    handler: python
    options:
      docstring_style: google
      members:
        - fit
        - predict
        - fit_predict
        - sample
      inherited_members: false
      heading_level: 3
      show_root_heading: true
      show_source: true"""
    output = setup_parser.process_markdown(fn)
    assert output == """### `BottomUp`

Bases: <code>[HReconciler](#hierarchicalforecast.methods.HReconciler)</code>

Bottom Up Reconciliation Class.

The most basic hierarchical reconciliation is performed using an Bottom-Up strategy. It was proposed for
the first time by Orcutt in 1968.
The corresponding hierarchical "projection" matrix is defined as:
$$
\\mathbf{P}_{\\text{BU}} = \[\\mathbf{0}_{\\mathrm{[b],[a]}};|;\\mathbf{I}\_{\\mathrm{[b][b]}}\]
$$

<details class="references" open markdown="1">
<summary>References</summary>

- [Orcutt, G.H., Watts, H.W., & Edwards, J.B.(1968). "Data aggregation and information loss". The American Economic Review, 58 , 773(787)](http://www.jstor.org/stable/1815532).

</details>

#### `BottomUp.fit`

```python
fit(S, y_hat, idx_bottom, y_insample=None, y_hat_insample=None, sigmah=None, intervals_method=None, num_samples=None, seed=None, tags=None)
```

Bottom Up Fit Method.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`S` | <code>[ndarray](#numpy.ndarray)</code> | Summing matrix of size (`base`, `bottom`). | *required*
`y_hat` | <code>[ndarray](#numpy.ndarray)</code> | Forecast values of size (`base`, `horizon`). | *required*
`idx_bottom` | <code>[ndarray](#numpy.ndarray)</code> | Indices corresponding to the bottom level of `S`, size (`bottom`). | *required*
`y_insample` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | In-sample values of size (`base`, `horizon`). Default is None. | <code>None</code>
`y_hat_insample` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | In-sample forecast values of size (`base`, `horizon`). Default is None. | <code>None</code>
`sigmah` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | Estimated standard deviation of the conditional marginal distribution. Default is None. | <code>None</code>
`intervals_method` | <code>[Optional](#typing.Optional)\[[str](#str)\]</code> | Sampler for prediction intervals, one of `normality`, `bootstrap`, `permbu`. Default is None. | <code>None</code>
`num_samples` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | Number of samples for probabilistic coherent distribution. Default is None. | <code>None</code>
`seed` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | Seed for reproducibility. Default is None. | <code>None</code>
`tags` | <code>[Optional](#typing.Optional)\[[dict](#dict)\[[str](#str), [ndarray](#numpy.ndarray)\]\]</code> | Tags for hierarchical structure. Default is None. | <code>None</code>

**Returns:**

Name | Type | Description
---- | ---- | -----------
`BottomUp` | | object, fitted reconciler.

#### `BottomUp.fit_predict`

```python
fit_predict(S, y_hat, idx_bottom, y_insample=None, y_hat_insample=None, sigmah=None, level=None, intervals_method=None, num_samples=None, seed=None, tags=None)
```

BottomUp Reconciliation Method.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`S` | <code>[ndarray](#numpy.ndarray)</code> | Summing matrix of size (`base`, `bottom`). | *required*
`y_hat` | <code>[ndarray](#numpy.ndarray)</code> | Forecast values of size (`base`, `horizon`). | *required*
`idx_bottom` | <code>[ndarray](#numpy.ndarray)</code> | Indices corresponding to the bottom level of `S`, size (`bottom`). | *required*
`y_insample` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | In-sample values of size (`base`, `insample_size`). Default is None. | <code>None</code>
`y_hat_insample` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | In-sample forecast values of size (`base`, `insample_size`). Default is None. | <code>None</code>
`sigmah` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | Estimated standard deviation of the conditional marginal distribution. Default is None. | <code>None</code>
`level` | <code>[Optional](#typing.Optional)\[[list](#list)\[[int](#int)\]\]</code> | float list 0-100, confidence levels for prediction intervals. Default is None. | <code>None</code>
`intervals_method` | <code>[Optional](#typing.Optional)\[[str](#str)\]</code> | Sampler for prediction intervals, one of `normality`, `bootstrap`, `permbu`. Default is None. | <code>None</code>
`num_samples` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | Number of samples for probabilistic coherent distribution. Default is None. | <code>None</code>
`seed` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | Seed for reproducibility. Default is None. | <code>None</code>
`tags` | <code>[Optional](#typing.Optional)\[[dict](#dict)\[[str](#str), [ndarray](#numpy.ndarray)\]\]</code> | Tags for hierarchical structure. Default is None. | <code>None</code>

**Returns:**

Name | Type | Description
---- | ---- | -----------
`dict` | | y_tilde: Reconciliated y_hat using the Bottom Up approach.
"""

def test_topdown(setup_parser):
    fn = """::: hierarchicalforecast.methods.TopDown
    handler: python
    options:
      docstring_style: google
      members:
        - fit
        - predict
        - fit_predict
        - sample
      inherited_members: false
      heading_level: 3
      show_root_heading: true
      show_source: true"""
    output = setup_parser.process_markdown(fn)
    assert output == """### `TopDown`

```python
TopDown(method)
```

Bases: <code>[HReconciler](#hierarchicalforecast.methods.HReconciler)</code>

Top Down Reconciliation Class.

The Top Down hierarchical reconciliation method, distributes the total aggregate predictions and decomposes
it down the hierarchy using proportions $\mathbf{p}\_{\mathrm{[b]}}$ that can be actual historical values
or estimated.

$$\mathbf{P}=\[\mathbf{p}_{\mathrm{[b]}};|;\mathbf{0}_{\mathrm{[b][a,b;-1]}}\]$$

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`method` | <code>[str](#str)</code> | One of `forecast_proportions`, `average_proportions` and `proportion_averages`. | *required*

<details class="references" open markdown="1">
<summary>References</summary>

- [CW. Gross (1990). "Disaggregation methods to expedite product line forecasting". Journal of Forecasting, 9 , 233-254. doi:10.1002/for.3980090304](https://onlinelibrary.wiley.com/doi/abs/10.1002/for.3980090304).
- [G. Fliedner (1999). "An investigation of aggregate variable time series forecast strategies with specific subaggregate time series statistical correlation". Computers and Operations Research, 26 , 1133-1149. doi:10.1016/S0305-0548(99)00017-9](<https://doi.org/10.1016/S0305-0548(99)00017-9>).

</details>

#### `TopDown.fit`

```python
fit(S, y_hat, y_insample, y_hat_insample=None, sigmah=None, intervals_method=None, num_samples=None, seed=None, tags=None, idx_bottom=None)
```

TopDown Fit Method.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`S` | | Summing matrix of size (`base`, `bottom`). | *required*
`y_hat` | | Forecast values of size (`base`, `horizon`). | *required*
`y_insample` | <code>[ndarray](#numpy.ndarray)</code> | Insample values of size (`base`, `insample_size`). Optional for `forecast_proportions` method. | *required*
`y_hat_insample` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | Insample forecast values of size (`base`, `insample_size`). Optional for `forecast_proportions` method. | <code>None</code>
`sigmah` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | Estimated standard deviation of the conditional marginal distribution. | <code>None</code>
`interval_method` | | Sampler for prediction intervals, one of `normality`, `bootstrap`, `permbu`. | *required*
`num_samples` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | Number of samples for probabilistic coherent distribution. | <code>None</code>
`seed` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | Seed for reproducibility. | <code>None</code>
`tags` | <code>[Optional](#typing.Optional)\[[dict](#dict)\[[str](#str), [ndarray](#numpy.ndarray)\]\]</code> | Each key is a level and each value its `S` indices. | <code>None</code>
`idx_bottom` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | Indices corresponding to the bottom level of `S`, size (`bottom`). | <code>None</code>

**Returns:**

Name | Type | Description
---- | ---- | -----------
`self` | | object, fitted reconciler.

#### `TopDown.fit_predict`

```python
fit_predict(S, y_hat, tags, idx_bottom=None, y_insample=None, y_hat_insample=None, sigmah=None, level=None, intervals_method=None, num_samples=None, seed=None)
```

Top Down Reconciliation Method.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`S` | <code>[ndarray](#numpy.ndarray)</code> | Summing matrix of size (`base`, `bottom`). | *required*
`y_hat` | <code>[ndarray](#numpy.ndarray)</code> | Forecast values of size (`base`, `horizon`). | *required*
`tags` | <code>[dict](#dict)\[[str](#str), [ndarray](#numpy.ndarray)\]</code> | Each key is a level and each value its `S` indices. | *required*
`idx_bottom` | <code>[ndarray](#numpy.ndarray)</code> | Indices corresponding to the bottom level of `S`, size (`bottom`). | <code>None</code>
`y_insample` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | Insample values of size (`base`, `insample_size`). Optional for `forecast_proportions` method. | <code>None</code>
`y_hat_insample` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | Insample forecast values of size (`base`, `insample_size`). Optional for `forecast_proportions` method. | <code>None</code>
`sigmah` | <code>[Optional](#typing.Optional)\[[ndarray](#numpy.ndarray)\]</code> | Estimated standard deviation of the conditional marginal distribution. | <code>None</code>
`level` | <code>[Optional](#typing.Optional)\[[list](#list)\[[int](#int)\]\]</code> | float list 0-100, confidence levels for prediction intervals. | <code>None</code>
`intervals_method` | <code>[Optional](#typing.Optional)\[[str](#str)\]</code> | Sampler for prediction intervals, one of `normality`, `bootstrap`, `permbu`. | <code>None</code>
`num_samples` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | Number of samples for probabilistic coherent distribution. | <code>None</code>
`seed` | <code>[Optional](#typing.Optional)\[[int](#int)\]</code> | Seed for reproducibility. | <code>None</code>

**Returns:**

Name | Type | Description
---- | ---- | -----------
`y_tilde` | | Reconciliated y_hat using the Top Down approach.
"""
