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


class ApiTracker(object):
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
        'connected': 'bool',
        'create_time': 'str',
        'create_user': 'str',
        'id': 'int',
        'identity': 'ApiRef',
        'insecure': 'bool',
        'kind': 'str',
        'last_updated': 'str',
        'message': 'str',
        'metadata': 'ApiMetadata',
        'name': 'str',
        'update_user': 'str',
        'url': 'str'
    }

    attribute_map = {
        'connected': 'connected',
        'create_time': 'createTime',
        'create_user': 'createUser',
        'id': 'id',
        'identity': 'identity',
        'insecure': 'insecure',
        'kind': 'kind',
        'last_updated': 'lastUpdated',
        'message': 'message',
        'metadata': 'metadata',
        'name': 'name',
        'update_user': 'updateUser',
        'url': 'url'
    }

    def __init__(self, connected=None, create_time=None, create_user=None, id=None, identity=None, insecure=None, kind=None, last_updated=None, message=None, metadata=None, name=None, update_user=None, url=None, _configuration=None):  # noqa: E501
        """ApiTracker - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connected = None
        self._create_time = None
        self._create_user = None
        self._id = None
        self._identity = None
        self._insecure = None
        self._kind = None
        self._last_updated = None
        self._message = None
        self._metadata = None
        self._name = None
        self._update_user = None
        self._url = None
        self.discriminator = None

        if connected is not None:
            self.connected = connected
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if id is not None:
            self.id = id
        self.identity = identity
        if insecure is not None:
            self.insecure = insecure
        self.kind = kind
        if last_updated is not None:
            self.last_updated = last_updated
        if message is not None:
            self.message = message
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        if update_user is not None:
            self.update_user = update_user
        self.url = url

    @property
    def connected(self):
        """Gets the connected of this ApiTracker.  # noqa: E501


        :return: The connected of this ApiTracker.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this ApiTracker.


        :param connected: The connected of this ApiTracker.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def create_time(self):
        """Gets the create_time of this ApiTracker.  # noqa: E501


        :return: The create_time of this ApiTracker.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiTracker.


        :param create_time: The create_time of this ApiTracker.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiTracker.  # noqa: E501


        :return: The create_user of this ApiTracker.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiTracker.


        :param create_user: The create_user of this ApiTracker.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def id(self):
        """Gets the id of this ApiTracker.  # noqa: E501


        :return: The id of this ApiTracker.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiTracker.


        :param id: The id of this ApiTracker.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def identity(self):
        """Gets the identity of this ApiTracker.  # noqa: E501


        :return: The identity of this ApiTracker.  # noqa: E501
        :rtype: ApiRef
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this ApiTracker.


        :param identity: The identity of this ApiTracker.  # noqa: E501
        :type: ApiRef
        """
        if self._configuration.client_side_validation and identity is None:
            raise ValueError("Invalid value for `identity`, must not be `None`")  # noqa: E501

        self._identity = identity

    @property
    def insecure(self):
        """Gets the insecure of this ApiTracker.  # noqa: E501


        :return: The insecure of this ApiTracker.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this ApiTracker.


        :param insecure: The insecure of this ApiTracker.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def kind(self):
        """Gets the kind of this ApiTracker.  # noqa: E501


        :return: The kind of this ApiTracker.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ApiTracker.


        :param kind: The kind of this ApiTracker.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["jira-cloud", "jira-onprem"]  # noqa: E501
        if (self._configuration.client_side_validation and
                kind not in allowed_values):
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def last_updated(self):
        """Gets the last_updated of this ApiTracker.  # noqa: E501


        :return: The last_updated of this ApiTracker.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ApiTracker.


        :param last_updated: The last_updated of this ApiTracker.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

    @property
    def message(self):
        """Gets the message of this ApiTracker.  # noqa: E501


        :return: The message of this ApiTracker.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ApiTracker.


        :param message: The message of this ApiTracker.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def metadata(self):
        """Gets the metadata of this ApiTracker.  # noqa: E501


        :return: The metadata of this ApiTracker.  # noqa: E501
        :rtype: ApiMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ApiTracker.


        :param metadata: The metadata of this ApiTracker.  # noqa: E501
        :type: ApiMetadata
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this ApiTracker.  # noqa: E501


        :return: The name of this ApiTracker.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiTracker.


        :param name: The name of this ApiTracker.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def update_user(self):
        """Gets the update_user of this ApiTracker.  # noqa: E501


        :return: The update_user of this ApiTracker.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiTracker.


        :param update_user: The update_user of this ApiTracker.  # noqa: E501
        :type: str
        """

        self._update_user = update_user

    @property
    def url(self):
        """Gets the url of this ApiTracker.  # noqa: E501


        :return: The url of this ApiTracker.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ApiTracker.


        :param url: The url of this ApiTracker.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if issubclass(ApiTracker, dict):
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
        if not isinstance(other, ApiTracker):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiTracker):
            return True

        return self.to_dict() != other.to_dict()
