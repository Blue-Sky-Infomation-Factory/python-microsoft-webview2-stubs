"""
https://learn.microsoft.com/zh-cn/dotnet/api/microsoft.web.webview2.core
"""

from enum import Enum
from System import Uri

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

class CoreWebView2InitializationCompletedEventArgs:
	@property
	def IsSuccess(self) -> bool: ...
	@property
	def InitializationException (self) -> object: ...

class CoreWebView2NavigationStartingEventArgs:
	AdditionalAllowedFrameAncestors: str
	Cancel: bool
	@property
	def IsRedirected(self) -> bool: ...
	@property
	def IsUserInitiated(self) -> bool: ...
	@property
	def NavigationId(self) -> int: ...
	@property
	def NavigationKind(self) -> CoreWebView2NavigationKind: ...
	@property
	def RequestHeaders(self) -> object: ...
	@property
	def Uri(self) -> str: ...

class CoreWebView2NavigationCompletedEventArgs:
	AdditionalAllowedFrameAncestors: str
	Cancel: bool
	@property
	def IsRedirected(self) -> bool: ...
	@property
	def IsUserInitiated(self) -> bool: ...
	@property
	def NavigationId(self) -> int: ...
	@property
	def NavigationKind(self) -> CoreWebView2NavigationKind: ...
	@property
	def RequestHeaders(self) -> object: ...
	@property
	def Uri(self) -> Uri: ...