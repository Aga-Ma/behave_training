# Created when scenario should be run with a number of variables giving a set of known states, actions and/or
# expected outcomes
# https://behave.readthedocs.io/en/latest/tutorial.html#scenario-outlines

Scenario Outline: Blenders
  Given I put <thing> in a blender,
  When I switch the blender on
  Then it should transform into <other thing>

Examples: Amphibians
  | thing         | other thing |
  | Red Tree Frog | mush        |

Examples: Consumer Electronics
  | thing        | other thing |
  | iPhone       | toxic waste |
  | Galaxy Nexus | toxic waste |