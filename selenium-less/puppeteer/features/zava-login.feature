Feature: Account Login

  Scenario: Redirect to the account page
    Given a "patient" is on the "account login" page
    When the "patient" fills out their login details
    And clicks login
    Then the "patient" is taken to the "account" steps
