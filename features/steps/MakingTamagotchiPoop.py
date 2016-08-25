from behave import *

use_step_matcher("re")


@when("I make it poop")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("it's fullness is decreased")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass