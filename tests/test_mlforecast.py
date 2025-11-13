def test_distributed_dask_lgb(setup_parser):
  fn = "::: mlforecast.distributed.dask.lgb"
  output = setup_parser.process_markdown(fn)
  assert output == """### `DaskLGBMForecast`

Bases: <code>[DaskLGBMRegressor](#lightgbm.dask.DaskLGBMRegressor)</code>

#### `DaskLGBMForecast.model_`

```python
model_
```
"""
