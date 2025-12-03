def test_utilsforecast_rmae(setup_parser):
    fn = """::: utilsforecast.losses.rmae
    handler: python
    options:
      docstring_style: google
      heading_level: 3
      show_root_heading: true
      show_source: true"""

    output = setup_parser.process_markdown(fn)

    assert output == """### `rmae`

```python
rmae(df, models, baseline, id_col='unique_id', target_col='y', cutoff_col='cutoff')
```

Relative Mean Absolute Error (RMAE)

Calculates the RAME between two sets of forecasts (from two different forecasting methods).
A number smaller than one implies that the forecast in the
numerator is better than the forecast in the denominator.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`df` | <code>pandas or polars DataFrame</code> | Input dataframe with id, times, actuals and predictions. | *required*
`models` | <code>list of str</code> | Columns that identify the models predictions. | *required*
`baseline` | <code>[str](#str)</code> | Column that identifies the baseline model predictions. | *required*
`id_col` | <code>[str](#str)</code> | Column that identifies each serie. Defaults to 'unique_id'. | <code>'unique_id'</code>
`target_col` | <code>[str](#str)</code> | Column that contains the target. Defaults to 'y'. | <code>'y'</code>
`cutoff_col` | <code>[str](#str)</code> | Column that identifies the cutoff point for each forecast cross-validation fold. Defaults to 'cutoff'. | <code>'cutoff'</code>

**Returns:**

Type | Description
---- | -----------
<code>[IntoDataFrameT](#narwhals.stable.v2.typing.IntoDataFrameT)</code> | pandas or polars DataFrame: dataframe with one row per id and one column per model.
"""
