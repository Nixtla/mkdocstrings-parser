def test_autoarima_prophet(setup_parser):
    fn = """::: statsforecast.adapters.prophet.AutoARIMAProphet
    handler: python
    options:
      docstring_style: google
      members:
        - fit
        - predict
      heading_level: 3
      show_root_heading: true
      show_source: true"""
    output = setup_parser.process_markdown(fn)
    assert output == """### `AutoARIMAProphet`

```python
AutoARIMAProphet(growth='linear', changepoints=None, n_changepoints=25, changepoint_range=0.8, yearly_seasonality='auto', weekly_seasonality='auto', daily_seasonality='auto', holidays=None, seasonality_mode='additive', seasonality_prior_scale=10.0, holidays_prior_scale=10.0, changepoint_prior_scale=0.05, mcmc_samples=0, interval_width=0.8, uncertainty_samples=1000, stan_backend=None, d=None, D=None, max_p=5, max_q=5, max_P=2, max_Q=2, max_order=5, max_d=2, max_D=1, start_p=2, start_q=2, start_P=1, start_Q=1, stationary=False, seasonal=True, ic='aicc', stepwise=True, nmodels=94, trace=False, approximation=False, method=None, truncate=None, test='kpss', test_kwargs=None, seasonal_test='seas', seasonal_test_kwargs=None, allowdrift=False, allowmean=False, blambda=None, biasadj=False, period=1)
```

Bases: <code>[Prophet](#fbprophet.Prophet)</code>

AutoARIMAProphet adapter.

Returns best ARIMA model using external variables created by the Prophet interface.
This class receives as parameters the same as prophet.Prophet and uses a `models.AutoARIMA`
backend.

If your forecasting pipeline uses Prophet the `AutoARIMAProphet` adapter helps to
easily substitute Prophet with an AutoARIMA.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`growth` | <code>str, default="linear"</code> | 'linear', 'logistic' or 'flat' to specify a linear, logistic or flat trend. | <code>'linear'</code>
`changepoints` | <code>List of dates, default=None</code> | Potential changepoints. Otherwise selected automatically. | <code>None</code>
`n_changepoints` | <code>int, default=25</code> | Number of potential changepoints to include. | <code>25</code>
`changepoint_range` | <code>float, default=0.8</code> | Proportion of history in which trend changepoints will be estimated. | <code>0.8</code>
`yearly_seasonality` | <code>str, bool or int, default="auto"</code> | Fit yearly seasonality. Can be 'auto', True, False, or a number of Fourier terms to generate. | <code>'auto'</code>
`weekly_seasonality` | <code>str, bool or int, default="auto"</code> | Fit weekly seasonality. Can be 'auto', True, False, or a number of Fourier terms to generate. | <code>'auto'</code>
`daily_seasonality` | <code>str, bool or int, default="auto"</code> | Fit daily seasonality. Can be 'auto', True, False, or a number of Fourier terms to generate. | <code>'auto'</code>
`holidays` | <code>pandas.DataFrame, default=None</code> | DataFrame with columns holiday (string) and ds (date type). | <code>None</code>
`interval_width` | <code>float, default=0.80</code> | Uncertainty forecast intervals width. `StatsForecast`'s level | <code>0.8</code>

<details class="note" open markdown="1">
<summary>Note</summary>

You can create automated exogenous variables from the Prophet data processing pipeline
these exogenous will be included into `AutoARIMA`'s exogenous features. Parameters like
`seasonality_mode`, `seasonality_prior_scale`, `holidays_prior_scale`, `changepoint_prior_scale`,
`mcmc_samples`, `uncertainty_samples`, `stan_backend` are Prophet exclusive.

</details>

<details class="references" open markdown="1">
<summary>References</summary>

[Sean J. Taylor, Benjamin Letham (2017). "Prophet Forecasting at Scale"](https://peerj.com/preprints/3190.pdf)

[Oskar Triebe, Hansika Hewamalage, Polina Pilyugina, Nikolay Laptev, Christoph Bergmeir, Ram Rajagopal (2021). "NeuralProphet: Explainable Forecasting at Scale".](https://arxiv.org/pdf/2111.15397.pdf)

[Rob J. Hyndman, Yeasmin Khandakar (2008). "Automatic Time Series Forecasting: The forecast package for R"](https://www.jstatsoft.org/article/view/v027i03).

</details>

#### `AutoARIMAProphet.fit`

```python
fit(df, disable_seasonal_features=True)
```

Fit the AutoARIMAProphet adapter.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`df` | <code>[DataFrame](#pandas.DataFrame)</code> | DataFrame with columns ds (date type) and y, the time series. | *required*
`disable_seasonal_features` | <code>bool, default=True</code> | Disable Prophet's seasonal features. | <code>True</code>

**Returns:**

Name | Type | Description
---- | ---- | -----------
`AutoARIMAProphet` | | Adapter object with `AutoARIMA` fitted model.

#### `AutoARIMAProphet.predict`

```python
predict(df=None)
```

Predict using the AutoARIMAProphet adapter.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`df` | <code>pandas.DataFrame, default=None</code> | DataFrame with columns ds (date type) and y, the time series. | <code>None</code>

**Returns:**

Type | Description
---- | -----------
| pandas.DataFrame: DataFrame with the forecast components.
"""