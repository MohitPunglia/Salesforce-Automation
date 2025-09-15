# features/login.feature
@login @ui
Feature: Salesforce Login Authentication

    As a Salesforce user
    I want to authenticate into the system
    So that I can access my CRM data

    Background:
        Given I am on the Salesforce login page

    @smoke
    Scenario: Successful login page load
        When the login page loads completely
        Then I should see the login form

    @smoke @credentials
    Scenario Outline: Login authentication
        When I attempt to login with username "<username>" and password "<password>"
        Then I should see the "<result>"

        Examples:
            | username                    | password      | result          |
            | ${SF_USERNAME}              | ${SF_PASSWORD} | home page       |
            | invalid@user.com            | wrongpass      | error message   |