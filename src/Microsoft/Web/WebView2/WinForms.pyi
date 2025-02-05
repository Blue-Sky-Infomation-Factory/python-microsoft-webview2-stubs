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
	AdditionalBrowserArguments: str
	BrowserExecutableFolder: str
	IsInPrivateModeEnabled: bool
	Language: str
	ProfileName: str
	UserDataFolder: str

class WebView2(Control):
	AllowDrop: Final[bool]
	AllowExternalDrop: bool
	CanGoBack: Final[bool]
	CanGoForward: Final[bool]
	ContextMenu: Final[object]
	ContextMenuStrip: Final[object]
	CoreWebView2: Final[Optional[CoreWebView2]]
	CreationProperties: Optional[CoreWebView2CreationProperties]
	DefaultBackgroundColor: object
	Font: Final[object]
	Source: Uri
	Text: Final[str]
	ZoomFactor: float

	CoreWebView2InitializationCompleted: EventHandler[Self, CoreWebView2InitializationCompletedEventArgs]
	NavigationCompleted: EventHandler[Self, CoreWebView2NavigationCompletedEventArgs]
	NavigationStarting: EventHandler[Self, CoreWebView2NavigationStartingEventArgs]
	WebMessageReceived: EventHandler[Self, CoreWebView2WebMessageReceivedEventArgs]