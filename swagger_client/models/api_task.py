# coding: utf-8

"""
    MTA 6.1.0 api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ApiTask(object):
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
        'addon': 'str',
        'application': 'ApiRef',
        'bucket': 'ApiRef',
        'canceled': 'bool',
        'create_time': 'str',
        'create_user': 'str',
        'data': 'object',
        'error': 'str',
        'id': 'int',
        'image': 'str',
        'locator': 'str',
        'name': 'str',
        'pod': 'str',
        'policy': 'str',
        'priority': 'int',
        'purged': 'bool',
        'report': 'ApiTaskReport',
        'retries': 'int',
        'started': 'str',
        'state': 'str',
        'terminated': 'str',
        'ttl': 'ApiTTL',
        'update_user': 'str',
        'variant': 'str'
    }

    attribute_map = {
        'addon': 'addon',
        'application': 'application',
        'bucket': 'bucket',
        'canceled': 'canceled',
        'create_time': 'createTime',
        'create_user': 'createUser',
        'data': 'data',
        'error': 'error',
        'id': 'id',
        'image': 'image',
        'locator': 'locator',
        'name': 'name',
        'pod': 'pod',
        'policy': 'policy',
        'priority': 'priority',
        'purged': 'purged',
        'report': 'report',
        'retries': 'retries',
        'started': 'started',
        'state': 'state',
        'terminated': 'terminated',
        'ttl': 'ttl',
        'update_user': 'updateUser',
        'variant': 'variant'
    }

    def __init__(self, addon=None, application=None, bucket=None, canceled=None, create_time=None, create_user=None, data=None, error=None, id=None, image=None, locator=None, name=None, pod=None, policy=None, priority=None, purged=None, report=None, retries=None, started=None, state=None, terminated=None, ttl=None, update_user=None, variant=None, _configuration=None):  # noqa: E501
        """ApiTask - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._addon = None
        self._application = None
        self._bucket = None
        self._canceled = None
        self._create_time = None
        self._create_user = None
        self._data = None
        self._error = None
        self._id = None
        self._image = None
        self._locator = None
        self._name = None
        self._pod = None
        self._policy = None
        self._priority = None
        self._purged = None
        self._report = None
        self._retries = None
        self._started = None
        self._state = None
        self._terminated = None
        self._ttl = None
        self._update_user = None
        self._variant = None
        self.discriminator = None

        self.addon = addon
        if application is not None:
            self.application = application
        if bucket is not None:
            self.bucket = bucket
        if canceled is not None:
            self.canceled = canceled
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        self.data = data
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if locator is not None:
            self.locator = locator
        if name is not None:
            self.name = name
        if pod is not None:
            self.pod = pod
        if policy is not None:
            self.policy = policy
        if priority is not None:
            self.priority = priority
        if purged is not None:
            self.purged = purged
        if report is not None:
            self.report = report
        if retries is not None:
            self.retries = retries
        if started is not None:
            self.started = started
        if state is not None:
            self.state = state
        if terminated is not None:
            self.terminated = terminated
        if ttl is not None:
            self.ttl = ttl
        if update_user is not None:
            self.update_user = update_user
        if variant is not None:
            self.variant = variant

    @property
    def addon(self):
        """Gets the addon of this ApiTask.  # noqa: E501


        :return: The addon of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._addon

    @addon.setter
    def addon(self, addon):
        """Sets the addon of this ApiTask.


        :param addon: The addon of this ApiTask.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and addon is None:
            raise ValueError("Invalid value for `addon`, must not be `None`")  # noqa: E501

        self._addon = addon

    @property
    def application(self):
        """Gets the application of this ApiTask.  # noqa: E501


        :return: The application of this ApiTask.  # noqa: E501
        :rtype: ApiRef
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ApiTask.


        :param application: The application of this ApiTask.  # noqa: E501
        :type: ApiRef
        """

        self._application = application

    @property
    def bucket(self):
        """Gets the bucket of this ApiTask.  # noqa: E501


        :return: The bucket of this ApiTask.  # noqa: E501
        :rtype: ApiRef
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ApiTask.


        :param bucket: The bucket of this ApiTask.  # noqa: E501
        :type: ApiRef
        """

        self._bucket = bucket

    @property
    def canceled(self):
        """Gets the canceled of this ApiTask.  # noqa: E501


        :return: The canceled of this ApiTask.  # noqa: E501
        :rtype: bool
        """
        return self._canceled

    @canceled.setter
    def canceled(self, canceled):
        """Sets the canceled of this ApiTask.


        :param canceled: The canceled of this ApiTask.  # noqa: E501
        :type: bool
        """

        self._canceled = canceled

    @property
    def create_time(self):
        """Gets the create_time of this ApiTask.  # noqa: E501


        :return: The create_time of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiTask.


        :param create_time: The create_time of this ApiTask.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiTask.  # noqa: E501


        :return: The create_user of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiTask.


        :param create_user: The create_user of this ApiTask.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def data(self):
        """Gets the data of this ApiTask.  # noqa: E501


        :return: The data of this ApiTask.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApiTask.


        :param data: The data of this ApiTask.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def error(self):
        """Gets the error of this ApiTask.  # noqa: E501


        :return: The error of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ApiTask.


        :param error: The error of this ApiTask.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """Gets the id of this ApiTask.  # noqa: E501


        :return: The id of this ApiTask.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiTask.


        :param id: The id of this ApiTask.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this ApiTask.  # noqa: E501


        :return: The image of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ApiTask.


        :param image: The image of this ApiTask.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def locator(self):
        """Gets the locator of this ApiTask.  # noqa: E501


        :return: The locator of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this ApiTask.


        :param locator: The locator of this ApiTask.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def name(self):
        """Gets the name of this ApiTask.  # noqa: E501


        :return: The name of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiTask.


        :param name: The name of this ApiTask.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pod(self):
        """Gets the pod of this ApiTask.  # noqa: E501


        :return: The pod of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._pod

    @pod.setter
    def pod(self, pod):
        """Sets the pod of this ApiTask.


        :param pod: The pod of this ApiTask.  # noqa: E501
        :type: str
        """

        self._pod = pod

    @property
    def policy(self):
        """Gets the policy of this ApiTask.  # noqa: E501


        :return: The policy of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ApiTask.


        :param policy: The policy of this ApiTask.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def priority(self):
        """Gets the priority of this ApiTask.  # noqa: E501


        :return: The priority of this ApiTask.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ApiTask.


        :param priority: The priority of this ApiTask.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def purged(self):
        """Gets the purged of this ApiTask.  # noqa: E501


        :return: The purged of this ApiTask.  # noqa: E501
        :rtype: bool
        """
        return self._purged

    @purged.setter
    def purged(self, purged):
        """Sets the purged of this ApiTask.


        :param purged: The purged of this ApiTask.  # noqa: E501
        :type: bool
        """

        self._purged = purged

    @property
    def report(self):
        """Gets the report of this ApiTask.  # noqa: E501


        :return: The report of this ApiTask.  # noqa: E501
        :rtype: ApiTaskReport
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this ApiTask.


        :param report: The report of this ApiTask.  # noqa: E501
        :type: ApiTaskReport
        """

        self._report = report

    @property
    def retries(self):
        """Gets the retries of this ApiTask.  # noqa: E501


        :return: The retries of this ApiTask.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this ApiTask.


        :param retries: The retries of this ApiTask.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def started(self):
        """Gets the started of this ApiTask.  # noqa: E501


        :return: The started of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this ApiTask.


        :param started: The started of this ApiTask.  # noqa: E501
        :type: str
        """

        self._started = started

    @property
    def state(self):
        """Gets the state of this ApiTask.  # noqa: E501


        :return: The state of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ApiTask.


        :param state: The state of this ApiTask.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def terminated(self):
        """Gets the terminated of this ApiTask.  # noqa: E501


        :return: The terminated of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this ApiTask.


        :param terminated: The terminated of this ApiTask.  # noqa: E501
        :type: str
        """

        self._terminated = terminated

    @property
    def ttl(self):
        """Gets the ttl of this ApiTask.  # noqa: E501


        :return: The ttl of this ApiTask.  # noqa: E501
        :rtype: ApiTTL
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this ApiTask.


        :param ttl: The ttl of this ApiTask.  # noqa: E501
        :type: ApiTTL
        """

        self._ttl = ttl

    @property
    def update_user(self):
        """Gets the update_user of this ApiTask.  # noqa: E501


        :return: The update_user of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiTask.


        :param update_user: The update_user of this ApiTask.  # noqa: E501
        :type: str
        """

        self._update_user = update_user

    @property
    def variant(self):
        """Gets the variant of this ApiTask.  # noqa: E501


        :return: The variant of this ApiTask.  # noqa: E501
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this ApiTask.


        :param variant: The variant of this ApiTask.  # noqa: E501
        :type: str
        """

        self._variant = variant

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
        if issubclass(ApiTask, dict):
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
        if not isinstance(other, ApiTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiTask):
            return True

        return self.to_dict() != other.to_dict()
