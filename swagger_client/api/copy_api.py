# coding: utf-8

"""
    MTA 6.1 api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CopyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def reviews_copy_post(self, copy_request, **kwargs):  # noqa: E501
        """Copy a review from one application to others.  # noqa: E501

        Copy a review from one application to others.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reviews_copy_post(copy_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiCopyRequest copy_request: Review copy request data (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reviews_copy_post_with_http_info(copy_request, **kwargs)  # noqa: E501
        else:
            (data) = self.reviews_copy_post_with_http_info(copy_request, **kwargs)  # noqa: E501
            return data

    def reviews_copy_post_with_http_info(self, copy_request, **kwargs):  # noqa: E501
        """Copy a review from one application to others.  # noqa: E501

        Copy a review from one application to others.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reviews_copy_post_with_http_info(copy_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiCopyRequest copy_request: Review copy request data (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['copy_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reviews_copy_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'copy_request' is set
        if self.api_client.client_side_validation and ('copy_request' not in params or
                                                       params['copy_request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `copy_request` when calling `reviews_copy_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'copy_request' in params:
            body_params = params['copy_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/reviews/copy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
