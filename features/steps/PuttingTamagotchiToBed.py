from behave import *

use_step_matcher("re")


@when("I put it to bed")
def step_impl(context):
    context.tamagotchi.toBed()


@then("it's tiredness is decreased")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass