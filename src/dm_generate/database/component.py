from attrs import asdict, define, field


@define
class Component:
    id: str = field()
    current: str = field()
    datasheet: str = field()
    datasheet_local: str = field()
    desc: str = field()
    exclude_from_board: bool = field()
    exclude_from_bom: bool = field()
    footprint: str = field()
    height: str = field()
    keywords: str = field()
    manufacturer_name: str = field()
    manufacturer_pn: str = field()
    package: str = field()
    power: str = field()
    sub_requirements: str = field()
    symbol: str = field()
    tolerance: str = field()
    type: str = field()
    value: str = field()
    vendor_name: str = field()
    vendor_pn: str = field()
    qualification: str = field()
    voltage: str = field()
    vendor_pn_url: str = field()
    datasheet_local_url: str = field()

    @property
    def description(self) -> str:
        parts = [
            "desc",
            "value",
            "current",
            "voltage",
            "power",
            "qualification",
            "package",
        ]
        d_keys = asdict(self, filter=lambda attr, value: attr.name in parts)
        result = ", ".join(d_keys)
        return result
