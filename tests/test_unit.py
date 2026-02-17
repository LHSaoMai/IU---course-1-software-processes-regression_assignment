import pytest 
from app.store import get_customer_status, calculate_discount

#  UNIT TEST: Checking Module A in isolation
@pytest.mark.parametrize('years ,expected_status',
        [(0,'standard'),
        (10,'platinum'),
        (15,'platinum')]
)
def test_all_customer_status(years,expected_status):
    result = get_customer_status(years)

    assert result == expected_status

#  UNIT TEST: Checking Module B in isolation
@pytest.mark.parametrize('status,expected_discount',
        [('standard',0),
        ('platinum',10)]
                         )
def test_all_discount(status,expected_discount):
    discount = calculate_discount(status)

    assert discount == expected_discount

   