def test_regular_fn(setup_parser):
    parser = setup_parser
    regular_fn = """::: coreforecast.differences.num_diffs"""
    output = parser.process_markdown(regular_fn)

    assert output == """### `num_diffs`

```python
num_diffs(x, max_d=1)
```

Find the optimal number of differences

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
expanding_mean(x)
```

Compute the expanding_mean of the input array.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`x` | <code>np.ndarray</code> | Input array. | *required*

**Returns:**

Type | Description
---- | -----------
| np.ndarray: Array with the expanding statistic
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