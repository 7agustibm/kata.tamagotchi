from behave import *

use_step_matcher("re")


@given("I have a Tamagotchi")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I feed it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("it's hungriness is decreased")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("it's fullness is increased")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass