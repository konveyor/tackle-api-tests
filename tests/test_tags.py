import logging

import pytest


@pytest.mark.smoke
def test_default_tags(tackle_api_gateway):

    assert tackle_api_gateway.get_tag_names() == ['COTS', 'In house', 'SaaS', 'Boston (USA)', 'London (UK)',
                                                    'Paris (FR)', 'Sydney (AU)', 'DB2', 'MongoDB', 'Oracle',
                                                    'PostgreSQL', 'SQL Server', 'C# ASP .Net', 'C++', 'COBOL', 'Java',
                                                    'Javascript', 'Python', 'RHEL 8',
                                                    'Windows Server 2016', 'Z/OS', 'EAP', 'JWS', 'Quarkus',
                                                    'Spring Boot', 'Tomcat', 'WebLogic',
                                                    'WebSphere'], \
                                                    'Tags list check failed! (found : expected)'  # noqa: E501

def test_create_tags(tackle_api_gateway):
    assert tackle_api_gateway.get_tag() == ['tag1']
