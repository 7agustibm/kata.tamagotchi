from behave import *
from nose.tools import eq_

from tamagochi.tamagochi import Tamagotchi

use_step_matcher("re")


@given("I have a Tamagotchi")
def step_impl(context):
    context.tamagotchi = Tamagotchi()

@when("I feed it")
def step_impl(context):
    context.tamagotchi.eat()

@then("it's hungriness is decreased")
def step_impl(context):
    eq_(4, context.tamagotchi.hungriness)

@step("it's fullness is increased")
def step_impl(context):
    eq_(6, context.tamagotchi.fullness)