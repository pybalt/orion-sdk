# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_metrics_metrics_get(self) -> None:
        """Test case for metrics_metrics_get

        Metrics
        """
        pass

    def test_start_session_start_session_post(self) -> None:
        """Test case for start_session_start_session_post

        Start Session
        """
        pass

    def test_talk_content_talk_content_post(self) -> None:
        """Test case for talk_content_talk_content_post

        Talk Content
        """
        pass

    def test_talk_content_transcribe_post(self) -> None:
        """Test case for talk_content_transcribe_post

        Talk Content
        """
        pass

    def test_talk_talk_post(self) -> None:
        """Test case for talk_talk_post

        Talk
        """
        pass

    def test_talk_with_gitbook_talk_gitbook_post(self) -> None:
        """Test case for talk_with_gitbook_talk_gitbook_post

        Talk With Gitbook
        """
        pass


if __name__ == '__main__':
    unittest.main()
