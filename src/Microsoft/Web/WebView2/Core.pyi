"""
https://learn.microsoft.com/zh-cn/dotnet/api/microsoft.web.webview2.core
"""

from enum import Enum
from typing import Any, Final, List, Tuple, overload
from System import CSharpObject, EventArgs
from System.Threading.Tasks import Tasks

class CoreWebView2PermissionState(Enum):
	# Specifies that the default browser behavior is used, which normally prompts users for decision.
	Default = 0
	# Specifies that the permission request is granted.
	Allow = 1
	#Specifies that the permission request is denied.
	Deny = 2

class CoreWebView2HostResourceAccessKind(Enum):
	# All cross origin resource access is denied, including normal sub resource access as src of a script or image element.
	Deny = 0
	# All cross origin resource access is allowed, including accesses that are subject to Cross-Origin Resource Sharing(CORS) check.
	# The behavior is similar to a web site sends back http header Access-Control-Allow-Origin: *.
	Allow = 1
	# Cross origin resource access is allowed for normal sub resource access like as src of a script or image element,
	# while any access that subjects to CORS check will be denied.
	# See Cross-Origin Resource Sharing for more information.
	DenyCors = 2

class CoreWebView2NavigationKind(Enum):
	# A navigation caused by CoreWebView2.Reload(), location.reload(), the end user using F5 or other UX, or other reload mechanisms
	# to reload the current document without modifying the navigation history.
	Reload = 0
	# A navigation back or forward to a different entry in the session navigation history,
	# like via CoreWebView2.Back(), location.back(), the end user pressing Alt+Left or other UX, or other mechanisms
	# to navigate back or forward in the current session navigation history.
	BackOrForward = 1
	# A navigation to another document,
	# which can be caused by CoreWebView2.Navigate(), window.location.href = ..., or other WebView2 or DOM APIs that navigate to a new URI.
	NewDocument = 2

class CoreWebView2WebErrorStatus(Enum):
	# Indicates that an unknown error occurred.
	Unknown = 0
	# Indicates that the SSL certificate common name does not match the web address.
	CertificateCommonNameIsIncorrect = 1
	# Indicates that the SSL certificate has expired.
	CertificateExpired = 2
	# Indicates that the SSL client certificate contains errors.
	ClientCertificateContainsErrors = 3
	# Indicates that the SSL certificate has been revoked.
	CertificateRevoked = 4
	# Indicates that the SSL certificate is not valid.
	# The certificate may not match the public key pins for the host name,
	# the certificate is signed by an untrusted authority or using a weak sign algorithm,
	# the certificate claimed DNS names violate name constraints,
	# the certificate contains a weak key, the validity period of the certificate is too long,
	# lack of revocation information or revocation mechanism, non-unique host name, lack of certificate transparency information,
	# or the certificate is chained to a legacy Symantec root.
	CertificateIsInvalid = 5
	# Indicates that the host is unreachable.
	ServerUnreachable = 6
	# Indicates that the connection has timed out.
	Timeout = 7
	# Indicates that the server returned an invalid or unrecognized response.
	ErrorHttpInvalidServerResponse = 8
	# Indicates that the connection was stopped.
	ConnectionAborted = 9
	# Indicates that the connection was reset.
	ConnectionReset = 10
	# Indicates that the Internet connection has been lost.
	Disconnected = 11
	# Indicates that a connection to the destination was not established.
	CannotConnect = 12
	# Indicates that the provided host name was not able to be resolved.
	HostNameNotResolved = 13
	# Indicates that the operation was canceled.
	# This status code is also used in the following cases:
	# 1) when the app cancels a navigation via NavigationStarting event.
	# 2) For original navigation if the app navigates the WebView2 in a rapid succession away after the load for original navigation commenced, but before it completed.
	OperationCanceled = 14
	# Indicates that the request redirect failed.
	RedirectFailed = 15
	# Indicates that an unexpected error occurred.
	UnexpectedError = 16
	# Indicates that user is prompted with a login, waiting on user action.
	# Initial navigation to a login site will always return this even if app provides credential using BasicAuthenticationRequested.
	# HTTP response status code in this case is 401. See status code reference here: https://developer.mozilla.org/docs/Web/HTTP/Status.
	ValidAuthenticationCredentialsRequired = 17
	# Indicates that user lacks proper authentication credentials for a proxy server.
	# HTTP response status code in this case is 407. See status code reference here: https://developer.mozilla.org/docs/Web/HTTP/Status.
	ValidProxyAuthenticationRequired = 18

class CoreWebView2HttpRequestHeaders(CSharpObject):
	# incomplete
	pass

class CoreWebView2InitializationCompletedEventArgs(EventArgs):
	def __init__(self):
		self.IsSuccess: Final[bool]
		self.InitializationException: Final[object]

class CoreWebView2NavigationStartingEventArgs(EventArgs):
	def __init__(self):
		self.AdditionalAllowedFrameAncestors: str
		self.Cancel: bool
		self.IsRedirected: Final[bool]
		self.IsUserInitiated: Final[bool]
		self.NavigationId: Final[int]
		self.NavigationKind: Final[CoreWebView2NavigationKind]
		self.RequestHeaders: Final[CoreWebView2HttpRequestHeaders]
		self.Uri: Final[str]

class CoreWebView2NavigationCompletedEventArgs(EventArgs):
	def __init__(self):
		self.HttpStatusCode: Final[int]
		self.IsSuccess: Final[bool]
		self.NavigationId: Final[int]
		self.WebErrorStatus: Final[CoreWebView2WebErrorStatus]

class CoreWebView2WebMessageReceivedEventArgs(EventArgs):
	def __init__(self):
		self.AdditionalObjects: Final[Tuple[Any]]
		self.Source: Final[str]
		self.WebMessageAsJson: Final[str]

class CoreWebView2(CSharpObject):
	# incomplete
	@overload
	def PostWebMessageAsJson(self, messageJson: str) -> None: ...
	@overload
	def PostWebMessageAsJson(self, messageJson: str, additional_objects: List[object]) -> None: ...
	def ExecuteScriptAsync(script: str) -> Tasks: ...