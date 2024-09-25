from enum import Enum


class WindDirection(str, Enum):
    N = "n"
    NE = "ne"
    E = "e"
    SE = "se"
    S = "s"
    SW = "sw"
    W = "w"
    NW = "nw"


WIND_DIRECTION_MAP = {
    WindDirection.N: "С",
    WindDirection.NE: "СВ",
    WindDirection.E: "В",
    WindDirection.SE: "ЮВ",
    WindDirection.S: "Ю",
    WindDirection.SW: "ЮЗ",
    WindDirection.W: "З",
    WindDirection.NW: "СЗ",
}

PRECIPITATION_TYPE_MAP = {
    0: "без осадков",
    1: "дождь",
    2: "дождь со снегом",
    3: "снег",
    4: "град",
}
