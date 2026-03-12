import pytest


@pytest.mark.datasets
def test_yearly_dataclass(setup_parser):
    fn = "::: datasetsforecast.m3.Yearly"
    rendered = setup_parser.process_markdown(fn)

    assert rendered == """### `Yearly`

```python
Yearly(seasonality=1, horizon=6, freq='YE', name='Yearly', n_ts=645, source_url='https://zenodo.org/api/records/4656222/files/m3_yearly_dataset.zip/content', file_name='m3_yearly_dataset')
```

#### `Yearly.file_name`

```python
file_name: str = 'm3_yearly_dataset'
```

#### `Yearly.freq`

```python
freq: str = 'YE'
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

#### `Yearly.source_url`

```python
source_url: str = 'https://zenodo.org/api/records/4656222/files/m3_yearly_dataset.zip/content'
```

"""

@pytest.mark.datasets
def test_download_file(setup_parser):
    fn = """::: datasetsforecast.utils.download_file"""
    rendered = setup_parser.process_markdown(fn)

    assert rendered == """### `download_file`

```python
download_file(directory, source_url, decompress=False, filename=None, max_retries=3)
```

Download data from source_url inside directory.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`directory` | <code>([str](#str), [Path](#pathlib.Path))</code> | Custom directory where data will be downloaded. | *required*
`source_url` | <code>[str](#str)</code> | URL where data is hosted. | *required*
`decompress` | <code>[bool](#bool)</code> | Whether to decompress downloaded file. Default False. | <code>False</code>
`filename` | <code>[str](#str)</code> | Override filename for the downloaded file. If None, the filename is derived from the URL. | <code>None</code>
`max_retries` | <code>[int](#int)</code> | Maximum number of retry attempts on transient errors. | <code>3</code>

"""