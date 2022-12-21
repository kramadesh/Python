from shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.addItem("apple")

    assert cart.getSize() == 1

def test_when_item_added_then_should_be_present_in_cart(cart):
    cart.addItem("mango")
    assert "mango" in cart.getItems()

def test_when_more_than_max_size_added_then_should_fail(cart):
    for i in range(5):
        cart.addItem("mango")
    
    with pytest.raises(OverflowError):
        cart.addItem("banana")

def test_can_remove_item_from_cart(cart):
    pass
