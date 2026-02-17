import pytest 
from app.store import get_customer_status

#  UNIT TEST: Checking Module A in isolation

@pytest.mark.parametrize('years ,expected_status',
        [(0,'standard'),
        (10,'platinum'),
        (15,'platinum')]
)
def test_all_customer_status(years,expected_status):
    result = get_customer_status(years)

    assert result == expected_status
   