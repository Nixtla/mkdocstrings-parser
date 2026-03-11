def test_regular_fn(setup_parser):
    parser = setup_parser
    regular_fn = """::: coreforecast.differences.num_diffs"""
    output = parser.process_markdown(regular_fn)

    assert output == """### `num_diffs`

```python
num_diffs(x, max_d=1)
```

Determine the optimal number of non-seasonal differences for stationarity.

Uses the KPSS (Kwiatkowski-Phillips-Schmidt-Shin) test to determine how many
times the series needs to be differenced to achieve stationarity. The function
applies differencing iteratively until the KPSS statistic falls below the
threshold or the maximum number of differences is reached.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`x` | <code>[ndarray](#numpy.ndarray)</code> | Array with the time series. | *required*
`max_d` | <code>[int](#int)</code> | Maximum number of differences to consider. Defaults to 1. | <code>1</code>

**Returns:**

Name | Type | Description
---- | ---- | -----------
`int` | <code>[int](#int)</code> | Optimal number of differences.
"""

def test_fn_w_decorator(setup_parser):
    parser = setup_parser
    fn_w_decorator = """::: coreforecast.expanding.expanding_mean"""
    output = parser.process_markdown(fn_w_decorator)
    assert output == """### `expanding_mean`

```python
expanding_mean(x, skipna=False)
```

Compute the expanding_mean of the input array.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`x` | <code>np.ndarray</code> | Input array. | *required*
`skipna` | <code>bool</code> | If True, exclude NaN values from calculations. When False (default), any NaN value causes the result to be NaN, maintaining backwards compatibility. When True, NaN values are ignored (matching pandas default behavior). | *required*

**Returns:**

Type | Description
---- | -----------
| np.ndarray: Array with the expanding statistic

**Examples:**

```pycon
>>> import numpy as np
>>> x = np.array([1.0, 2.0, np.nan, 4.0, 5.0])
>>> # Default behavior: NaN propagates
>>> expanding_mean(x)
array([1., 1.5, nan, nan, nan])
>>> # With skipna=True: NaN values are excluded
>>> expanding_mean(x, skipna=True)
array([1., 1.5, 1.5, 2.33..., 3.0])
```
"""

def test_inherited_fn(setup_parser):
    inherited_fn = """::: coreforecast.lag_transforms.Lag
    handler: python
    options:
      docstring_style: google
      members:
        - stack
        - take
        - transform
        - update
      heading_level: 3
      show_root_heading: true
      show_source: true"""
    output = setup_parser.process_markdown(inherited_fn)
    assert output == """### `Lag`

```python
Lag(lag)
```

Bases: <code>[\_BaseLagTransform](#coreforecast.lag_transforms._BaseLagTransform)</code>

Simple lag operator

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`lag` | <code>[int](#int)</code> | Number of periods to offset | *required*

#### `Lag.stack`

```python
stack(transforms)
```

#### `Lag.take`

```python
take(_idxs)
```

#### `Lag.transform`

```python
transform(ga)
```

#### `Lag.update`

```python
update(ga)
```
"""