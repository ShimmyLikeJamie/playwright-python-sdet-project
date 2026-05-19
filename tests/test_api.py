import pytest, logging
from playwright.sync_api import APIRequestContext

#initialize logger for this module

logger = logging.getLogger(__name__)

def test_create_user_via_api(playwright):
    #1 Create API request context
    request_context = playwright.request.new_context(base_url="https://reqres.in")
    #2 Define user data to send in the request
    user_data = {
        "data": {
        "name": "Wynter Oppel",
        "role": "SDET Engineer",
        "email": "oppel.jamie@gmail.com"
    }}

    #3 Set headers for the request, including content type and API key if required

    headers = {
        "Content-Type": "application/json",
        "x-api-key": "pro_52a8b2c769299481b599b914a8a5d439528fe35245d9fe8e"  # Replace with actual API key if required
    }

    #4 Set endpoint
    endpoint = "https://reqres.in/api/collections/users/records?project_id=22718"

    logger.info(f"Sending POST request to endpoint: {endpoint} with data: {user_data}")

    response = request_context.post(endpoint, 
                                    data=user_data,
                                    headers=headers)
    #4 Verify the response status code is 201 (Created)

    assert response.ok, f"API call failed with status: {response.status}"
    assert response.status == 201, f"Expected status code 201, got {response.status}"

    #5 Extract JSON back from server response
    response_json = response.json()

    #5a Log the response for debugging purposes
    logger.info(f"Received response: {response_json}")

    #6 Assertions follow below
    assert response.ok, f"API call failed with status: {response.status}"

    #Response has user data nested inside of TWO layers of "data" objects
    actual_user_data = response_json["data"]["data"]

    #7 Verify the data was stored correctly by checking the response
    assert actual_user_data["name"] == "Wynter Oppel"
    assert actual_user_data["role"] == "SDET Engineer"

    #8 Check that an ID and createdAt timestamp were returned
    outer_data = response_json["data"]

    assert "id" in outer_data, "Response is missing 'id'"
    assert "created_at" in outer_data, "Response is missing 'createdAt'"

    # Clean up the context
    request_context.dispose()