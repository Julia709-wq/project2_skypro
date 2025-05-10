from unittest.mock import patch
from src.hh import HeadHunterAPI

@patch('requests.get')
def test_get_data(mock_get, sample_api_response):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = sample_api_response

    api = HeadHunterAPI()
    result = api.get_data('python')

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["name"] == "Backend разработчик"
