from behave import *
from nose.tools import eq_

use_step_matcher("re")


@when("time passes")
def step_impl(context):
    context.tamagotchi.timePasses()


@step("it's hungriness is increased")
def step_impl(context):
    eq_(6, context.tamagotchi.hungriness)


@step("it's happiness is decreased")
def step_impl(context):
    eq_(4, context.tamagotchi.happiness)