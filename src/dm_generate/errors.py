class PluginError(ImportError):
    """Raised for a missing or unknown DM plugin."""

    def __init__(
        self,
        *args: object,
        name: str | None = None,
        path: str | None = None,
        msg: str = "",
    ) -> None:
        super().__init__(*args, name=name, path=path)
        self.msg = msg
