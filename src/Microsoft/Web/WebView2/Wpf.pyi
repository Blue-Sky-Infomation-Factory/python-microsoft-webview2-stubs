"""
https://learn.microsoft.com/zh-cn/dotnet/api/microsoft.web.webview2.wpf
"""

from abc import ABC, abstractmethod
from typing import Final, Optional, Self
from .Core import CoreWebView2
from System import IDisposable, IKeyboardInputSink, Object, EventHandler, Uri
from System.Drawing import Color
from System.Windows.Controls import Control
from System.Windows.Interop import HwndHost
from Microsoft.Web.WebView2.Core import (
	CoreWebView2InitializationCompletedEventArgs,
	CoreWebView2NavigationStartingEventArgs,
	CoreWebView2NavigationCompletedEventArgs,
	CoreWebView2WebMessageReceivedEventArgs
)

class CoreWebView2CreationProperties(Object):
	def __init__(self):
		self.AdditionalBrowserArguments: str
		self.BrowserExecutableFolder: str
		self.IsInPrivateModeEnabled: bool
		self.Language: str
		self.ProfileName: str
		self.UserDataFolder: str

class IWebView2(IDisposable, ABC):
	# incomplete
	@property
	@abstractmethod
	def CoreWebView2(self) -> Optional[CoreWebView2] :...
	@property
	@abstractmethod
	def DefaultBackgroundColor(self) -> Color :...
	@DefaultBackgroundColor.setter
	@abstractmethod
	def DefaultBackgroundColor(self, value: Color) -> None :...
	@property
	@abstractmethod
	def CreationProperties(self) -> Optional[CoreWebView2CreationProperties] :...
	@CreationProperties.setter
	@abstractmethod
	def CreationProperties(self, value: Optional[CoreWebView2CreationProperties]) -> None :...
	@property
	@abstractmethod
	def Source(self) -> Uri :...
	@Source.setter
	@abstractmethod
	def Source(self, value: Uri) -> None :...

	CoreWebView2InitializationCompleted: EventHandler[Self, CoreWebView2InitializationCompletedEventArgs]
	NavigationCompleted: EventHandler[Self, CoreWebView2NavigationCompletedEventArgs]
	NavigationStarting: EventHandler[Self, CoreWebView2NavigationStartingEventArgs]
	WebMessageReceived: EventHandler[Self, CoreWebView2WebMessageReceivedEventArgs]

class WebView2(HwndHost, IWebView2):
	# incomplete
	def __init__(self):
		self.AllowDrop: Final[bool]
		self.AllowExternalDrop: bool
		self.CanGoBack: Final[bool]
		self.CanGoForward: Final[bool]
		self.ContextMenuStrip: Final[object]
		self.Font: Final[object]
		self.Text: Final[str]
		self.ZoomFactor: float

	@property
	def CoreWebView2(self) -> Optional[CoreWebView2] :...
	@property
	def DefaultBackgroundColor(self) -> Color :...
	@DefaultBackgroundColor.setter
	def DefaultBackgroundColor(self, value: Color) -> None :...
	@property
	def CreationProperties(self) -> Optional[CoreWebView2CreationProperties] :...
	@CreationProperties.setter
	def CreationProperties(self, value: Optional[CoreWebView2CreationProperties]) -> None :...
	@property
	def Source(self) -> Uri :...
	@Source.setter
	def Source(self, value: Uri) -> None :...

class WebView2CompositionControl(Control, IKeyboardInputSink, IWebView2):
	@property
	def CoreWebView2(self) -> Optional[CoreWebView2] :...
	@property
	def DefaultBackgroundColor(self) -> Color :...
	@DefaultBackgroundColor.setter
	def DefaultBackgroundColor(self, value: Color) -> None :...
	@property
	def CreationProperties(self) -> Optional[CoreWebView2CreationProperties] :...
	@CreationProperties.setter
	def CreationProperties(self, value: Optional[CoreWebView2CreationProperties]) -> None :...
	@property
	def Source(self) -> Uri :...
	@Source.setter
	def Source(self, value: Uri) -> None :...