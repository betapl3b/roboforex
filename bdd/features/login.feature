Feature: User login

  As a registered user
  I want to log in with valid credentials
  So that I can access my profile page

  Scenario: Successful login
    Given existing user account
    And the user is on the login page
    When the user logs in with valid credentials of the existing account
    Then correct user account number is shown on trading page
