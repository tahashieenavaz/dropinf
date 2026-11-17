import pandas
import numpy
import typing

DataFrameOrSeries: typing.TypeAlias = pandas.DataFrame | pandas.Series


def dropinf(
    dataframe: DataFrameOrSeries,
    *,
    inplace: bool = False,
    infinity: float = numpy.inf,
    nan: float = numpy.nan,
) -> DataFrameOrSeries:
    return dataframe.replace([infinity, -infinity], nan).dropna(inplace=inplace)
