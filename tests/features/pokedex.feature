Feature: pokedex search
  As a Pokemon trainer,
  I want to search for pokemons in my pokedex,
  So I can learn more about them.

  Background:
    Given the pokedex page

  Scenario Outline: Name pokedex search
    When the user searches for "<text>"
    Then the "<pokemon>" information is shown

    Examples: Pokemons
      | text       | pokemon    |
      | Pikachu    | Pikachu    |
      | Charmander | Charmander |