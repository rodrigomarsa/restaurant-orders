from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    bacon = Ingredient("bacon")
    bacon2 = Ingredient("bacon")
    farinha = Ingredient("farinha")
    assert bacon.name == "bacon"
    assert bacon.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    # assert bacon == bacon2
    assert bacon.__eq__(bacon2) is True
    assert bacon.__hash__() == bacon2.__hash__()
    assert bacon.__repr__() == "Ingredient('bacon')"
    assert bacon.__hash__() != farinha.__hash__()
