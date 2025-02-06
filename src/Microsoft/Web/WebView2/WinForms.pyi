"""
https://learn.microsoft.com/zh-cn/dotnet/api/microsoft.web.webview2.winforms
"""

from typing import Final, Optional, Self
from .Core import CoreWebView2
from System import CSharpObject, EventHandler, Uri
from System.Windows.Forms import Control
from Microsoft.Web.WebView2.Core import (
	CoreWebView2InitializationCompletedEventArgs,
	CoreWebView2NavigationStartingEventArgs,
	CoreWebView2NavigationCompletedEventArgs,
	CoreWebView2WebMessageReceivedEventArgs
)

class CoreWebView2CreationProperties(CSharpObject):
	def __init__(self):
		self.AdditionalBrowserArguments: str
		self.BrowserExecutableFolder: str
		self.IsInPrivateModeEnabled: bool
		self.Language: str
		self.ProfileName: str
		self.UserDataFolder: str

class WebView2(Control):
	# incomplete
	def __init__(self):
		self.AllowDrop: Final[bool]
		self.AllowExternalDrop: bool
		self.CanGoBack: Final[bool]
		self.CanGoForward: Final[bool]
		self.ContextMenu: Final[object]
		self.ContextMenuStrip: Final[object]
		self.CoreWebView2: Final[Optional[CoreWebView2]]
		self.CreationProperties: Optional[CoreWebView2CreationProperties]
		self.DefaultBackgroundColor: object
		self.Font: Final[object]
		self.Source: Uri
		self.Text: Final[str]
		self.ZoomFactor: float

	CoreWebView2InitializationCompleted: EventHandler[Self, CoreWebView2InitializationCompletedEventArgs]
	NavigationCompleted: EventHandler[Self, CoreWebView2NavigationCompletedEventArgs]
	NavigationStarting: EventHandler[Self, CoreWebView2NavigationStartingEventArgs]
	WebMessageReceived: EventHandler[Self, CoreWebView2WebMessageReceivedEventArgs]