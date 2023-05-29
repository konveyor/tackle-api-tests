# coding: utf-8

"""
    MTA 6.1 api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ApiApplication(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'binary': 'str',
        'bucket': 'ApiRef',
        'business_service': 'ApiRef',
        'comments': 'str',
        'contributors': 'list[ApiRef]',
        'create_time': 'str',
        'create_user': 'str',
        'description': 'str',
        'id': 'int',
        'identities': 'list[ApiRef]',
        'migration_wave': 'ApiRef',
        'name': 'str',
        'owner': 'ApiRef',
        'repository': 'ApiRepository',
        'review': 'ApiRef',
        'tags': 'list[ApiTagRef]',
        'update_user': 'str'
    }

    attribute_map = {
        'binary': 'binary',
        'bucket': 'bucket',
        'business_service': 'businessService',
        'comments': 'comments',
        'contributors': 'contributors',
        'create_time': 'createTime',
        'create_user': 'createUser',
        'description': 'description',
        'id': 'id',
        'identities': 'identities',
        'migration_wave': 'migrationWave',
        'name': 'name',
        'owner': 'owner',
        'repository': 'repository',
        'review': 'review',
        'tags': 'tags',
        'update_user': 'updateUser'
    }

    def __init__(self, binary=None, bucket=None, business_service=None, comments=None, contributors=None, create_time=None, create_user=None, description=None, id=None, identities=None, migration_wave=None, name=None, owner=None, repository=None, review=None, tags=None, update_user=None, _configuration=None):  # noqa: E501
        """ApiApplication - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._binary = None
        self._bucket = None
        self._business_service = None
        self._comments = None
        self._contributors = None
        self._create_time = None
        self._create_user = None
        self._description = None
        self._id = None
        self._identities = None
        self._migration_wave = None
        self._name = None
        self._owner = None
        self._repository = None
        self._review = None
        self._tags = None
        self._update_user = None
        self.discriminator = None

        if binary is not None:
            self.binary = binary
        if bucket is not None:
            self.bucket = bucket
        if business_service is not None:
            self.business_service = business_service
        if comments is not None:
            self.comments = comments
        if contributors is not None:
            self.contributors = contributors
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if identities is not None:
            self.identities = identities
        if migration_wave is not None:
            self.migration_wave = migration_wave
        self.name = name
        if owner is not None:
            self.owner = owner
        if repository is not None:
            self.repository = repository
        if review is not None:
            self.review = review
        if tags is not None:
            self.tags = tags
        if update_user is not None:
            self.update_user = update_user

    @property
    def binary(self):
        """Gets the binary of this ApiApplication.  # noqa: E501


        :return: The binary of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """Sets the binary of this ApiApplication.


        :param binary: The binary of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._binary = binary

    @property
    def bucket(self):
        """Gets the bucket of this ApiApplication.  # noqa: E501


        :return: The bucket of this ApiApplication.  # noqa: E501
        :rtype: ApiRef
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ApiApplication.


        :param bucket: The bucket of this ApiApplication.  # noqa: E501
        :type: ApiRef
        """

        self._bucket = bucket

    @property
    def business_service(self):
        """Gets the business_service of this ApiApplication.  # noqa: E501


        :return: The business_service of this ApiApplication.  # noqa: E501
        :rtype: ApiRef
        """
        return self._business_service

    @business_service.setter
    def business_service(self, business_service):
        """Sets the business_service of this ApiApplication.


        :param business_service: The business_service of this ApiApplication.  # noqa: E501
        :type: ApiRef
        """

        self._business_service = business_service

    @property
    def comments(self):
        """Gets the comments of this ApiApplication.  # noqa: E501


        :return: The comments of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ApiApplication.


        :param comments: The comments of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def contributors(self):
        """Gets the contributors of this ApiApplication.  # noqa: E501


        :return: The contributors of this ApiApplication.  # noqa: E501
        :rtype: list[ApiRef]
        """
        return self._contributors

    @contributors.setter
    def contributors(self, contributors):
        """Sets the contributors of this ApiApplication.


        :param contributors: The contributors of this ApiApplication.  # noqa: E501
        :type: list[ApiRef]
        """

        self._contributors = contributors

    @property
    def create_time(self):
        """Gets the create_time of this ApiApplication.  # noqa: E501


        :return: The create_time of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiApplication.


        :param create_time: The create_time of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiApplication.  # noqa: E501


        :return: The create_user of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiApplication.


        :param create_user: The create_user of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def description(self):
        """Gets the description of this ApiApplication.  # noqa: E501


        :return: The description of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiApplication.


        :param description: The description of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ApiApplication.  # noqa: E501


        :return: The id of this ApiApplication.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiApplication.


        :param id: The id of this ApiApplication.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def identities(self):
        """Gets the identities of this ApiApplication.  # noqa: E501


        :return: The identities of this ApiApplication.  # noqa: E501
        :rtype: list[ApiRef]
        """
        return self._identities

    @identities.setter
    def identities(self, identities):
        """Sets the identities of this ApiApplication.


        :param identities: The identities of this ApiApplication.  # noqa: E501
        :type: list[ApiRef]
        """

        self._identities = identities

    @property
    def migration_wave(self):
        """Gets the migration_wave of this ApiApplication.  # noqa: E501


        :return: The migration_wave of this ApiApplication.  # noqa: E501
        :rtype: ApiRef
        """
        return self._migration_wave

    @migration_wave.setter
    def migration_wave(self, migration_wave):
        """Sets the migration_wave of this ApiApplication.


        :param migration_wave: The migration_wave of this ApiApplication.  # noqa: E501
        :type: ApiRef
        """

        self._migration_wave = migration_wave

    @property
    def name(self):
        """Gets the name of this ApiApplication.  # noqa: E501


        :return: The name of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiApplication.


        :param name: The name of this ApiApplication.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this ApiApplication.  # noqa: E501


        :return: The owner of this ApiApplication.  # noqa: E501
        :rtype: ApiRef
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ApiApplication.


        :param owner: The owner of this ApiApplication.  # noqa: E501
        :type: ApiRef
        """

        self._owner = owner

    @property
    def repository(self):
        """Gets the repository of this ApiApplication.  # noqa: E501


        :return: The repository of this ApiApplication.  # noqa: E501
        :rtype: ApiRepository
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ApiApplication.


        :param repository: The repository of this ApiApplication.  # noqa: E501
        :type: ApiRepository
        """

        self._repository = repository

    @property
    def review(self):
        """Gets the review of this ApiApplication.  # noqa: E501


        :return: The review of this ApiApplication.  # noqa: E501
        :rtype: ApiRef
        """
        return self._review

    @review.setter
    def review(self, review):
        """Sets the review of this ApiApplication.


        :param review: The review of this ApiApplication.  # noqa: E501
        :type: ApiRef
        """

        self._review = review

    @property
    def tags(self):
        """Gets the tags of this ApiApplication.  # noqa: E501


        :return: The tags of this ApiApplication.  # noqa: E501
        :rtype: list[ApiTagRef]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ApiApplication.


        :param tags: The tags of this ApiApplication.  # noqa: E501
        :type: list[ApiTagRef]
        """

        self._tags = tags

    @property
    def update_user(self):
        """Gets the update_user of this ApiApplication.  # noqa: E501


        :return: The update_user of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiApplication.


        :param update_user: The update_user of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._update_user = update_user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ApiApplication, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiApplication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiApplication):
            return True

        return self.to_dict() != other.to_dict()
