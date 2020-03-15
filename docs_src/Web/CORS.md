# CORS

- [CORS on Wikipedia]( https://en.wikipedia.org/wiki/Cross-origin_resource_sharing )
- [Same-origin_policy]( https://en.wikipedia.org/wiki/Same-origin_policy )
- [CORS]( https://www.html5rocks.com/en/tutorials/cors/ )

Certain "cross-domain" requests, notably AJAX requests, are forbidden by default by the same-origin security policy of web browsers.

The same-origin policy is an important security concept implemented by web browsers to prevent Javascript code from making requests against a different origin (e.g., different domain, more precisely combination of URI scheme, hostname, and port number ) than the one from which it was served. Although the same-origin policy is effective in preventing resources from different origins, it also prevents legitimate interactions between a server and clients of a known and trusted origin.

Cross-Origin Resource Sharing (CORS) is a technique for relaxing the same-origin policy, allowing Javascript on a web page to consume a REST API served from a different origin.

Cross-origin requests come in two flavors:
1. simple requests
2. "not-so-simple requests" (a term just made up)

## Simple Requests

Simple requests are requests that meet the following criteria:

HTTP Method matches (case-sensitive) one of:
- HEAD
- GET
- POST
 
HTTP Headers matches (case-insensitive):
- Accept
- Accept-Language
- Content-Language
- Last-Event-ID
- Content-Type, but only if the value is one of `application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`

## Handling a not-so-simple request

A not-so-simple request looks like a single request to the client, but it actually consists of two requests under the hood. The browser first issues a preflight request, which is like asking the server for permission to make the actual request. Once permissions have been granted, the browser makes the actual request. The browser handles the details of these two requests transparently. The preflight response can also be cached so that it is not issued on every request.

Some Javascript libraries, such as AngularJS and Sencha Touch, send preflight requests for any kind of request. This approach is arguably safer, because it doesn't assume that a service adheres to HTTP method semantics (i.e., a GET endpoint could have been written to have side effects.)


## API Gateway and CORS

[How to CORS (AWS)]( https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors.html )






