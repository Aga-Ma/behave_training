# Feature file written by Business Analyst / Sponsor / whoever with behaviour scenarios
# A feature file has a natural language format
# https://behave.readthedocs.io/en/latest/tutorial.html#feature-files

Feature: showing off behave

  Scenario: run a simple test
    # we put the system in a known state
    Given we have behave installed
    # we take key actions
    When we implement a test
    # we observe outcomes
    Then behave will test it for us!