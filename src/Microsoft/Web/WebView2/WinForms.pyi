"""
https://learn.microsoft.com/zh-cn/dotnet/api/microsoft.web.webview2.winforms
"""

from typing import Optional, Self

from System import EventHandler
from Microsoft.Web.WebView2.Core import CoreWebView2InitializationCompletedEventArgs, CoreWebView2NavigationStartingEventArgs

class CoreWebView2CreationProperties:
	AdditionalBrowserArguments: str
	BrowserExecutableFolder: str
	IsInPrivateModeEnabled: bool
	Language: str
	ProfileName: str
	UserDataFolder: str

class WebView2:
	@property
	def AllowDrop(self) -> bool: ...
	AllowExternalDrop: bool
	@property
	def CanGoBack(self) -> bool: ...
	@property
	def CanGoForward(self) -> bool: ...
	@property
	def ContextMenu(self) -> object: ...
	@property
	def ContextMenuStrip(self) -> object: ...
	@property
	def CoreWebView2(self) -> Optional[object]: ...
	@property
	def CreateParams(self) -> object: ...
	CreationProperties: Optional[CoreWebView2CreationProperties]
	DefaultBackgroundColor: object
	@property
	def Font(self) -> object: ...
	Source: object
	@property
	def Text(self) -> str: ...
	ZoomFactor: float

	def Dispose(self, disposing: bool) -> None: ...

	CoreWebView2InitializationCompleted: EventHandler[Self, CoreWebView2InitializationCompletedEventArgs]
	NavigationStarting:  EventHandler[Self, CoreWebView2NavigationStartingEventArgs]