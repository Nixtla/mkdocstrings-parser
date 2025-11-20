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
`dataset` | | Dataset to load data from. | *required*
`batch_size` | <code>[int](#int)</code> | How many samples per batch to load. Defaults to 1. | *required*
`shuffle` | <code>[bool](#bool)</code> | Set to True to have the data reshuffled at every epoch. Defaults to False. | *required*
`sampler` | <code>[Sampler](#Sampler) or [Iterable](#Iterable)</code> | Defines the strategy to draw samples from the dataset. | *required*
`drop_last` | <code>[bool](#bool)</code> | Set to True to drop the last incomplete batch. Defaults to False. | *required*
`**kwargs` | | Additional keyword arguments for DataLoader. | <code>{}</code>
"""

def test_autornn(setup_parser):
    fn = """::: neuralforecast.auto.AutoRNN
    options:
      members: [__init__]
      heading_level: 3"""
    output = setup_parser.process_markdown(fn)
    assert output == """### `AutoRNN`

```python
AutoRNN(h, loss=MAE(), valid_loss=None, config=None, search_alg=BasicVariantGenerator(random_state=1), num_samples=10, refit_with_val=False, cpus=cpu_count(), gpus=torch.cuda.device_count(), verbose=False, alias=None, backend='ray', callbacks=None)
```

Bases: <code>[BaseAuto](#neuralforecast.common._base_auto.BaseAuto)</code>

Class for Automatic Hyperparameter Optimization, it builds on top of `ray` to
give access to a wide variety of hyperparameter optimization tools ranging
from classic grid search, to Bayesian optimization and HyperBand algorithm.

The validation loss to be optimized is defined by the `config['loss']` dictionary
value, the config also contains the rest of the hyperparameter search space.

It is important to note that the success of this hyperparameter optimization
heavily relies on a strong correlation between the validation and test periods.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`cls_model` | <code>PyTorch/PyTorchLightning model</code> | See `neuralforecast.models` [collection here](./models). | *required*
`h` | <code>int</code> | Forecast horizon | *required*
`loss` | <code>PyTorch module</code> | Instantiated train loss class from [losses collection](./losses.pytorch). | *required*
`valid_loss` | <code>PyTorch module</code> | Instantiated valid loss class from [losses collection](./losses.pytorch). | *required*
`config` | <code>dict or callable</code> | Dictionary with ray.tune defined search space or function that takes an optuna trial and returns a configuration dict. | *required*
`search_alg` | <code>ray.tune.search variant or optuna.sampler</code> | For ray see https://docs.ray.io/en/latest/tune/api_docs/suggestion.html | *required*
`For optuna see https` | | //optuna.readthedocs.io/en/stable/reference/samplers/index.html. | *required*
`num_samples` | <code>int</code> | Number of hyperparameter optimization steps/samples. | *required*
`cpus` | <code>int</code> | Number of cpus to use during optimization. Only used with ray tune. | *required*
`gpus` | <code>int</code> | Number of gpus to use during optimization, default all available. Only used with ray tune. | *required*
`refit_with_val` | <code>bool</code> | Refit of best model should preserve val_size. | *required*
`verbose` | <code>bool</code> | Track progress. | *required*
`alias` | <code>str</code> | Custom name of the model. | *required*
`backend` | <code>str</code> | Backend to use for searching the hyperparameter space, can be either 'ray' or 'optuna'. | *required*
`callbacks` | <code>list of callable</code> | List of functions to call during the optimization process. | *required*
`ray reference` | | https://docs.ray.io/en/latest/tune/tutorials/tune-metrics.html | *required*
`optuna reference` | | https://optuna.readthedocs.io/en/stable | *required*
"""