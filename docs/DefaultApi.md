# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_metrics_get**](DefaultApi.md#metrics_metrics_get) | **GET** /metrics | Metrics
[**start_session_set_id_post**](DefaultApi.md#start_session_set_id_post) | **POST** /set_id | Start Session
[**talk_content_talk_content_post**](DefaultApi.md#talk_content_talk_content_post) | **POST** /talk/content | Talk Content
[**talk_talk_post**](DefaultApi.md#talk_talk_post) | **POST** /talk | Talk
[**talk_with_gitbook_talk_gitbook_post**](DefaultApi.md#talk_with_gitbook_talk_gitbook_post) | **POST** /talk/gitbook | Talk With Gitbook
[**transcribe_transcribe_post**](DefaultApi.md#transcribe_transcribe_post) | **POST** /transcribe | Transcribe


# **metrics_metrics_get**
> object metrics_metrics_get()

Metrics

Endpoint that serves Prometheus metrics.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Metrics
        api_response = api_instance.metrics_metrics_get()
        print("The response of DefaultApi->metrics_metrics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->metrics_metrics_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session_set_id_post**
> object start_session_set_id_post(id)

Start Session

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Start Session
        api_response = api_instance.start_session_set_id_post(id)
        print("The response of DefaultApi->start_session_set_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->start_session_set_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **talk_content_talk_content_post**
> object talk_content_talk_content_post(files, text=text, user_id=user_id)

Talk Content

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    files = None # List[bytearray] | 
    text = 'text_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Talk Content
        api_response = api_instance.talk_content_talk_content_post(files, text=text, user_id=user_id)
        print("The response of DefaultApi->talk_content_talk_content_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->talk_content_talk_content_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **List[bytearray]**|  | 
 **text** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **talk_talk_post**
> object talk_talk_post(content, user_id=user_id)

Talk

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    content = 'content_example' # str | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Talk
        api_response = api_instance.talk_talk_post(content, user_id=user_id)
        print("The response of DefaultApi->talk_talk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->talk_talk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**|  | 
 **user_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **talk_with_gitbook_talk_gitbook_post**
> object talk_with_gitbook_talk_gitbook_post(url, text, user_id)

Talk With Gitbook

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    url = 'url_example' # str | 
    text = 'text_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Talk With Gitbook
        api_response = api_instance.talk_with_gitbook_talk_gitbook_post(url, text, user_id)
        print("The response of DefaultApi->talk_with_gitbook_talk_gitbook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->talk_with_gitbook_talk_gitbook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 
 **text** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcribe_transcribe_post**
> object transcribe_transcribe_post(files)

Transcribe

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    files = None # List[bytearray] | 

    try:
        # Transcribe
        api_response = api_instance.transcribe_transcribe_post(files)
        print("The response of DefaultApi->transcribe_transcribe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->transcribe_transcribe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **List[bytearray]**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

