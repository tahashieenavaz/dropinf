import pandas
import numpy
from dropinf import dropinf


def test_dropinf_works_on_dataframes():
    df = pandas.DataFrame([[1, 2], [numpy.inf, 4], [5, 6]])

    result = dropinf(df)

    expected = pandas.DataFrame([[1, 2], [5, 6]], index=[0, 2])
    pandas.testing.assert_frame_equal(result, expected, check_dtype=False)


def test_dropinf_works_on_series():
    series = pandas.Series([1, numpy.inf, 3, -numpy.inf, 5])

    result = dropinf(series)

    expected = pandas.Series([1, 3, 5], index=[0, 2, 4])
    pandas.testing.assert_series_equal(result, expected, check_dtype=False)
