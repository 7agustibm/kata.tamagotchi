from behave import *
from nose.tools import eq_

from tamagochi.tamagochi import Tamagotchi

use_step_matcher("re")


@given("I have a Tamagotchi")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.tamagotchi = Tamagotchi()


@when("I feed it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.tamaotchi.eat()


@then("it's hungriness is decreased")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    eq_(4, context.tamaotchi.hungriness())


@step("it's fullness is increased")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    eq_(6, context.tamaotchi.fullness())
