import pytest
import os
import webbrowser
from datetime import datetime

def pytest_configure(config):
    """Configure the HTML report with custom settings"""
    # Create reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Generate timestamp for unique report name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = os.path.join('reports', f'test_report_{timestamp}.html')
    
    # Set the report path in pytest configuration
    config.option.htmlpath = report_path
    config.option.self_contained_html = True

def pytest_sessionfinish(session, exitstatus):
    """Open the HTML report after test completion"""
    if not os.getenv("GITHUB_ACTIONS"):  # Only open if not in CI environment
        report_path = session.config.option.htmlpath
        if os.path.exists(report_path):
            print(f"\nOpening HTML report: {report_path}")
            webbrowser.open(f'file://{os.path.abspath(report_path)}') 