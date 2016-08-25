from behave import *
from nose.tools import eq_

use_step_matcher("re")

@when("I play with it")
def step_impl(context):
    context.tamagotchi.play()

@then("it's happiness is increased")
def step_impl(context):
    eq_(6, context.tamagotchi.happiness)

@step("it's tiredness is increased")
def step_impl(context):
    eq_(6, context.tamagotchi.tiredness)