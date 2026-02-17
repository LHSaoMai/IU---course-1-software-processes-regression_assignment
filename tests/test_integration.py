import pytest 
from app.store import get_customer_status, calculate_discount

#  UNIT TEST: Checking Module A in isolation
@pytest.mark.parametrize('years,expected_discounts',
                         [(0,0),
                          (10,10),
                          (12,10)])

def test_integration_discount(years,expected_discounts):
    status = get_customer_status(years)
    discount = calculate_discount(status)

    assert discount == expected_discounts 
