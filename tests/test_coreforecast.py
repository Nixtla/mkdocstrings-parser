import sys

sys.path.append("..")
from parser import MkDocstringsParser

import pytest


@pytest.fixture
def setup_parser():
    parser = MkDocstringsParser()
    yield parser


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
