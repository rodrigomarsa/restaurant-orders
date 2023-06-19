from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("pizza 4 queijos", None)

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("pizza 4 queijos", 0)

    pizza_4_queijos = Dish("pizza 4 queijos", 59.9)
    pizza_queijos = Dish("pizza 4 queijos", 59.9)
    assert pizza_4_queijos.name == "pizza 4 queijos"
    pizza_calabresa = Dish("pizza 4 queijos", 49.9)
    assert pizza_4_queijos != pizza_calabresa
    assert pizza_4_queijos == pizza_queijos
    assert pizza_4_queijos.__repr__() == "Dish('pizza 4 queijos', R$59.90)"
    assert pizza_4_queijos.__hash__() == pizza_queijos.__hash__()
    assert pizza_4_queijos.__hash__() != pizza_calabresa.__hash__()
    queijo_mussarela = Ingredient("queijo mussarela")
    pizza_4_queijos.add_ingredient_dependency(queijo_mussarela, 10)
    assert pizza_4_queijos.get_ingredients() == {
        Ingredient("queijo mussarela")
    }
    assert pizza_4_queijos.recipe.get(queijo_mussarela) == 10
    assert pizza_4_queijos.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
