Feature: Changing Tamagotchi Needs Over Time
  As a Tamagotchi owner
  I want my Tamagotchi's needs to change over time
  So that I have to look after it carefully

  Scenario: Changing Tamagotchi Needs Over Time
    Given I have a Tamagotchi
    When time passes
    Then it's tiredness is increased
    And it's hungriness is increased
    And it's happiness is decreased