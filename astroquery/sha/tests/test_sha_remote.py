import pytest

from astropy.table import Table

from astroquery import sha
from astroquery.exceptions import NoResultsWarning


@pytest.mark.remote_data
def test_query_no_results():
    # Test for issue #1836
    with pytest.warns(NoResultsWarning):
        result = sha.query(ra=219.57741, dec=64.171525, size=0.001)

    assert isinstance(result, Table)
    assert len(result) == 0
