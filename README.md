# dropinf

A lightweight Python utility for replacing infinite values (`inf`, `-inf`) with `NaN` and dropping rows containing missing values in Pandas DataFrames and Series.

## Installation

```bash
pip install dropinf
```

## Usage

```python
import pandas as pd
import numpy as np
from dropinf import dropinf

df = pd.DataFrame({
    "A": [1, np.inf, 3],
    "B": [4, 5, 6]
})

cleaned = dropinf(df)
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `dataframe` | Required | Pandas DataFrame or Series |
| `inplace` | `False` | Modify the original object |
| `infinity` | `numpy.inf` | Value representing infinity |
| `nan` | `numpy.nan` | Replacement for infinity |

## Return value

Returns a cleaned DataFrame or Series.
