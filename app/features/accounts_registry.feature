Feature: Accounts registry

 Scenario: User is able to create a new account
   Given Number of accounts in registry equals: "0"
   When I create an account using first name: "kurt", last name: "cobain", pesel: "89091209875"
   Then Number of accounts in registry equals: "1"
   And Account with pesel "89091209875" exists in registry

 Scenario: User is able to create a second account
   Given Number of accounts in registry equals: "1"
   When I create an account using first name: "janusz", last name: "dariuszewski", pesel: "66092909258"
   Then Number of accounts in registry equals: "2"
   And Account with pesel "66092909258" exists in registry

 Scenario: Admin user is able to save the account registry to db
   When I save the account registry to db
   Then Number of accounts in registry equals: "2"

 Scenario: User is able to delete already created account
   Given Account with pesel "89091209875" exists in registry
   When I delete account with pesel: "89091209875"
   Then Account with pesel "89091209875" does not exist in registry

 Scenario: User is able to update last name saved in account
   Given Account with pesel "66092909258" exists in registry
   When I update last name in account with pesel "66092909258" to "januszewski"
   Then Last name in account with pesel "66092909258" is "januszewski"

 Scenario: User is able to load account registry from db
   When I load account registry from db
   Then Number of accounts in registry equals: "2"
   And Account with pesel "89091209875" exists in registry
   And Account with pesel "66092909258" exists in registry

 Scenario: User is able to delete both accounts 
   Given Account with pesel "89091209875" exists in registry
   And Account with pesel "66092909258" exists in registry
   When I delete account with pesel: "89091209875"
   And I delete account with pesel: "66092909258"
   Then Number of accounts in registry equals: "0"
