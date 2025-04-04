from _typeshed import Incomplete

def CoInitializeEx() -> None: ...
def CoUninitialize() -> None: ...
def RegisterServiceCtrlHandler(serviceName: str, callback, extra_args: bool = ..., /): ...
def LogMsg(errorType: int, eventId: int, inserts: tuple[str, str] | None = ..., /) -> None: ...
def LogInfoMsg(msg: str, /) -> None: ...
def LogErrorMsg(msg: str, /) -> None: ...
def LogWarningMsg(msg: str, /) -> None: ...
def PumpWaitingMessages(firstMessage: int = ..., lastMessage: int = ..., /) -> int: ...
def Debugging(newVal: int = ..., /): ...
def Initialize(eventSourceName: str | None = ..., eventSourceFile: str | None = ..., /) -> None: ...
def Finalize() -> None: ...
def PrepareToHostSingle(klass: Incomplete | None = ..., /) -> None: ...
def PrepareToHostMultiple(service_name: str, klass, /) -> None: ...
def RunningAsService(): ...
def SetEventSourceName(sourceName: str, registerNow: bool = ..., /) -> None: ...
def StartServiceCtrlDispatcher(): ...

COINIT_APARTMENTTHREADED: int
COINIT_DISABLE_OLE1DDE: int
COINIT_MULTITHREADED: int
COINIT_SPEED_OVER_MEMORY: int
EVENTLOG_AUDIT_FAILURE: int
EVENTLOG_AUDIT_SUCCESS: int
EVENTLOG_ERROR_TYPE: int
EVENTLOG_INFORMATION_TYPE: int
EVENTLOG_WARNING_TYPE: int
PYS_SERVICE_STARTED: int
PYS_SERVICE_STARTING: int
PYS_SERVICE_STOPPED: int
PYS_SERVICE_STOPPING: int

class startup_error(Exception): ...
