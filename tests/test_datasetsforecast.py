def test_yearly_dataclass(setup_parser):
    fn = "::: datasetsforecast.m3.Yearly"
    rendered = setup_parser.process_markdown(fn)

    assert rendered == """### `Yearly`

```python
Yearly(
    seasonality=1,
    horizon=6,
    freq="Y",
    sheet_name="M3Year",
    name="Yearly",
    n_ts=645,
)
```

#### `Yearly.freq`

```python
freq: str = 'Y'
```

#### `Yearly.horizon`

```python
horizon: int = 6
```

#### `Yearly.n_ts`

```python
n_ts: int = 645
```

#### `Yearly.name`

```python
name: str = 'Yearly'
```

#### `Yearly.seasonality`

```python
seasonality: int = 1
```

#### `Yearly.sheet_name`

```python
sheet_name: str = 'M3Year'
```
"""


def test_download_file(setup_parser):
    fn = """::: datasetsforecast.utils.download_file"""
    rendered = setup_parser.process_markdown(fn)

    assert rendered == """### `download_file`

```python
download_file(directory, source_url, decompress=False)
```

Download data from source_ulr inside directory.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`directory` | <code>([str](#str), [Path](#pathlib.Path))</code> | Custom directory where data will be downloaded. | *required*
`source_url` | <code>[str](#str)</code> | URL where data is hosted. | *required*
`decompress` | <code>[bool](#bool)</code> | Wheter decompress downloaded file. Default False. | <code>False</code>
"""