Feature: Private account transfers

  Scenario: User is able to make an incoming transfer
    When I create an account using first name: "kurt", last name: "cobain", pesel: "89091209875"
    And I make an "incoming" transfer of "100"
    Then My balance should be "100"

  Scenario: User is able to make an outgoing transfer
    When I create an account using first name: "janusz", last name: "dariuszewski", pesel: "66092909258"
    And I make an "incoming" transfer of "200"
    And I make an "outgoing" transfer of "50"
    Then My balance should be "150"

  Scenario: User is able to delete both accounts 
    Given Account with pesel "89091209875" exists in registry
    And Account with pesel "66092909258" exists in registry
    When I delete account with pesel: "89091209875"
    And I delete account with pesel: "66092909258"
    Then Number of accounts in registry equals: "0"
