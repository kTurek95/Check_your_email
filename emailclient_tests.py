import unittest
from unittest.mock import patch
from emailclient import EmailClient


class TestEmailClient(unittest.TestCase):

    def setUp(self):
        self.configurations = [
            {
                'imap_server': 'imap.example.com',
                'login': 'user@example.com',
                'password': 'password123'
            }
        ]
        self.file_name = "test.db"
        self.client = EmailClient(self.configurations, self.file_name)

    @patch("imaplib.IMAP4_SSL")
    def test_connect_with_server(self, MockIMAP):
        mock_server = MockIMAP()
        mock_server.login.return_value = "OK"

        result = self.client.connect_with_server(1)
        mock_server.login.assert_called_with(self.configurations[0]['login'], self.configurations[0]['password'])
        self.assertEqual(result, mock_server)

    @patch("imaplib.IMAP4_SSL")
    def test_select_mailbox(self, MockIMAP):
        mock_server = MockIMAP()
        mock_server.select.return_value = "OK"

        with patch("builtins.input", return_value="inbox"):
            result = self.client.select_mailbox(mock_server)
            self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()