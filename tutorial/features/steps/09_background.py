from behave import given
from hamcrest import assert_that, equal_to,  is_not


@given('the ninja encounters another opponent')
def step_the_ninja_encounters_another_opponent(context):
    """
    BACKGROUND steps are called at begin of each scenario before other steps.
    """
    # -- SETUP/TEARDOWN:
    if hasattr(context, "ninja_fight"):
        # -- VERIFY: Double-call does not occur.
        assert_that(context.ninja_fight, is_not(equal_to(None)))
    context.ninja_fight = None
