import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import github

# Add the backend directory to the Python path to allow for absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.application.services.readme_generator_service import ReadmeGeneratorService
from app.application.schemas.readme_schemas import ReadmeRequest

class TestReadmeGeneratorService(unittest.TestCase):

    def setUp(self):
        """Set up a test client and sample data."""
        self.service = ReadmeGeneratorService()
        self.request_data = ReadmeRequest(
            repo_name="Test-Repo",
            repo_description="A test repository for generating READMEs.",
            license="MIT"
        )

    def test_generate_readme_content(self):
        """Test the generation of README content."""
        content = self.service.generate_readme_content(self.request_data)

        self.assertIn("# Test-Repo", content)
        self.assertIn("A test repository for generating READMEs.", content)
        self.assertIn("This project is licensed under the MIT License.", content)
        self.assertIn("## Installation", content)
        self.assertIn("## Usage", content)
        self.assertIn("## Contributing", content)

    @patch('github.Github')
    def test_create_readme_on_github_new_file(self, mock_github):
        """Test creating a new README file on GitHub."""
        # Setup the mock
        mock_repo = MagicMock()
        # Raise the specific exception that the service code expects.
        mock_repo.get_contents.side_effect = github.UnknownObjectException(status=404, data={}, headers={})
        mock_github.return_value.get_repo.return_value = mock_repo

        result = self.service.create_readme_on_github(
            repo_full_name="user/test-repo",
            content="Test content",
            github_token="fake_token"
        )

        self.assertTrue(result)
        mock_repo.create_file.assert_called_once_with(
            path="README.md",
            message="docs: Create README.md",
            content="Test content",
            branch="main"
        )
        mock_repo.update_file.assert_not_called()

    @patch('github.Github')
    def test_create_readme_on_github_update_file(self, mock_github):
        """Test updating an existing README file on GitHub."""
        # Setup the mock
        mock_existing_file = MagicMock()
        mock_existing_file.sha = "fake_sha"

        mock_repo = MagicMock()
        mock_repo.get_contents.return_value = mock_existing_file
        mock_github.return_value.get_repo.return_value = mock_repo

        result = self.service.create_readme_on_github(
            repo_full_name="user/test-repo",
            content="Updated content",
            github_token="fake_token"
        )

        self.assertTrue(result)
        mock_repo.update_file.assert_called_once_with(
            path="README.md",
            message="docs: Update README.md",
            content="Updated content",
            sha="fake_sha",
            branch="main"
        )
        mock_repo.create_file.assert_not_called()

if __name__ == '__main__':
    unittest.main()
