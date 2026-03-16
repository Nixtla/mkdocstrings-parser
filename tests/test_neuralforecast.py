def test_timeseriesloader(setup_parser):
    fn = "::: neuralforecast.tsdataset.TimeSeriesLoader"
    output = setup_parser.process_markdown(fn)
    assert output == """### `TimeSeriesLoader`

```python
TimeSeriesLoader(dataset, **kwargs)
```

Bases: <code>[DataLoader](#torch.utils.data.DataLoader)</code>

TimeSeriesLoader DataLoader.

Small change to PyTorch's Data loader.
Combines a dataset and a sampler, and provides an iterable over the given dataset.

The class `~torch.utils.data.DataLoader` supports both map-style and
iterable-style datasets with single- or multi-process loading, customizing
loading order and optional automatic batching (collation) and memory pinning.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`dataset` |  | Dataset to load data from. | *required*
`batch_size` | <code>[int](#int)</code> | How many samples per batch to load. Defaults to 1. | *required*
`shuffle` | <code>[bool](#bool)</code> | Set to True to have the data reshuffled at every epoch. Defaults to False. | *required*
`sampler` | <code>[Sampler](#Sampler) or [Iterable](#Iterable)</code> | Defines the strategy to draw samples from the dataset. | *required*
`drop_last` | <code>[bool](#bool)</code> | Set to True to drop the last incomplete batch. Defaults to False. | *required*
`**kwargs` |  | Additional keyword arguments for DataLoader. | <code>{}</code>

"""